__author__ = 'Ar3love'

import csv
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
import json

# Загружаем данные из файла
with open('config.json', 'r') as f:
    config = json.load(f)

config_voice_data = config['config_voice']


class CurrentSettingsLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создание вертикального лэйаута
        layout = QVBoxLayout()

        # Настройка отступов и интервалов между виджетами
        layout.setSpacing(8)  # Расстояние между виджетами
        layout.setContentsMargins(2, 2, 2, 2)  # Отступы лэйаута

        # Загрузка настроек из файла config.csv
        with open(config_voice_data, 'r') as f:
            reader = csv.reader(f)
            config_data = {rows[0]: rows[1] for rows in reader}

        # Чтение настроек голосового ассистента
        speaker = config_data.get('speaker', 'Не задано')
        tts_model = config_data.get('tts_model', 'Не задано')
        accentizer_enabled = bool(int(config_data.get('accentizer_enabled', '0')))

        # Создание и стилизация виджетов с информацией о настройках
        font = QFont("Arial", 10, QFont.Bold)

        speaker_label = QLabel(f"Голосовой движок: {speaker}")
        speaker_label.setFont(font)
        speaker_label.setStyleSheet("QLabel { color : #007ACC; }")

        tts_model_label = QLabel(f"Модель TTS: {tts_model}")
        tts_model_label.setFont(font)
        tts_model_label.setStyleSheet("QLabel { color : #00B74A; }")

        accentizer_status = "Включен" if accentizer_enabled else "Отключен"
        accentizer_label = QLabel(f"Акцентизатор: {accentizer_status}")
        accentizer_label.setFont(font)
        accentizer_label.setStyleSheet("QLabel { color : #FFA500; }")

        # Добавление информации о настройках в лэйаут
        layout.addWidget(speaker_label)
        layout.addWidget(tts_model_label)
        layout.addWidget(accentizer_label)

        # Установка лэйаута
        self.setLayout(layout)

        # Дополнительная стилизация виджета, если нужно
        self.setStyleSheet("QWidget { background-color: #1E213D; }")
        self.setFixedSize(400, 150)  # Установить фиксированный размер, если требуется

