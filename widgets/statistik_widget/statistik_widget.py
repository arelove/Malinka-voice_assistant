__author__ = 'Ar3love'

import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
import csv


class StatsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.session_start_time = time.time()

        self.layout = QVBoxLayout(self)

        self.layout.setSpacing(10)

        self.total_usage_time = 0
        self.usage_time_label = QLabel("Общее время использования: 0 минут")
        self.usage_time_label.setFixedHeight(20)
        self.layout.addWidget(self.usage_time_label)
        self.set_label_style(self.usage_time_label, padding=20, align='left')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_usage_time)
        self.timer.start(60000)  # обновлять каждую минуту

        self.button_clicks_label = QLabel("Количество включений голосового ассистента: 0")
        self.program_starts_label = QLabel("Количество включений программы: 0")
        self.button_clicks_label1 = QLabel("Количество сессий смены пароля: 0")
        self.program_starts_label1 = QLabel("Общее время использования голосового ассистента: 0")
        self.button_clicks_label2 = QLabel("Количество нажатий кнопки: 0")
        self.program_starts_label2 = QLabel("Количество включений программы: 0")
        self.button_clicks_label3 = QLabel("Количество нажатий кнопки: 0")
        self.program_starts_label3 = QLabel("Количество включений программы: 0")
        self.button_clicks_label4 = QLabel("Количество нажатий кнопки: 0")
        self.program_starts_label4 = QLabel("Количество включений программы: 0")
        self.button_clicks_label5 = QLabel("Количество нажатий кнопки: 0")
        self.program_starts_label5 = QLabel("Количество включений программы: 0")

        self.button_clicks_label.setFixedHeight(20)
        self.program_starts_label.setFixedHeight(20)
        self.button_clicks_label1.setFixedHeight(20)
        self.program_starts_label1.setFixedHeight(20)
        self.button_clicks_label2.setFixedHeight(20)
        self.program_starts_label2.setFixedHeight(20)
        self.button_clicks_label3.setFixedHeight(20)
        self.program_starts_label3.setFixedHeight(20)
        self.button_clicks_label4.setFixedHeight(20)
        self.program_starts_label4.setFixedHeight(20)
        self.button_clicks_label5.setFixedHeight(20)
        self.program_starts_label5.setFixedHeight(20)

        self.set_label_style(self.button_clicks_label, padding=20, align='left')
        self.set_label_style(self.program_starts_label, padding=20, align='left')
        self.set_label_style(self.button_clicks_label1, padding=20, align='left')
        self.set_label_style(self.program_starts_label1, padding=20, align='left')
        self.set_label_style(self.button_clicks_label2, padding=20, align='left')
        self.set_label_style(self.program_starts_label2, padding=20, align='left')
        self.set_label_style(self.button_clicks_label3, padding=20, align='left')
        self.set_label_style(self.program_starts_label3, padding=20, align='left')
        self.set_label_style(self.button_clicks_label4, padding=20, align='left')
        self.set_label_style(self.program_starts_label4, padding=20, align='left')
        self.set_label_style(self.button_clicks_label5, padding=20, align='left')
        self.set_label_style(self.program_starts_label5, padding=20, align='left')

        self.layout.addWidget(self.button_clicks_label)
        self.layout.addWidget(self.program_starts_label)
        self.layout.addWidget(self.button_clicks_label1)
        self.layout.addWidget(self.program_starts_label1)
        self.layout.addWidget(self.button_clicks_label2)
        self.layout.addWidget(self.program_starts_label2)
        self.layout.addWidget(self.button_clicks_label3)
        self.layout.addWidget(self.program_starts_label3)
        self.layout.addWidget(self.button_clicks_label4)
        self.layout.addWidget(self.program_starts_label4)
        self.layout.addWidget(self.button_clicks_label5)
        self.layout.addWidget(self.program_starts_label5)

        # Загрузить статистику из CSV-файла
        self.load_stats_from_csv('unique_csv/stats.csv')

        self.update_usage_time()
        # Увеличиваем счетчик запусков программы
        self.program_starts_count += 1
        # Обновляем метку и сохраняем статистику
        self.update_program_starts(self.program_starts_count)

    def set_label_style(self, label, padding, align):
        label.setStyleSheet(f"""
               padding: {padding}px;
               text-align: {align};
           """)

################################
    def update_usage_time(self):
        self.total_usage_time += 1  # увеличиваем на одну минуту
        self.usage_time_label.setText(f"Общее время использования: {int(self.total_usage_time)} минут")
        # Сохранить статистику в CSV-файл
        self.save_stats_to_csv('unique_csv/stats.csv')
################################

    def button_clicked(self):
        # Увеличиваем счетчик нажатий кнопки
        self.button_clicks_count += 1
        # Обновляем метку
        self.update_button_clicks(self.button_clicks_count)
        # Сохраняем статистику в CSV-файл
        self.save_stats_to_csv('unique_csv/stats.csv')

    def load_stats_from_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                stats = next(reader)
                self.button_clicks_count = int(stats[0])
                self.program_starts_count = int(stats[1])
                if len(stats) > 2:  # проверка на количество элементов в строке
                    self.total_usage_time = float(stats[2])
                else:
                    self.total_usage_time = 0
        except FileNotFoundError:
            # Если файл не найден, инициализируем счетчики нулями
            self.button_clicks_count = 0
            self.program_starts_count = 0
            self.total_usage_time = 0
        # ...

        # Обновить метки
        self.update_button_clicks(self.button_clicks_count)
        self.update_program_starts(self.program_starts_count)

    def update_button_clicks(self, count):
        self.button_clicks_label.setText(f"Количество нажатий кнопки: {count}")
        # Сохранить статистику в CSV-файл
        self.save_stats_to_csv('unique_csv/stats.csv')

    def update_program_starts(self, count):
        self.program_starts_label.setText(f"Количество включений программы: {count}")
        # Сохранить статистику в CSV-файл
        self.save_stats_to_csv('unique_csv/stats.csv')

    def save_stats_to_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([self.button_clicks_count, self.program_starts_count, round(self.total_usage_time)])
