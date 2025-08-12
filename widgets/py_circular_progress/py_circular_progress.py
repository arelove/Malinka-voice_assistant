from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import QRectF, Qt, QThread, Signal
from PySide6.QtWidgets import QWidget, QApplication, QDialog, QVBoxLayout, QLabel
import psutil
import sys
import platform
import wmi
from time import sleep


class Worker(QThread):
    data_ready = Signal(float, float)

    def __init__(self, current_zone):
        super(Worker, self).__init__()
        self.current_zone = current_zone

    def run(self):
        while True:
            cpu_percent = psutil.cpu_percent()
            try:
                w = wmi.WMI(namespace='root\\wmi')
                temperature_info = w.query('SELECT * FROM MSAcpi_ThermalZoneTemperature')
                raw_temperature = temperature_info[self.current_zone].CurrentTemperature
                actual_temperature = (raw_temperature - 2732) / 10
                self.current_zone = (self.current_zone + 1) % 2  # переключить зону для следующего вызова
            except Exception as e:
                print(f"Ошибка получения температуры ЦПУ: {e}")
            self.data_ready.emit(cpu_percent, actual_temperature)
            sleep(2)  # обновлять данные каждые 2 секунды


class PyCircularProgress(QWidget):
    def __init__(self,
                 progress_width=5,
                 is_rounded=True,
                 max_value=100,
                 progress_color="#55a0be",
                 enable_text=True,
                 font_family="Peak 5pt",
                 font_size=7,
                 suffix="%",
                 text_color="#ccd7db",
                 enable_bg=True,
                 bg_color="#44475a"):
        super().__init__()

        self.progress_width = progress_width
        self.is_rounded = is_rounded
        self.max_value = max_value
        self.progress_color = progress_color
        self.enable_text = enable_text
        self.font_family = font_family
        self.font_size = font_size
        self.suffix = suffix
        self.text_color = text_color
        self.enable_bg = enable_bg
        self.bg_color = bg_color
        self.value = 0
        self.temperature = 0
        self.cpu_name = "unknown"
        self.current_zone = 0

        self.full_cpu_name = platform.processor()
        self.cpu_name = ' '.join(self.full_cpu_name.split()[0:3])

        self.worker = Worker(self.current_zone)
        self.worker.data_ready.connect(self.update_info)
        self.worker.start()
        # self.mousePressEvent = self.show_cpu_info_popup

    def update_info(self, cpu_percent, temperature):
        self.value = cpu_percent
        self.temperature = temperature
        self.update()

    def paintEvent(self, e):
        width = self.width() - self.progress_width
        height = self.height() - self.progress_width
        margin = self.progress_width / 2
        value = (self.value / self.max_value) * 360

        # Рисование
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(QFont(self.font_family, self.font_size))

        rect = QRectF(margin, margin, width, height)
        pen = QPen()
        pen.setWidth(self.progress_width)

        if self.is_rounded:
            pen.setCapStyle(Qt.RoundCap)

        # Рисовать фон, если требуется
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            painter.setPen(pen)
            painter.drawArc(rect, -90 * 16, -360 * 16)

        # Рисовать прогресс
        pen.setColor(QColor(self.progress_color))
        painter.setPen(pen)
        painter.drawArc(rect, -90 * 16, -value * 16)

        # Рисовать текст, если требуется
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            painter.setPen(pen)
            painter.drawText(rect, Qt.AlignCenter, f"CPU: {self.value:.1f}{self.suffix}")
            painter.setFont(QFont(self.font_family, self.font_size))
            shifted_rect = QRectF(rect.left(), rect.top() + rect.height() * 0.20, rect.width(), rect.height())
            shifted_rect_temp = QRectF(rect.left(), rect.top() + rect.height() * 0.3, rect.width(), rect.height())
            painter.setFont(QFont(self.font_family, self.font_size - 3))
            painter.drawText(shifted_rect_temp,
                             Qt.AlignCenter | Qt.AlignCenter,
                             f"Temp zone {self.current_zone}: {self.temperature}C")

            # переключить зону для следующего вызова
            self.current_zone = (self.current_zone + 1) % 2
            painter.setFont(QFont(self.font_family, self.font_size - 3))
            painter.drawText(shifted_rect, Qt.AlignCenter | Qt.AlignCenter, f"{self.cpu_name}")
    #
    # def setValue(self, value):
    #     self.value = value
    #     self.update()  # Обновляем виджет, чтобы изменения отразились на отображении
    #
    # def setTemperature(self, temperature):
    #     self.temperature = temperature
    #     self.update()  # Обновляем виджет, чтобы изменения отразились на отображении
    #
    # def setCPUName(self, cpu_name):
    #     self.cpu_name = cpu_name
    #     self.update()  # Обновляем виджет, чтобы изменения отразились на отображении
    #
    # def setFontSize(self, font_size):
    #     self.font_size = font_size
    #
    # def copyWidget(self):
    #     # создаем новый экземпляр и копируем значения в него
    #     new_widget = PyCircularProgress()
    #     new_widget.setValue(self.value)
    #     new_widget.setTemperature(self.temperature)
    #     new_widget.setCPUName(self.cpu_name)
    #     new_widget.setFontSize(self.font_size * 3)  # увеличиваем размер шрифта
    #     return new_widget
    #
    # def show_cpu_info_popup(self, event):
    #     # Создайте виджет для затемнения и добавьте его на основной виджет
    #     self.dim_widget = QWidget(self)
    #     self.dim_widget.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
    #     self.dim_widget.resize(self.size())
    #     self.dim_widget.show()
    #
    #     # Затем покажите всплывающее окно
    #     cpu_info = {
    #         "value": self.value,
    #         "temperature": self.temperature,
    #         "cpu_name": self.cpu_name
    #     }
    #     self.popup = CPUInfoPopup(cpu_info, self)
    #     self.popup.show()

#
# class CPUInfoPopup(QDialog):
#     def __init__(self, cpu_info, parent=None):
#         super(CPUInfoPopup, self).__init__(parent, Qt.FramelessWindowHint)
#         self.setModal(True)
#
#         self.layout = QVBoxLayout(self)
#         self.layout.setContentsMargins(0, 0, 0, 0)  # Убираем отступы и границы внутри layout
#
#         # Создаем QLabel для отображения текста
#         self.label = QLabel(self)
#         cpu_text = f"CPU: {cpu_info['value']:.1f}%\nTemp: {cpu_info['temperature']}C\n{cpu_info['cpu_name']}"
#         self.label.setText(cpu_text)
#         self.label.setFont(QFont("Arial", 24))  # Увеличиваем размер шрифта
#         self.layout.addWidget(self.label)
#
#         # Создаем PyCircularProgress для отображения большого круга
#         self.progress = PyCircularProgress(progress_width=20, font_size=20)
#         self.progress.setValue(cpu_info['value'])
#         self.progress.setTemperature(cpu_info['temperature'])
#         self.progress.setCPUName(cpu_info['cpu_name'])
#         self.layout.addWidget(self.progress)
#
#         # Установим размеры диалогового окна
#         self.setFixedSize(400, 400)  # Размеры можно корректировать под свои нужды
#
#     # Переопределение метода, чтобы закрыть окно при клике мышью
#     def mousePressEvent(self, event):
#         self.parent().dim_widget.deleteLater()
#         self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = PyCircularProgress()
    form.show()
    sys.exit(app.exec())
