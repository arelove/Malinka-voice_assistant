__author__ = 'Ar3love'

from PySide6.QtCore import QThread, QAbstractNativeEventFilter, Qt, QPoint
from cryptography.fernet import Fernet
import psutil
import logging
import ctypes
from ctypes import wintypes
import win32con
import time
from widgets.admin_window_widget.gui.uis.windows.main_window.functions_main_window import *
import sys
import os
from widgets.admin_window_widget.qt_core import *
from widgets.admin_window_widget.gui.core.json_settings import Settings
from widgets.admin_window_widget.gui.uis.windows.main_window import *
from widgets.admin_window_widget.gui.uis.pages.ui_main_pages import Ui_MainPages
import sqlite3
import json

# Загружаем данные из файла
with open('config.json', 'r') as f:
    config = json.load(f)

base_project_dir = config['base_project_dir']
users_bd = config['users_bd']

admin_logs_dir = config['admin_logs']['admin_logs_dir']
assistant_logs_file = config['admin_logs']['assistant_logs_file']
flashdrive_watcher_file = config['admin_logs']['flashdrive_watcher_file']
letter_drive = config['crypto_drive_letter']


os.environ["QT_FONT_DPI"] = "96"

# Это условное имя для окна, которое будет получать сообщения от WinAPI
WND_NAME = u"MyWindow"

# Эти две константы нужны для функции RegisterDeviceNotification
DBT_DEVICEARRIVAL = 0x8000
DBT_DEVICEREMOVECOMPLETE = 0x8004

DBT_DEVTYP_VOLUME = 0x2


# Это структуры, которые используются функцией RegisterDeviceNotification
class DEV_BROADCAST_HDR(ctypes.Structure):
    _fields_ = [
        ("dbch_size", wintypes.DWORD),
        ("dbch_devicetype", wintypes.DWORD),
        ("dbch_reserved", wintypes.DWORD)
    ]


class DEV_BROADCAST_VOLUME(ctypes.Structure):
    _fields_ = [
        ("dbcv_size", wintypes.DWORD),
        ("dbcv_devicetype", wintypes.DWORD),
        ("dbcv_reserved", wintypes.DWORD),
        ("dbcv_unitmask", wintypes.DWORD),
        ("dbcv_flags", wintypes.DWORD)
    ]


# Настройка логгера
logger = logging.getLogger('FlashDriveWatcher')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Лог в файл

flashdrive_watcher_path = os.path.join(admin_logs_dir, flashdrive_watcher_file)
file_handler = logging.FileHandler(flashdrive_watcher_path)  # admin_logs/
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Лог в консоль
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class DeviceEventFilter(QAbstractNativeEventFilter):
    def __init__(self, device_added_callback, device_removed_callback):
        super(DeviceEventFilter, self).__init__()
        self.device_added_callback = device_added_callback
        self.device_removed_callback = device_removed_callback

    def nativeEventFilter(self, eventType, message):
        msg = ctypes.wintypes.MSG.from_address(message.__int__())
        if msg.message == win32con.WM_DEVICECHANGE:
            if msg.wParam == DBT_DEVICEARRIVAL or msg.wParam == DBT_DEVICEREMOVECOMPLETE:
                info = ctypes.cast(msg.lParam, ctypes.POINTER(DEV_BROADCAST_HDR)).contents
                if info.dbch_devicetype == DBT_DEVTYP_VOLUME:
                    volume_info = ctypes.cast(msg.lParam, ctypes.POINTER(DEV_BROADCAST_VOLUME)).contents
                    letter = chr(ord('A') + (volume_info.dbcv_unitmask & -volume_info.dbcv_unitmask).bit_length() - 1)
                    if msg.wParam == DBT_DEVICEARRIVAL:
                        self.device_added_callback(letter)
                    elif msg.wParam == DBT_DEVICEREMOVECOMPLETE:
                        self.device_removed_callback(letter)
        return False, 0


