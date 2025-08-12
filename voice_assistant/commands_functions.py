__author__ = 'Ar3love'

import webbrowser
import os
import time
import random
from threading import Timer
import datetime
import wave
import pyaudio
import subprocess
import speech_recognition as sr
from g4f.client import Client
import g4f


class AssistantFunctions:
    def __init__(self, assistant):
        self.assistant = assistant
        self.backup_folder = 'backups'  # Замените на путь к папке для резервных копий
        self.reminder_timers = []  # Список для таймеров напоминаний
        self.ordinal_to_index = {
            "первый": 0,
            "второй": 1,
            "третий": 2,
            "четвёртый": 3,
            "пятый": 4,
            "шестой": 5,
            "седьмой": 6,
            "восьмой": 7,
            "девятый": 8,
            "десятый": 9,
            # Добавьте больше чисел по мере необходимости
        }
        g4f.debug.logging = True
        g4f.debug.version_check = False
        self.client = Client()

    def format_code(self, file_path):
        # Запускаем black для автоматического форматирования кода
        subprocess.run(['black', file_path])

    def test_code(self, file_path):
        # Запускаем код в фоновом режиме
        process = subprocess.Popen(
            ['venv/Scripts/python.exe', file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Выводим результат выполнения кода
        stdout, stderr = process.communicate()
        print(stdout.decode())

        # Выводим ошибки, если они есть
        if stderr:
            print("Ошибки:")
            print(stderr.decode())

    # Функция для чтения файла
    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    # Функция для записи в файл
    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    # Функция для создания резервной копии файла
    def backup_file(self, file_path, backup_folder):
        filename = os.path.basename(file_path)
        base_name, extension = os.path.splitext(filename)
        backup_path = os.path.join(backup_folder, base_name + '.backup' + extension)
        counter = 1
        while os.path.exists(backup_path):
            backup_path = os.path.join(backup_folder, f"{base_name}.backup{counter}{extension}")
            counter += 1
        content = self.read_file(file_path)
        self.write_file(backup_path, content)

    def list_files(self, directory):
        files = os.listdir(directory)
        file_dict = {}
        file_count = 0
        for file in files:
            if os.path.isdir(os.path.join(directory, file)):
                print(f"+ {file}")
            else:
                print(f"{self.ordinal_to_index.get(str(file_count), file_count + 1)}: {file}")
                file_dict[self.ordinal_to_index.get(str(file_count), file_count)] = file
                file_count += 1
        return file_dict

    def search_web(self, query):
        webbrowser.open("https://www.google.com/search?q=" + query)

    def open_youtube(self, query):
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)

    def mstasks(self):
        os.system('taskmgr')

    def play_random_quote_and_sound(self):
        directory = "voice_assistant/quotes"
        files = [f for f in os.listdir(directory) if f.endswith('.wav')]
        filename = random.choice(files)
        full_path = os.path.join(directory, filename)
        print(full_path)  # Проверка полного пути
        self.play_sound_func(full_path)  # вызов метода вашего класса

    def play_sound_func(self, filename):
        chunk = 1024
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(chunk)

        while data != b'':
            stream.write(data)
            data = wf.readframes(chunk)

        stream.close()
        p.terminate()

    def create_reminder(self, time_for_reminder, reminder_sound_file):
        # Функция принимает время напоминания и путь к звуковому файлу
        reminder_time = self.parse_time_input(time_for_reminder)
        current_time = time.time()
        delay = reminder_time - current_time
        if delay > 0:  # Если время напоминания еще не прошло
            # Создаем и стартуем таймер
            timer = Timer(delay, self.play_sound_func, [reminder_sound_file])
            timer.start()
            self.reminder_timers.append(timer)
            print(f"Напоминание установлено на {time_for_reminder}")
        else:
            print("Указано прошедшее время. Напоминание не может быть создано.")

    def parse_time_input(self, time_str):
        # Формат времени будет, например, "HH:MM" (24-часовой формат)
        try:
            # Преобразование строки времени в объект datetime.time
            reminder_time = datetime.datetime.strptime(time_str, "%H:%M").time()
            # Получение текущей даты и времени
            now = datetime.datetime.now()
            # Комбинирование текущей даты с временем напоминания
            reminder_datetime = datetime.datetime.combine(now.date(), reminder_time)
            # Если указанное время уже прошло, добавляем 1 день
            if reminder_datetime < now:
                reminder_datetime += datetime.timedelta(days=1)
            # Возвращаем timestamp
            return reminder_datetime.timestamp()
        except ValueError:
            print("Неправильный формат времени.")
            return None

    def listen_command_end(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:  # Добавляем цикл для бесконечного ожидания команды
                print("Скажите команду:")
                audio = r.listen(source)
                try:
                    command = r.recognize_google(audio, language='ru-RU')
                    print("Вы сказали: " + command)
                    return command.lower()
                except sr.UnknownValueError:
                    print("Не удалось распознать команду")

    def reserve_file(self, text):
        print("Выберите файл для создания резервной копии:")
        files = self.list_files('.')
        while True:  # Добавляем внутренний цикл, чтобы ждать команды выбора файла
            file_name = self.listen_command_end()
            if file_name == "давай в начало":
                break  # Прерываем внутренний цикл, если получена команда "давай в начало"
            if file_name is not None:
                file_number = None
                for word in file_name.split():
                    file_number = self.ordinal_to_index.get(word.lower(), None)
                    if file_number is not None:
                        break
                if file_number is not None:
                    file_path = files.get(file_number, None)
                    if file_path is not None:
                        self.backup_file(file_path, self.backup_folder)
                        print(f"Резервная копия для {file_path} создана.")
                        break  # Прерываем внутренний цикл, если резервная копия была успешно создана
                    else:
                        print("Некорректный номер файла.")
                else:
                    print("Не удалось распознать команду.")
            else:
                print("Не удалось распознать команду.")

    def reading_file(self, text):
        files = self.list_files('.')
        while True:  # Добавляем внутренний цикл, чтобы ждать команды выбора файла
            file_name = self.listen_command_end()
            if file_name == "давай в начало":
                break  # Прерываем внутренний цикл, если получена команда "давай в начало"
            if file_name is not None:
                file_number = None
                for word in file_name.split():
                    file_number = self.ordinal_to_index.get(word.lower(), None)
                    if file_number is not None:
                        break
                if file_number is not None:
                    file_path = files.get(file_number, None)
                    if file_path is not None:
                        content = self.read_file(file_path)  # Читаем файл вместо создания резервной копии
                        print(f"Содержимое файла {file_path}:\n{content}")  # Выводим содержимое файла
                        break  # Прерываем внутренний цикл, если файл был успешно прочитан
                    else:
                        print("Некорректный номер файла.")
                else:
                    print("Не удалось распознать команду.")
            else:
                print("Не удалось распознать команду.")

    def run_code(self, text):
        files = self.list_files('.')
        while True:  # Добавляем внутренний цикл, чтобы ждать команды выбора файла
            file_name = self.listen_command_end()
            if file_name == "давай в начало":
                break  # Прерываем внутренний цикл, если получена команда "давай в начало"
            if file_name is not None:
                file_number = None
                for word in file_name.split():
                    file_number = self.ordinal_to_index.get(word.lower(), None)
                    if file_number is not None:
                        break
                if file_number is not None:
                    file_path = files.get(file_number, None)
                    if file_path is not None:
                        self.test_code(file_path)
                        print(f"Тестирование кода в файле {file_path} завершено.")
                        break  # Прерываем внутренний цикл, если тестирование кода было успешно выполнено
                    else:
                        print("Некорректный номер файла.")
                else:
                    print("Не удалось распознать команду.")
            else:
                print("Не удалось распознать команду.")

    def formate_voice_code(self, text):
        files = self.list_files('backups')
        while True:  # Добавляем внутренний цикл, чтобы ждать команды выбора файла
            file_name = self.listen_command_end()
            if file_name == "давай в начало":
                break  # Прерываем внутренний цикл, если получена команда "давай в начало"
            if file_name is not None:
                file_number = None
                for word in file_name.split():
                    file_number = self.ordinal_to_index.get(word.lower(), None)
                    if file_number is not None:
                        break
                if file_number is not None:
                    file_path = files.get(file_number, None)
                    if file_path is not None:
                        self.format_code(file_path)
                        print(f"Форматирование кода в файле {file_path} завершено.")
                        break  # Прерываем внутренний цикл, если тестирование кода было успешно выполнено
                    else:
                        print("Некорректный номер файла.")
                else:
                    print("Не удалось распознать команду.")
            else:
                print("Не удалось распознать команду.")

    def analyze_data(self, text):
        print("Вот вам файлы для анализа: ")
        files = self.list_files('.')
        while True:  # Добавляем внутренний цикл, чтобы ждать команды выбора файла
            file_name = self.listen_command_end()
            if file_name == "давай в начало":
                break  # Прерываем внутренний цикл, если получена команда "давай в начало"
            if file_name is not None:
                file_number = None
                for word in file_name.split():
                    file_number = self.ordinal_to_index.get(word.lower(), None)
                    if file_number is not None:
                        break
                if file_number is not None:
                    file_path = files.get(file_number, None)
                    if file_path is not None:
                        content = self.read_file(file_path)
                        response = self.client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "user",
                                 "content": "Проанализируй мой код пожалуйста, отвечай только на русском языке, "
                                            "если будут слова на английском переделай их под русские символы."
                                            " Вот мой код:  " + content}
                            ],
                        )
                        result = "Ответ: " + response.choices[0].message.content
                        print(result)
                        file_path = os.path.join('results', f'analysis_result{os.path.basename(file_path)}.txt')
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(result)
                        os.system(file_path)
                    else:
                        print("Некорректный номер файла.")
                else:
                    print("Не удалось распознать команду.")
            else:
                print("Не удалось распознать команду.")

    def improve_code(self, text):
        files = self.list_files('.')
        while True:  # Добавляем внутренний цикл, чтобы ждать команды выбора файла
            file_name = self.listen_command_end()
            if file_name == "давай в начало":
                break  # Прерываем внутренний цикл, если получена команда "давай в начало"
            if file_name is not None:
                file_number = None
                for word in file_name.split():
                    file_number = self.ordinal_to_index.get(word.lower(), None)
                    if file_number is not None:
                        break
                if file_number is not None:
                    file_path = files.get(file_number, None)
                    if file_path is not None:
                        content = self.read_file(file_path)
                        response = self.client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "user",
                                 "content": "Можешь пожалуйста улучшить мой код, отвечай без слов, только код"
                                            " Вот мой код:  " + content}
                            ],
                        )
                        print("Ответ: " + response.choices[0].message.content)

                        self.backup_file(file_path, self.backup_folder)
                        print("Резервная копия создана.")
                        self.write_file(file_path, response.choices[0].message.content)

                        print("Изменения применены.")
                    else:
                        print("Некорректный номер файла.")
                else:
                    print("Не удалось распознать команду.")
            else:
                print("Не удалось распознать команду.")

    def analyze_and_fix_errors(self, text):
        print("Выберите файл для анализа ошибок: ")
        files = self.list_files('.')
        while True:  # Добавляем внутренний цикл, чтобы ждать команды выбора файла
            file_name = self.listen_command_end()
            if file_name == "давай в начало":
                break  # Прерываем внутренний цикл, если получена команда "давай в начало"
            if file_name is not None:
                file_number = None
                for word in file_name.split():
                    file_number = self.ordinal_to_index.get(word.lower(), None)
                    if file_number is not None:
                        break
                if file_number is not None:
                    file_path = files.get(file_number, None)
                    if file_path is not None:
                        content = self.read_file(file_path)
                        # Запускаем код и собираем ошибки
                        process = subprocess.Popen(
                            ['venv/Scripts/python.exe', file_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        stdout, stderr = process.communicate()
                        errors = stderr.decode()
                        # Отправляем код и ошибки в GPT
                        response = self.client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "user",
                                 "content": f"Проанализируй мой код и ошибки, отвечай без слов, "
                                            f"только код и комментарии на русском языке "
                                            f" Вот мой код:  {content}"
                                            f" Вот ошибки: {errors}"}
                            ],
                        )
                        result = "Ответ: " + response.choices[0].message.content
                        print(result)
                        file_path = os.path.join('results', f'analysis_result6{os.path.basename(file_path)}.txt')
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(result)
                        os.system(file_path)
                    else:
                        print("Некорректный номер файла.")
                else:
                    print("Не удалось распознать команду.")
            else:
                print("Не удалось распознать команду.")
