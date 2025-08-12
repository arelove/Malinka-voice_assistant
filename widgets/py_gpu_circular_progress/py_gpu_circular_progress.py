from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import QTimer, QRectF, Qt, Signal, QThread
from PySide6.QtWidgets import QWidget, QApplication
import GPUtil
import sys
from time import sleep


class GpuWorker(QThread):
    data_ready = Signal(float, float)

    def __init__(self):
        super(GpuWorker, self).__init__()
        gpus = GPUtil.getGPUs()  # получить информацию о видеокартах
        self.gpu = gpus[0]  # первая видеокарта

    def run(self):
        while True:
            gpus = GPUtil.getGPUs()  # получить информацию о видеокартах внутри цикла
            gpu = gpus[0]  # первая видеокарта
            load = gpu.load * 100
            temperature = gpu.temperature
            self.data_ready.emit(load, temperature)
            sleep(2)


class PyCircularGpuProgress(QWidget):
    def __init__(self,
                 progress_width=5,
                 is_rounded=True,
                 max_value=100,
                 progress_color="#4d0000",
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
        self.gpu_name = "Unknown"  # название
        self.gpu_temp = 0  # температура

        gpus = GPUtil.getGPUs()  # получить информацию о видеокартах
        gpu = gpus[0]  # первая видеокарта

        full_gpu_name = gpu.name  # название
        self.gpu_name = ' '.join(full_gpu_name.split()[2:5])

        self.worker = GpuWorker()
        self.worker.data_ready.connect(self.update_info)
        self.worker.start()

    def update_info(self, load, temperature):
        self.value = load
        self.gpu_temp = temperature
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
            painter.setFont(QFont(self.font_family, self.font_size))
            shifted_rect = QRectF(rect.left(), rect.top() + rect.height() * 0.2, rect.width(), rect.height())
            shifted_rect_temp = QRectF(rect.left(), rect.top() + rect.height() * 0.3, rect.width(), rect.height())
            painter.drawText(rect, Qt.AlignCenter, f"GPU: {self.value:.1f}{self.suffix}")
            painter.setFont(QFont(self.font_family, self.font_size - 3))
            painter.drawText(shifted_rect_temp, Qt.AlignCenter | Qt.AlignCenter, f"Temp: {self.gpu_temp}C")
            painter.setFont(QFont(self.font_family, self.font_size - 3))
            painter.drawText(shifted_rect, Qt.AlignCenter | Qt.AlignCenter, f"{self.gpu_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = PyCircularGpuProgress()
    form.show()
    sys.exit(app.exec())
