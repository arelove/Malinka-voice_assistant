__author__ = 'Ar3love'

from datetime import datetime
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,  QGridLayout, QHBoxLayout
from PySide6.QtGui import QPixmap, QPainter
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные окружения из файла .env
api_key_weather = os.getenv('WEATHER_API_KEY')


class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.api_key = api_key_weather
        self.description = ""
        self.initUI()

    def get_weather(self, city):
        city = self.city_input.text() or "Moscow"
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&lang=ru")
        data = response.json()

        # накладываем изображение дождя или снега, если они есть
        if 'main' in data and 'weather' in data:
            self.temp = round(data['main']['temp'] - 273.15, 2)
            self.description = data['weather'][0]['description']  # обновляем self.description
            pixmap = QPixmap('images/images/sun.png')

            # устанавливаем изображение в зависимости от погоды
            if "дождь" in self.description:
                pixmap = QPixmap('images/images/rain.png')
            elif "снег" in self.description:
                pixmap = QPixmap('images/images/snow.png')
            elif "ясно" in self.description:
                pixmap = QPixmap('images/images/sun.png')
            elif ("облачно с прояснениями" in self.description
                  or "небольшая облачность" in self.description
                  or "пасмурно" in self.description):
                pixmap = QPixmap('images/images/cloud.png')
            self.weather_icon.setPixmap(pixmap)

        else:
            # Показать сообщение об ошибке
            self.temp_label.setText("Ошибка при получении данных погоды")
            self.desc_label.setText("")

        self.humidity = data['main']['humidity']
        self.pressure = data['main']['pressure']
        self.wind_speed = data['wind']['speed']
        self.wind_direction = data['wind']['deg']

        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        self.sun_info = f"Восход: {sunrise.strftime('%H:%M')}, Закат: {sunset.strftime('%H:%M')}"

    def initUI(self):
        # Set widget's background color
        # self.setStyleSheet("background-color: #add8e6; color: #000080;")

        layout = QVBoxLayout(self)
        grid_layout = QGridLayout()

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Введите название города")
        self.city_input.setStyleSheet("""
            QLineEdit {
                min-height: 10px;
                border-radius: 5px;
            }
        """)

        self.search_button = QPushButton("Поиск")
        self.search_button.setStyleSheet("""
            QPushButton {
                color: #FFFFFF; 
                background-color: #000080; 
                border: none;
                min-height: 10px;
                border-radius: 5px;
                padding: 2px 12px;
                text-align: center;
                text-decoration: none;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #00004b;
            }
            QPushButton:pressed {
                background-color: #000035;
            }
        """)

        self.search_button.clicked.connect(self.update_weather)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.city_input)
        search_layout.addWidget(self.search_button)

        self.temp_label = QLabel()
        self.desc_label = QLabel()
        self.humidity_label = QLabel()
        self.pressure_label = QLabel()
        self.wind_label = QLabel()
        self.sun_info_label = QLabel()
        self.weather_icon = QLabel()

        # Set a custom style for each label
        for label in [self.temp_label]:
            label.setStyleSheet("font-size: 20px; padding: 3px;")

        for label in [self.desc_label, self.humidity_label, self.pressure_label, self.wind_label, self.sun_info_label]:
            label.setStyleSheet("font-size: 12px; padding: 2px;")

        # Add widgets to the grid layout
        grid_layout.addWidget(self.weather_icon, 0, 0, 4, 1)  # Целиком в первом столбце
        grid_layout.addWidget(self.temp_label, 0, 1, 4, 1)  # Целиком во втором столбце
        grid_layout.addWidget(self.desc_label, 0, 2)
        grid_layout.addWidget(self.humidity_label, 1, 2)
        grid_layout.addWidget(self.pressure_label, 0, 3)
        grid_layout.addWidget(self.wind_label, 1, 3)
        grid_layout.addWidget(self.sun_info_label, 2, 2, 1, 2)

        layout.addLayout(search_layout)
        layout.addLayout(grid_layout)

        self.setLayout(layout)
        self.update_weather()

    def update_weather(self):
        city = self.city_input.text() or "Moscow"
        self.get_weather(city)

        # self.temp_label.setText(f"Температура: {self.temp} C")
        # self.desc_label.setText(f"Описание: {self.description}")
        # self.humidity_label.setText(f"Влажность: {self.humidity}%")
        # self.pressure_label.setText(f"Давление: {self.pressure} hPa")
        # self.wind_label.setText(f"Ветер: {self.wind_speed} м/с, направление {self.wind_direction} градусов")
        # self.sun_info_label.setText(self.sun_info)

        self.temp_label.setText(f"{self.temp} C")
        self.desc_label.setText(f"{self.description}")
        self.humidity_label.setText(f"{self.humidity}%")
        self.pressure_label.setText(f"{self.pressure} hPa")
        self.wind_label.setText(f"{self.wind_speed} м/с")
        self.sun_info_label.setText(self.sun_info)

        # self.set_weather_icon()


if __name__ == '__main__':
    app = QApplication([])
    weather_widget = WeatherWidget()
    weather_widget.show()
    sys.exit(app.exec())