class FlashDriveWatcher(QThread):
    admin_window_signal = Signal()

    def __init__(self, device_added_callback, device_removed_callback):
        QThread.__init__(self)
        self.device_added_callback = device_added_callback
        self.device_removed_callback = device_removed_callback
        self.processed_drives = set()
        self.connected_drives = set()

    def run(self):
        while not self.isInterruptionRequested():
            self.check_existing_flashdrives()
            self.check_for_new_flashdrives()
            time.sleep(1)

    def check_flashdrive(self, drive_letter):
        if drive_letter == letter_drive:
            flashdrive_path = f"{drive_letter}:/"
            if self.is_admin_flashdrive(flashdrive_path):
                # Если флеш-накопитель является административным, генерируем сигнал для отображения админ-панели
                self.admin_window_signal.emit()

    def check_existing_flashdrives(self):
        for disk in psutil.disk_partitions(all=False):
            if 'removable' in disk.opts:
                drive_letter = disk.device[0]
                self.check_flashdrive(drive_letter)

    # Добавление нового метода для проверки новых устройств
    def check_for_new_flashdrives(self):
        new_drives = {disk.device for disk in psutil.disk_partitions(all=False)}
        added_drives = new_drives - self.connected_drives
        removed_drives = self.connected_drives - new_drives
        self.connected_drives = new_drives  # Обновляем список подключенных дисков

        if added_drives:
            for drive in added_drives:
                # Проверяем имя диска
                if "G" in drive:
                    logger.info(f"Обнаружено устройство криптоключа: {drive}")
                    self.device_added_callback(drive[0])  # drive[0] содержит букву диска

        if removed_drives:
            for drive in removed_drives:
                # Проверяем имя диска
                if "G" in drive:
                    logger.info(f"Устройство отключено: {drive}")
                    self.device_removed_callback(drive[0])  # drive[0] содержит букву диска

    def is_admin_flashdrive(self, flashdrive_path):
        key_file_path = os.path.join(flashdrive_path, "admin_key.key")
        if os.path.exists(key_file_path):
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
                try:
                    cipher_suite = Fernet(key)
                    test_data = b"This is a test message."
                    encrypted_data = cipher_suite.encrypt(test_data)
                    decrypted_data = cipher_suite.decrypt(encrypted_data)
                    if decrypted_data == test_data:
                        return True
                    else:
                        logger.warning("Invalid key.")
                except ValueError as e:
                    logger.error("Ошибка чтения ключа: %s", e)
                except Exception as e:
                    # Обрабатываем другие исключения, которые мы не ожидаем
                    logger.error("Неожиданная ошибка: %s", e, exc_info=True)
        else:
            logger.warning("Файл ключа не найден на диске %s", flashdrive_path)
        return False


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.username_change = None
        self.new_password_change = None
        self.ui = UI_MainWindow()
        self.uit = Ui_MainPages()
        self.ui.setup_ui(self)

        # Передаем self в setupUi
        self.uit.setupUi(self)

        settings = Settings()
        self.settings = settings.items

        self.hide_grips = True
        SetupMainWindow.setup_gui(self)

        self.ui.load_pages.Log_admin_button.clicked.connect(self.open_log_file_flash)
        self.ui.load_pages.Log_admin_button_2.clicked.connect(self.open_log_file)
        self.ui.load_pages.Log_admin_button_3.clicked.connect(self.open_log_file)
        self.ui.load_pages.Log_admin_button_4.clicked.connect(self.open_log_file)

        self.ui.load_pages.login_button.clicked.connect(self.admin_save_new_pass)

        self.show()

    def admin_save_new_pass(self):
        # Получите имя пользователя и пароль прямо здесь
        self.username_change = self.ui.load_pages.Login_edit_admin.text()
        self.new_password_change = self.ui.load_pages.Pass_edit_admin.text()

        # Создайте соединение с базой данных
        users_bd_path = os.path.join(base_project_dir, users_bd)
        conn = sqlite3.connect(users_bd_path )
        cursor = conn.cursor()

        # Обновите пароль для данного пользователя
        cursor.execute("""
               UPDATE users
               SET password = ?
               WHERE name = ?
           """, (self.new_password_change, self.username_change))

        # Сохраните изменения и закройте соединение с базой данных
        conn.commit()
        conn.close()

    @Slot()
    def open_log_file(self):
        print("Trying to open log file...")
        try:
            full_path_assistant_logs_file = os.path.join(admin_logs_dir, assistant_logs_file)
            os.startfile(full_path_assistant_logs_file)
            logger.info("Log file opened")
        except Exception as e:
            print("Failed to open log file:", e)
            logger.error("Failed to open log file: " + str(e))

    def open_log_file_flash(self):
        print("Trying to open log file...")
        try:
            full_path_flashdrive_watcher = os.path.join(admin_logs_dir, flashdrive_watcher_file)
            os.startfile(full_path_flashdrive_watcher)
            logger.info("Log file opened")
        except Exception as e:
            print("Failed to open log file:", e)
            logger.error("Failed to open log file: " + str(e))

    def btn_clicked(self):
        btn = SetupMainWindow.setup_btns(self)
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_1)
        if btn.objectName() == "btn_add_user":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
        # if btn.objectName() == "Log_admin_button":
        #     os.startfile("admin_logs/assistant.log")

    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = AdminWindow()
    sys.exit(app.exec())
