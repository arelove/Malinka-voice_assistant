__author__ = 'Ar3love'

from PySide6.QtWidgets import  QWidget, QVBoxLayout, QStackedWidget, QLabel, QPushButton, QHBoxLayout
import requests
from bs4 import BeautifulSoup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtGui import QPainter, QColor


class PageIndicator(QWidget):
    def __init__(self, count=0, current=0, parent=None):
        super().__init__(parent)

        self.count = count
        self.current = current

    def sizeHint(self):
        return QSize(200, 50)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        radius = 5  # изменен размер
        spacing = 10  # изменено расстояние между кружками
        y = self.height() / 2
        total_width = (radius * 2 + spacing) * self.count - spacing
        x = (self.width() - total_width) / 2

        for i in range(self.count):
            color = QColor(43, 45, 115) if i == self.current else QColor(43, 45, 54)
            painter.setBrush(color)  # изменен цвет
            painter.drawEllipse(QPoint(x + i * (radius * 2 + spacing), y), radius, radius)


class CurrencyPage(QWidget):
    def __init__(self, currency, background_image, parent=None):
        super().__init__(parent)

        self.currency = currency
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(255,255,255,0);")  # Установить цвет текста

        self.price_label = QLabel(self)
        self.price_label.setAlignment(Qt.AlignCenter)
        self.price_label.setStyleSheet("background-color: rgba(255,255,255,0);")

        self.container = QWidget(self)  # Создаем контейнер для макета
        self.container.setStyleSheet(
            f"background-image: url({background_image});")  # Устанавливаем фоновое изображение для контейнера

        self.layout = QVBoxLayout(self.container)  # Устанавливаем контейнер как родительский виджет для макета
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.price_label)

        self.container.setLayout(self.layout)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.container)  # Добавляем контейнер в основной макет виджета

        self.setLayout(self.main_layout)

    def update_rates(self):
        # Парсим данные с сайта Центробанка
        url = 'https://www.cbr.ru/currency_base/daily/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ищем таблицу с курсами валют
        table = soup.find('table', {'class': 'data'})
        # Предполагаем, что в таблице есть строки с данными
        rows = table.find_all('tr')[1:]  # Пропускаем заголовок таблицы

        rate = None  # Инициализируем переменную для курса
        base_currency = 'RUB'  # Базовая валюта для конвертации

        # Итерируем по строкам и находим курс нужной валюты
        for row in rows:
            cols = row.find_all('td')
            currency_code = cols[1].text.strip()  # Код валюты
            currency_nominal = float(cols[2].text.replace(',', '.'))  # Номинал валюты
            if currency_code == self.currency:
                rate = float(cols[4].text.replace(',', '.'))
                break

        # Если курс найден, обновляем текст на виджетах
        if rate:
            price_in_foreign_currency = rate / currency_nominal  # стоимость номинала иностранной валюты в рублях
            price_in_rub = 1 / price_in_foreign_currency  # стоимость 1 рубля в иностранной валюте
            self.label.setText(f'1 {self.currency} = {price_in_foreign_currency:.2f} {base_currency}')
            self.price_label.setText(f'1 {base_currency} = {price_in_rub:.4f} {self.currency}')
        else:
            self.label.setText(f'Курс {self.currency} не найден')
            self.price_label.setText('')


class CurrencyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD']

        self.background_images = {
            'USD': 'path_to_eur_image.png',
            'EUR': 'path_to_eur_image.png',
            'GBP': 'path_to_gbp_image.png',
            'JPY': 'path_to_jpy_image.png',
            'AUD': 'path_to_aud_image.png',
        }

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setStyleSheet("background-color: rgba(22,24,33,70);")  # Изменить фон на черный
        self.layout.addWidget(self.stacked_widget)

        self.setMouseTracking(True)
        self.mouse_press_position = None

        for currency in self.currencies:
            background_image = self.background_images[currency]
            page = CurrencyPage(currency, background_image, self)
            self.stacked_widget.addWidget(page)

        self.button_prev = QPushButton("<", self)
        self.button_next = QPushButton(">", self)

        self.button_prev.setFont(QFont('Arial', 20))
        self.button_next.setFont(QFont('Arial', 20))

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button_prev)
        self.button_layout.addWidget(self.button_next)

        self.layout.addLayout(self.button_layout)

        self.button_prev.clicked.connect(self.show_prev_currency)
        self.button_next.clicked.connect(self.show_next_currency)

        self.page_indicator = PageIndicator(len(self.currencies), 0, self)
        self.layout.addWidget(self.page_indicator)

        self.setLayout(self.layout)

        self.update_rates()

    def update_rates(self):
        for index in range(self.stacked_widget.count()):
            page = self.stacked_widget.widget(index)
            page.update_rates()

    def show_prev_currency(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(current_index - 1)
        self.page_indicator.current = self.stacked_widget.currentIndex()
        self.page_indicator.update()  # обновляем отображение индикатора страниц

    def show_next_currency(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index < len(self.currencies) - 1:
            self.stacked_widget.setCurrentIndex(current_index + 1)
        self.page_indicator.current = self.stacked_widget.currentIndex()
        self.page_indicator.update()  # обновляем отображение индикатора страниц

    def resizeEvent(self, event):
        self.page_indicator.update()

    def update_page_indicator(self):
        self.page_indicator.setText(f'Page {self.stacked_widget.currentIndex() + 1} of {self.stacked_widget.count()}')

    def mousePressEvent(self, event):
        self.mouse_press_position = event.position()

    def mouseReleaseEvent(self, event):
        if self.mouse_press_position is not None:
            diff = self.mouse_press_position - event.position()
            if abs(diff.x()) > abs(diff.y()):
                if diff.x() > 0:
                    self.show_next_currency()
                else:
                    self.show_prev_currency()

