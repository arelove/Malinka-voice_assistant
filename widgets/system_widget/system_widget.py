__author__ = 'Ar3love'

import platform
import psutil
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class SystemInfoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        self.os_label = QLabel()
        self.architecture_label = QLabel()
        self.cpu_label = QLabel()
        self.ram_label = QLabel()
        self.disk_label = QLabel()

        self.layout.addWidget(self.os_label)
        self.layout.addWidget(self.architecture_label)
        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.ram_label)
        self.layout.addWidget(self.disk_label)

        self.update_system_info()

    def update_system_info(self):
        self.os_label.setText(f"ОС: {platform.system()} {platform.release()}")
        self.architecture_label.setText(f"Архитектура: {'x64' if platform.machine().endswith('64') else 'x86'}")
        self.cpu_label.setText(f"Процессор: {platform.processor()}")
        self.ram_label.setText(f"RAM: {round(psutil.virtual_memory().total / (1024.0 ** 3))} GB")

        disk_usage = psutil.disk_usage('C://')
        total_disk_space = round(disk_usage.total / (1024.0 ** 3))
        free_disk_space = round(disk_usage.free / (1024.0 ** 3))
        self.disk_label.setText(f"Свободно на диске C: {free_disk_space}/{total_disk_space} GB")
