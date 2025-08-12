__author__ = 'Ar3love'

from PySide6.QtWidgets import QWidget, QPushButton
import torch
import wave
import pyaudio
import speech_recognition as sr
import g4f
import threading
import os
# from g4f.client import Client
from gtts import gTTS
import pygame
from ruaccent import RUAccent
import logging
from voice_assistant.commands_functions import AssistantFunctions
import time
from openai import OpenAI
from TeraTTS import TTS
import csv
from runorm import RUNorm
from dotenv import load_dotenv
import random
import json

# Загружаем данные из файла
with open('config.json', 'r') as f:
    config = json.load(f)

config_voice_data = config['config_voice']
admin_logs_dir = config['admin_logs']['admin_logs_dir']
assistant_logs_file = config['admin_logs']['assistant_logs_file']
flashdrive_watcher_file = config['admin_logs']['flashdrive_watcher_file']
silero_model_file = config['silero_model']


load_dotenv()  # Загружает переменные окружения из файла .env
api_key = os.getenv('API_KEY')


class Assistant:
    def __init__(self):
        # Настройка логгера
        self.logger = logging.getLogger('Assistant')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

        # Лог в файл
        assistant_logs_path = os.path.join(admin_logs_dir, assistant_logs_file)
        file_handler = logging.FileHandler(assistant_logs_path)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Лог в консоль
        if not any(isinstance(handler, logging.StreamHandler) for handler in self.logger.handlers):
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

        self.func_helper = AssistantFunctions(self)
        with open(config_voice_data, 'r') as f:
            reader = csv.reader(f)
            config_data = {rows[0]: rows[1] for rows in reader}

        self.speaker = config_data.get('speaker', 'kseniya')
        self.tts_model = config_data.get('tts_model', 'silero')
        self.accentizer_enabled = bool(int(config_data.get('accentizer_enabled', 1)))

        self.sample_rate = 48000
        self.state = False
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # Инициализация и загрузка RUAccent заранее, если нужно

        self.accentizer = RUAccent()
        self.accentizer.load(omograph_model_size='big_poetry', use_dictionary=True)
        # "TeraTTS/girl_nice-g2p-vits"
        self.tts = TTS("TeraTTS/glados2-g2p-vits-jit", add_time_to_end=1.0, tokenizer_load_dict=False, use_cuda=True, sample_rate=22050)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        self.normalizer = RUNorm()
        self.normalizer.load(model_size="small", device="cuda")

        self.state = False
        # Инициализация модели Silero и её загрузка на CUDA
        self.device = torch.device('cuda')
        torch.set_num_threads(4)
        self.local_file = silero_model_file

        if not os.path.isfile(self.local_file):
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                           self.local_file)

        self.model = torch.package.PackageImporter(self.local_file).load_pickle("tts_models", "model")
        self.model.to(self.device)

        # Определение функций прослушивания
        self.r = sr.Recognizer()

        g4f.debug.logging = True
        g4f.debug.version_check = False

        self.commands = {
                            ("поиск", "найти"): (self.func_helper.search_web, "voice_assistant/sound/jokeGPTorSMTH.wav"),
                            ("youtube",): (self.func_helper.open_youtube, "voice_assistant/sound/jokeGPTorSMTH.wav"),  # Что вы хотите найти на YouTube?
                            ("диспетчер задач",): (self.func_helper.mstasks, "voice_assistant/sound/jokeGPTorSMTH.wav"),  # Вот ваш диспетчер задач
                            # ("отправить почту"): ('sendmail', ""),
                            ("напоминание", "напомни"): (self.func_helper.create_reminder, "voice_assistant/sound/jokeGPTorSMTH.wav"),  # Выберите время для напоминания
                            ("мотивируй меня",): (self.func_helper.play_random_quote_and_sound, "voice_assistant/sound/jokeGPTorSMTH.wav"),
                            ("тестировать", "протестировать"): (self.func_helper.run_code, "voice_assistant/sound/jokeGPTorSMTH.wav"),
                            ("форматировать", "отформатировать", "отформатируй", "форматни"):
                            (self.func_helper.formate_voice_code, "voice_assistant/sound/jokeGPTorSMTH.wav"),
                            ("анализировать", "проанализировать"): (self.func_helper.analyze_data, "voice_assistant/sound/jokeGPTorSMTH.wav"),
                            ("улучшить", "проапгрейдить"): (self.func_helper.improve_code, None),
                            ("резервную копию", "копию"): (self.func_helper.reserve_file, None),
                            ("прочитать файл", "прочитай файл"): (self.func_helper.reading_file, None),
                            ("ошибку", "ошибки"): (self.func_helper.analyze_and_fix_errors, None),
                            ("новый запрос", "можно спросить", "узнать"): (self.coze_gpt_wrapper, "voice_assistant/sound/jokeGPTorSMTH.wav"),
                            ("факт", "факты"): (self.speak_random_fact, None),
                            ("цитата", "цитаты", "грустно"): (self.speak_random_quote, None)
                        }

    def speak_random_quote(self, csv_file):
        # Чтение фактов из CSV файла
        csv_file = 'unique_csv/quotes.csv'
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            facts = list(reader)
        # Выбор случайного факта
        fact = random.choice(facts)[0]  # выбираем первый элемент из списка fact
        # Проговаривание факта
        self.tera_tts(fact)

    def speak_random_fact(self, csv_file):
        # Чтение фактов из CSV файла
        csv_file = 'unique_csv/facts.csv'
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            facts = list(reader)
        # Выбор случайного факта
        fact = random.choice(facts)[0]  # выбираем первый элемент из списка fact
        # Проговаривание факта
        self.tera_tts(fact)

    def coze_gpt_wrapper(self, text):  # обертка для self.coze_gpt
        self.coze_gpt(text)

    def coze_gpt(self, text):
        while True:  # Добавляем внешний цикл для продолжения диалога
            text = self.listen_param()  # Слушаем команду
            if text == "закончим":
                break  # Прерываем внешний цикл, если получена команда "закончим"
                # Чтение данных из CSV файла
            with open(config_voice_data, 'r') as f:
                reader = csv.reader(f)
                config_data = {rows[0]: rows[1] for rows in reader}

            self.tts_model = config_data.get('tts_model', 'silero')
            start_time_gpt = time.time()
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.llama-api.com"
            )
            response = client.chat.completions.create(
                model="llama-13b-chat",
                messages=[
                    {"role": "user",
                     "content": "отвечай только на русском языке, и старайся отвечать коротко в 1-2 предложения "
                                "если будут слова на английском переделай их под русские символы."
                                " Вот мой запрос:  " + text}
                ],
            )

            # Вывод ответа
            full_response = response.choices[0].message.content
            end_time_gpt = time.time()
            # Расчет затраченного времени
            elapsed_time_gpt = end_time_gpt - start_time_gpt
            # Вывод затраченного времени в секундах
            print(f"Время выполнения команды: {elapsed_time_gpt:.2f} секунд.")
            print(full_response)
            self.logger.info(full_response)
            if full_response and not self.state:
                print("Получен пустой ответ от модели.")
            else:
                self.logger.info(full_response)
                if self.tts_model == 'silero':
                    try:
                        self.silero(full_response)
                    except Exception as e:
                        print("Ошибка при синтезе речи:", str(e))
                elif self.tts_model == 'gtts':
                    try:
                        self.gtts(full_response)
                    except Exception as e:
                        print("Ошибка при синтезе речи:", str(e))
                elif self.tts_model == 'tera_tts':
                    try:
                        self.tera_tts(full_response)
                    except Exception as e:
                        print("Ошибка при синтезе речи:", str(e))

    def tera_tts(self, text):
        self.logger.info('Используемое устр-во: {}'.format(self.device))
        if self.device.type == 'cuda':
            self.logger.info(torch.cuda.get_device_name(0))
            self.logger.info('Memory Usage:')
            self.logger.info('Allocated: {} GB'.format(round(torch.cuda.memory_allocated(0) / 1024 ** 3, 1)))
            self.logger.info('Cached:   {} GB'.format(round(torch.cuda.memory_reserved(0) / 1024 ** 3, 1)))

        # Нормализация текста
        normalized_text = self.normalizer.norm(text)
        start_time_ruaccent_tera = time.time()
        if self.accentizer_enabled:
            normalized_text = self.accentizer.process_all(
                normalized_text)  # Обратите внимание, что мы передаем уже нормализованный текст
        end_time_ruaccent_tera = time.time()
        self.logger.info(
            f"Время выполнения обработки текста акцентайзером: {end_time_ruaccent_tera - start_time_ruaccent_tera:.2f} секунд.")
        start_time_tera_audio = time.time()
        audio = self.tts(normalized_text,
                         lenght_scale=1.2, )  # Создать аудио. Здесь тоже используется нормализованный текст
        end_time_tera_audio = time.time()
        self.logger.info(f"Время выполнения обработки текста и генерации аудио: "
                         f"{end_time_tera_audio - start_time_tera_audio:.2f} секунд.")
        self.tts.play_audio(audio)  # Воспроизвести созданное аудио

    def silero(self, text):
        # Использование RUAccent для обработки текста
        start_time_silero = time.time()

        start_time_ruaccent = time.time()
        if self.accentizer_enabled:
            text = self.accentizer.process_all(text)

        end_time_ruaccent = time.time()
        self.logger.info(
            f"Время выполнения обработки текста акцентайзером: {end_time_ruaccent - start_time_ruaccent:.2f} секунд.")

        start_time_silero_acc = time.time()

        self.model.save_wav(text=text, speaker=self.speaker, sample_rate=self.sample_rate)
        end_time_silero_acc = time.time()
        self.logger.info(f"Время выполнения генерации аудио: "
                         f"{end_time_silero_acc - start_time_silero_acc:.2f} секунд.")

        end_time_silero = time.time()
        self.logger.info(f"Время выполнения обработки текста и генерации аудио: "
                         f"{end_time_silero - start_time_silero:.2f} секунд.")

        wf = wave.open('test.wav', 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
        chunk = 1024
        data = wf.readframes(chunk)

        while data:
            if not self.state:
                break
            stream.write(data)
            data = wf.readframes(chunk)

        if not self.state:
            return
        wf.close()
        stream.close()
        p.terminate()

        os.remove('test.wav')  # Удалите временный файл после использования

    def gtts(self, text):
        tts = gTTS(text=text, lang='ru', slow=False)  # Создаем объект gTTS
        tts.save("text_to_speech.mp3")  # Сохраняем аудиофайл в формате MP3
        pygame.mixer.init()
        pygame.mixer.music.load('text_to_speech.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop()  # Останавливаем воспроизведение
        pygame.mixer.quit()  # Завершаем работу с микшером
        os.remove("text_to_speech.mp3")  # Удаляем файл после воспроизведения

    def play_sound(self, filename):
        chunk = 1024
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(chunk)

        while data != b'':
            if not self.state:  # Если состояние изменилось на "выключено", прервать воспроизведение
                break
            stream.write(data)
            data = wf.readframes(chunk)

        stream.close()
        p.terminate()

    def listen_param(self):
        while self.state:  # Пока ассистент включен
            with sr.Microphone() as source:
                print("Слушаю...")
                audio = self.r.listen(source)
            # Проверяем состояние ассистента после ожидания аудио
            if not self.state:
                return None
            try:
                text = self.r.recognize_google(audio, language="ru-RU")
                print("Вы сказали: " + text)
                return text.lower()
            except sr.UnknownValueError:
                # Проверяем состояние ассистента после неудачной попытки распознавания
                if not self.state:
                    return None
                print("Не удалось распознать речь")

        # Если мы вышли из цикла while из-за изменения состояния ассистента, возвращаем None
        return None

    def listen(self):
        while self.state:  # Пока ассистент включен
            with sr.Microphone() as source:
                print("Слушаю...")
                audio = self.r.listen(source)
            try:
                # Распознавание ключевого слова
                keyword = self.r.recognize_google(audio, language='ru-RU')
                if "малинка" in keyword.lower():
                    self.play_sound(os.path.join(self.base_dir, 'sound/yes_yes.wav'))
                    print("Обнаружено ключевое слово. Начало обработки команд.")
                    try:
                        with sr.Microphone() as source:
                            print("Слушаю...")
                            audio = self.r.listen(source)
                            start_time_listen = time.time()
                            text = self.r.recognize_google(audio, language="ru-RU")
                            end_time_listen = time.time()
                            self.logger.info("Вы сказали: " + text)
                            self.logger.info(f"Время распознавания голоса: {end_time_listen - start_time_listen:.2f} сек.")

                        return text.lower()

                    except sr.UnknownValueError:
                        print("Не удалось распознать речь")
                else:
                    if not self.state:  # Если состояние изменилось на "выключено"
                        return None
                # Ваш код ...
            except sr.UnknownValueError:
                if not self.state:  # Если состояние изменилось на "выключено"
                    return None
                print("Не удалось распознать ключевое слово. Попробуйте снова.")
                continue
            return None

    def main(self):
        while True:
            if self.state:  # Если ассистент включен
                text = self.listen()
                if text is None:  # Если функция listen вернула None, значит ассистент выключен
                    return  # Выходим из функции main
                try:
                    if text:
                        for keywords, (function, prompt) in self.commands.items():
                            for keyword in keywords:
                                if keyword in text:
                                    if prompt:
                                        self.play_sound(prompt)
                                        function(text)
                                    else:
                                        function(text)
                except Exception as e:
                    print(f"Не удалось распознать команду {e}")
            # start_time_gpt = time.time()
            # if not command_executed and self.state:  # Проверяем, была ли выполнена команда
            #     # client = Client()
            #     client = OpenAI(
            #         api_key=api_key,
            #         base_url="https://api.llama-api.com"
            #     )
            #     try:
            #         response = client.chat.completions.create(
            #             model="llama-13b-chat",  # gpt-3.5-turbo g4f.models.gpt_4, "llama-13b-chat"
            #             # provider=g4f.Provider.FlowGpt,
            #             messages=[
            #                 {"role": "user",
            #                  "content": "отвечай только на русском языке, и старайся отвечать коротко в 1-2 предложения "
            #                             "если будут слова на английском переделай их под русские символы."
            #                             " Вот мой запрос:  " + text}
            #             ],
            #         )
            #
            #         # Вывод ответа
            #         full_response = response.choices[0].message.content
            #         end_time_gpt = time.time()
            #         # Расчет затраченного времени
            #         elapsed_time_gpt = end_time_gpt - start_time_gpt
            #         # Вывод затраченного времени в секундах
            #         print(f"Время выполнения команды: {elapsed_time_gpt:.2f} секунд.")
            #
            #         # Проверяем, что full_response содержит текст и не None
            #         if full_response and not self.state:
            #             print("Получен пустой ответ от модели.")
            #         else:
            #             self.logger.info(full_response)
            #             if self.tts_model == 'silero':
            #                 try:
            #                     self.silero(full_response)
            #                 except Exception as e:
            #                     print("Ошибка при синтезе речи:", str(e))
            #             elif self.tts_model == 'gtts':
            #                 try:
            #                     self.gtts(full_response)
            #                 except Exception as e:
            #                     print("Ошибка при синтезе речи:", str(e))
            #             elif self.tts_model == 'tera_tts':
            #                 try:
            #                     self.tera_tts(full_response)
            #                 except Exception as e:
            #                     print("Ошибка при синтезе речи:", str(e))
            #
            #     except g4f.errors.RateLimitError as e:
            #         print("Достигнут лимит запросов. Подождите некоторое время перед следующим запросом.")
            #         # Опционально: вы можете добавить задержку перед повторной попыткой
            #     command_executed = False


class ToggleWidget(QWidget, Assistant):
    def __init__(self):
        Assistant.__init__(self)
        super().__init__()

        self.button = QPushButton(text="Включить", parent=self)
        self.button.clicked.connect(self.toggle_function)

    def toggle_function(self):
        self.state = not self.state
        if self.state:
            self.button.setText("Выключить")
            threading.Thread(target=self.main).start()

            print("Ассистент включен")
        else:
            self.button.setText("Включить")
            print("Ассистент выключен")

