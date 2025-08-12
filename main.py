from modules import *
from widgets import *
from ui_splash_screen import Ui_SplashScreen
from voice_assistant.assistent_widget import ToggleWidget
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QPlainTextEdit,
                               QSystemTrayIcon, QMessageBox, QSizePolicy)
from PySide6 import QtCharts
from PySide6.QtGui import QPainter
from PySide6 import QtCore
from PySide6.QtCore import Qt
import sqlite3
import pyotp
import pyqrcode
from login import Ui_Login
import pickle
import sys
import time
import threading
import logging
import os
import csv
import json

# Загружаем данные из файла
with open('config.json', 'r') as f:
    config = json.load(f)

base_project_dir = config['base_project_dir']
users_bd = config['users_bd']
user_data = config['user_data_pcl']
config_voice_data = config['config_voice']

os.environ["QT_FONT_DPI"] = "96"

widgets = None
counter = 0
jumper = 0


class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.appendHtml(f"<p style='line-height:20px;'>{text}</p>")


class LoginUI(QMainWindow, Ui_Login):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.main_win = None
        self.username = None  # Добавьте эту строку

        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.close_button.clicked.connect(self.close)
        self.minimize_button.clicked.connect(self.minimize)

        self.create_database()
        self.layout = QVBoxLayout()
        self.login_button.clicked.connect(self.check_password)
        self.forgot_button.clicked.connect(self.forgot_password)
        self.lineEdit_OTP.hide()

        # Создаем кнопки для переключения языка
        self.language = 'en'

        # Создаем кнопки для переключения языка
        self.btn_en = QPushButton('EN', self)
        self.btn_ru = QPushButton('RU', self)
        self.btn_en.clicked.connect(self.switch_to_en)
        self.btn_ru.clicked.connect(self.switch_to_ru)

        # Размещаем кнопки в правом нижнем углу
        self.btn_en.setGeometry(self.width() - 60, self.height() - 30, 30, 30)
        self.btn_ru.setGeometry(self.width() - 30, self.height() - 30, 30, 30)

    def resizeEvent(self, event):
        # Переопределяем обработчик события изменения размера окна,
        # чтобы переместить кнопки при изменении размера
        self.btn_en.setGeometry(self.width() - 60, self.height() - 30, 30, 30)
        self.btn_ru.setGeometry(self.width() - 30, self.height() - 30, 30, 30)
        super().resizeEvent(event)

    def switch_to_en(self):
        # Переключение на английский язык
        self.language = 'en'
        self.forgot_button.setText('Forgot Password')
        self.login_button.setText('Sign In')

        font = self.sign_label.font()
        font.setPointSize(20)  # Можно установить нужный вам размер шрифта
        self.sign_label.setFont(font)
        self.sign_label.setText('Sign In')

        self.lineEdit_Login.setPlaceholderText('Username')
        self.lineEdit_Password.setPlaceholderText('Password')
        self.lineEdit_OTP.setPlaceholderText('OTP')
        self.checkBox.setText('Remember me')

    def switch_to_ru(self):
        # Переключение на русский язык
        self.language = 'ru'
        self.forgot_button.setText('Забыли пароль')
        self.login_button.setText('Войти')

        font = self.sign_label.font()
        font.setPointSize(20)  # Можно установить нужный вам размер шрифта
        self.sign_label.setFont(font)
        self.sign_label.setText('Войти в систему')

        self.lineEdit_Login.setPlaceholderText('Имя пользователя')
        self.lineEdit_Password.setPlaceholderText('Пароль')
        self.lineEdit_OTP.setPlaceholderText('OTP')
        self.checkBox.setText('Запомнить меня')

    def close(self):
        return super().close()

    def minimize(self):
        self.showMinimized()

    def create_database(self):
        conn = sqlite3.connect(users_bd)  # Это создаст файл базы данных, если его еще нет
        cursor = conn.cursor()

        # Создаем таблицу, если она еще не существует
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                password TEXT,
                secret_word TEXT,
                otp_secret TEXT,
                first_name TEXT DEFAULT '',  
                last_name TEXT DEFAULT '',
                avatar_path TEXT DEFAULT 'images/images/avatar_def.png',
                email TEXT DEFAULT '',
                phone TEXT DEFAULT '',
                date_of_birth TEXT DEFAULT '',
                position TEXT DEFAULT '',
                salary REAL DEFAULT 0.0  
            )
        """)

        conn.commit()
        conn.close()

    def forgot_password(self):
        if self.language == 'en':
            if self.forgot_button.text() == 'Forgot Password':
                self.lineEdit_Password.hide()
                self.lineEdit_OTP.show()
                self.forgot_button.setText('Sign In')
            else:
                self.lineEdit_Password.show()
                self.lineEdit_OTP.hide()
                self.forgot_button.setText('Forgot Password')
        elif self.language == 'ru':
            if self.forgot_button.text() == 'Забыли пароль':
                self.lineEdit_Password.hide()
                self.lineEdit_OTP.show()
                self.forgot_button.setText('Войти')
            else:
                self.lineEdit_Password.show()
                self.lineEdit_OTP.hide()
                self.forgot_button.setText('Забыли пароль')

    def check_password(self):
        name = self.lineEdit_Login.text()
        password = self.lineEdit_Password.text()
        otp = self.lineEdit_OTP.text()

        conn = sqlite3.connect(users_bd)
        cursor = conn.cursor()
        cursor.execute("SELECT password, otp_secret FROM users WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()

        if result is None:
            QMessageBox.warning(self, "Ошибка входа", "Неправильное имя пользователя или OTP. Попробуйте еще раз.")
            self.lineEdit_Password.clear()
            self.lineEdit_OTP.clear()
            return

        db_password, otp_secret = result

        if otp_secret is None and (password and password == db_password):
            print(self, "Ошибка OTP", "У этого пользователя нет секрета OTP. Пожалуйста, обратитесь к администратору.")
            if self.checkBox.isChecked():  # Если флажок "Remember me" установлен
                # Сохраняем имя пользователя и время входа
                with open(user_data, 'wb') as f:
                    pickle.dump((name, time.time()), f)
            self.main_win = MainWindow(name)
            self.main_win.show()
            self.close()
            return

        totp = pyotp.TOTP(otp_secret)
        if totp.verify(otp) or (password and password == db_password):
            if self.checkBox.isChecked():  # Если флажок "Remember me" установлен
                # Сохраняем имя пользователя и время входа
                with open(user_data, 'wb') as f:
                    pickle.dump((name, time.time()), f)
            self.main_win = MainWindow(name)
            self.main_win.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка входа", "Неправильный OTP или пароль. Попробуйте еще раз.")
            self.lineEdit_Password.clear()
            self.lineEdit_OTP.clear()


class SplashScreen(QMainWindow):
    spla_time = time.time()

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.progressBarValue(0)

        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground)  # Set background to transparent

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        self.show()
    spla_time_end = time.time()
    logging.info(f"splash : {spla_time_end - spla_time}")

    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 1

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            self.login = MainWindow(username)
            self.login.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


class MainWindow(QMainWindow):
    def __init__(self, username):
        QMainWindow.__init__(self)
        if QSystemTrayIcon.isSystemTrayAvailable():
            self.tray_icon = QSystemTrayIcon(self.style().standardIcon(QStyle.SP_ComputerIcon), self)
            self.tray_icon.setVisible(True)
        else:
            print("Системные уведомления не поддерживаются.")

        self.username = username
        self.assistant = ToggleWidget()
        self.db_manager = DatabaseManager(users_bd)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.donut = NestedDonut()
        # self.donut_dash = NestedDonutDash()
        # Создаем виджет статистики
        self.stats_widget = StatsWidget()
        self.ui.pushButton_5.clicked.connect(self.stats_widget.button_clicked)
        self.system_info_widget = SystemInfoWidget()
        self.ui.configure_pc_layout.addWidget(self.system_info_widget)

        global widgets
        widgets = self.ui

        self.ui.radioButton_5.toggled.connect(self.on_tts_model_toggled)
        self.ui.radioButton_6.toggled.connect(self.on_tts_model_toggled)

        self.accentizer_enabled = False
        self.accentizer = None

        self.ui.AccentizerRadioButton.clicked.connect(self.toggle_accentizer)

        self.load_config()
        # Создаем экземпляр QPlainTextEdit для вывода текста ассистента
        self.console_output_widget = QPlainTextEdit()

        # Создаем кнопку для очистки текста
        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.console_output_widget.clear)

        # Создаем QVBoxLayout для console_output_widget и clear_button
        vbox = QVBoxLayout()
        vbox.addWidget(self.console_output_widget)
        vbox.addWidget(self.clear_button)

        reminderWidget = RemindersWidget()  # Your RemindersWidget instance
        # Adding reminderWidget to horizontalLayout_7
        self.ui.horizontalLayout_7.addWidget(reminderWidget)

        # Создаем виджет, который будет содержать наш QVBoxLayout
        widget = QWidget()
        widget.setLayout(vbox)

        # Добавляем виджет в существующий макет console_dialogue_layout
        self.ui.console_dialogue_layout.addWidget(widget)

        self.layout = QVBoxLayout()
        self.horizontalLayout_6 = QHBoxLayout()
        self.layout.addLayout(self.horizontalLayout_6)

        conn = sqlite3.connect(users_bd)
        cursor = conn.cursor()

        # Проверяем, существует ли уже секрет OTP для этого пользователя
        cursor.execute("SELECT otp_secret FROM users WHERE name = ?", (self.username,))
        result = cursor.fetchone()

        if result is None:
            # Если секрета OTP нет, генерируем новый и сохраняем его в базе данных
            self.otp_secret = pyotp.random_base32()
            cursor.execute("""
                UPDATE users 
                SET otp_secret=?
                WHERE name=?
            """, (self.otp_secret, self.username))
            conn.commit()
        else:
            # Если секрет OTP уже существует, используем его
            self.otp_secret = result[0]

        conn.close()

        # Генерируем QR код
        totp = pyotp.TOTP(self.otp_secret)
        url = totp.provisioning_uri(self.username, issuer_name="Voice Assistant")
        img = pyqrcode.create(url)
        img.png('qrcode.png', scale=4)

        # Устанавливаем изображение QR кода
        self.qr_label = QLabel()
        self.qr_label.setPixmap(QPixmap('qrcode.png'))
        self.ui.horizontalLayout_6.addWidget(self.qr_label)
        self.setLayout(self.layout)

        # Объявляем и подключаем OutputRedirector к нашему виджету console_output_widget
        self.redirector = OutputRedirector(self.console_output_widget)
        sys.stdout = self.redirector

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PY3LOVE"
        description = "Voice Assistant"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # # QTableWidget PARAMETERS
        # # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        # widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////

        self.updateButton = QPushButton("Обновить график")
        self.updateButton.setIcon(QIcon('images/images/refresh.png'))  # Указываем путь к изображению
        self.updateButton.setIconSize(QSize(10, 10))  # Задаем размер иконки
        self.updateButton.setStyleSheet("background-color: transparent; border: none; font-size: 12px; min-height: 15px;")  # Стилизуем кнопку
        self.updateButton.clicked.connect(self.update_chart)  # Обновляем график при нажатии на кнопку

        # Создаем горизонтальный layout для кнопки
        button_layout = QHBoxLayout()
        # Добавляем пустое пространство слева от кнопки
        button_layout.addStretch()
        # Добавляем кнопку
        button_layout.addWidget(self.updateButton)
        # Добавляем пустое пространство справа от кнопки
        button_layout.addStretch()

        # Добавляем layout с кнопкой в вертикальный layout
        self.ui.bar_charts_cont.addLayout(button_layout)
        self.setLayout(self.ui.bar_charts_cont)
        self.create_bar_graph()

        progress_widget = PyCircularProgress()  # Пример инициализации
        self.ui.cpu_progress_bar.addWidget(progress_widget)

        gpu_widget = PyCircularGpuProgress()
        self.ui.gpu_progress_bar.addWidget(gpu_widget)

        avatar_widget = MainCircleWidget(username)
        self.ui.avatar_layout.addWidget(avatar_widget)

        to_do = ToDoLister()
        self.ui.to_do_list_layout.addWidget(to_do)

        self.currency_widget = CurrencyWidget()  # создаём экземпляр виджета
        self.ui.currency_widget_layout.addWidget(self.currency_widget)

        weather_widget = WeatherWidget()  # создаем экземпляр вашего виджета погоды
        self.ui.weather_layout.addWidget(weather_widget)  # добавляем виджет погоды в макет

        self.qr_label.mousePressEvent = self.show_qr_popup  # Привязываем функцию к событию нажатия мыши
        self.ui.frame_3.mousePressEvent = self.show_employee_info_popup

        self.ui.Current_settings_layout.addWidget(CurrentSettingsLayout())

        # зп и тд
        # Предполагаемые данные
        earnings = 1394600
        formatted_earnings = '{:,}'.format(earnings).replace(',', ' ')
        sales = 68
        approx_salary = earnings * 0.05 + sales * 250

        # Добавление меток в макет
        self.ui.label_2.setText(f"Заработок: {formatted_earnings} ₽")
        self.ui.label_4.setText(f"Количество продаж: {sales}")
        self.ui.label_5.setText(f"Примерная зарплата: {approx_salary} ₽")

        self.ui.pushButton_5.clicked.connect(self.assistant.toggle_function)
        self.show()

        self.ui.pushButton_2.clicked.connect(self.save_config)

        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        # фильтр для нативных событий и установите его для приложения
        self.flashdrive_watcher = FlashDriveWatcher(self.on_device_added, self.on_device_removed)
        self.flashdrive_watcher.admin_window_signal.connect(self.show_admin_window)  # Подключение сигнала к слоту
        self.flashdrive_watcher.start()

        # Запускаем функцию print_login_time через 2 секунды
        timer = threading.Timer(2, self.print_login_time)
        timer.start()

        # Добавляем его в layout
        self.ui.use_stat_layout.addWidget(self.stats_widget)

        self.ui.pie_graph_layout.addWidget(self.donut)
        # self.ui.donut_layout_dash.addWidget(self.donut_dash)
        self.ui.Button_save_password.clicked.connect(self.save_password)

    def save_password(self):

        new_password = self.ui.lineEdit_NewPass.text()
        current_password = self.ui.lineEdit_CurrentPass.text()
        confirm_password = self.ui.lineEdit_NewPassConfirm.text()

        if self.db_manager.get_password(self.username) != current_password:
            QMessageBox.warning(self, "Ошибка", "Текущий пароль неверный")
        elif new_password != confirm_password:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают")
        else:
            self.db_manager.update_password(self.username, new_password)

    def closeEvent(self, event):
        self.db_manager.close()
        super().closeEvent(event)

    def print_login_time(self):
        with open(user_data, 'rb') as f:
            username, login_time = pickle.load(f)
            print(f"Имя пользователя: {username}")
            login_time_struct = time.localtime(login_time)
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", login_time_struct)
            print(f"Время начала сессии: {formatted_time}")
            current_time = time.time()
            elapsed_time = current_time - login_time  # время с начала сессии, в секундах
            remaining_time = 8 * 60 * 60 - elapsed_time  # время до окончания сессии, в секундах

            elapsed_hours, elapsed_remainder = divmod(elapsed_time, 3600)
            elapsed_minutes, elapsed_seconds = divmod(elapsed_remainder, 60)
            print(f"Время использования: {int(elapsed_hours)}:{int(elapsed_minutes)}:{int(elapsed_seconds)}")

            remaining_hours, remaining_remainder = divmod(remaining_time, 3600)
            remaining_minutes, remaining_seconds = divmod(remaining_remainder, 60)
            print(f"До конца сессии: {int(remaining_hours)}:{int(remaining_minutes)}:{int(remaining_seconds)}")

    def on_device_added(self, drive_letter):
        self.notify_user(f"Криптоключ {drive_letter} был подключен.")

    def on_device_removed(self, drive_letter):
        self.notify_user(f"Криптоключ {drive_letter} был отключен.")

    def notify_user(self, message):
        if hasattr(self, 'tray_icon'):
            self.tray_icon.showMessage("Уведомление", message, QSystemTrayIcon.Information, 5000)

    def start_flashdrive_watcher(self):
        if not self.is_running:
            try:
                self.flashdrive_watcher.admin_window_signal.disconnect()
                self.flashdrive_watcher.finished.disconnect()
            except RuntimeError:
                pass  # Игнорируем исключение RuntimeError, которое возникает, если сигнал не был подключен
            self.flashdrive_watcher.admin_window_signal.connect(self.show_admin_window)
            self.flashdrive_watcher.finished.connect(self.on_flashdrive_watcher_finished)
            self.flashdrive_watcher.start()
            self.is_running = True
        else:
            self.notify_user("FlashDriveWatcher уже запущен.")

    def on_flashdrive_watcher_finished(self):
        if self.is_running:
            # Отсоединяем сигналы от слотов
            self.flashdrive_watcher.admin_window_signal.disconnect(self.show_admin_window)
            self.flashdrive_watcher.finished.disconnect(self.on_flashdrive_watcher_finished)
            self.flashdrive_watcher = None
            self.is_running = False

    def show_admin_window(self):
        # Отображение окна администратора без проверки наличия флеш-накопителя
        if not hasattr(self, 'admin_window') or self.admin_window is None:
            self.admin_window = AdminWindow()  # Создаем экземпляр вашего кастомизированного окна
            self.admin_window.setWindowTitle("Окно администратора")
            self.admin_window.show()  # Отображаем окно
        else:
            self.admin_window.raise_()  # Поднимаем окно наверх, если оно уже открыто

    def on_admin_window_closed(self):
        if self.is_running and self.flashdrive_watcher is not None:
            # Останавливаем поток безопасным способом
            self.flashdrive_watcher.quit()
            self.flashdrive_watcher.wait()  # Дожидаемся завершения потока
            # Остальной код по очистке и завершению потока
            self.is_running = False
        # Устанавливаем self.admin_window в None, когда окно закрывается
        self.admin_window = None
        
    def on_tts_model_toggled(self):
        if self.ui.radioButton_2.isChecked():  # Если выбрана модель silero
            self.ui.radioButton_5.setDisabled(False)
            self.ui.radioButton_3.setDisabled(False)
        if self.ui.radioButton_3.isChecked():
            self.ui.radioButton_5.setDisabled(False)
            self.ui.radioButton_2.setDisabled(False)

    def toggle_accentizer(self):
        self.accentizer_enabled = not self.accentizer_enabled

    def load_config(self):
        config = {}
        with open(config_voice_data, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    config[row[0]] = row[1]

        self.speaker = config.get('speaker', 'baya')
        self.model = config.get('tts_model', 'silero')
        self.accentizer_enabled = config.get('accentizer_enabled', '1') == '1'

        if self.speaker == 'baya':
            self.ui.radioButton_2.setChecked(True)

        if self.speaker == 'kseniya':
            self.ui.radioButton_3.setChecked(True)

        if self.model == 'silero':
            self.ui.radioButton_5.setChecked(True)

        if self.model == 'gtts':
            self.ui.radioButton_6.setChecked(True)

        if self.model == 'tera_tts':
            self.ui.radioButton_7.setChecked(True)

        if self.model == 'TeraGirl':
            self.ui.radioButton_8.setChecked(True)

        if self.accentizer == '1':
            self.ui.AccentizerRadioButton.setChecked(True)
        else:
            self.ui.AccentizerRadioButton.setChecked(False)

    def save_config(self):
        if self.ui.radioButton_2.isChecked():
            self.speaker = 'baya'

        if self.ui.radioButton_3.isChecked():
            self.speaker = 'kseniya'

        if self.ui.radioButton_3.isChecked():
            self.speaker = 'gtts'

        if self.ui.radioButton_5.isChecked():
            self.model = 'silero'

        if self.ui.radioButton_6.isChecked():
            self.model = 'gtts'

        if self.ui.radioButton_7.isChecked():
            self.model = 'tera_tts'

        if self.ui.radioButton_8.isChecked():
            self.speaker = "TeraGirl"

        accentizer_state = str(int(self.accentizer_enabled))

        config = [['speaker', self.speaker], ['tts_model', self.model], ['accentizer_enabled', accentizer_state]]

        with open(config_voice_data, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(config)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Для применения всех настроек необходимо перезапустить программу.")
        # msg.setWindowTitle("Сохранено")
        msg.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)

        reply = msg.exec()

        if reply == QMessageBox.StandardButton.Yes:
            msg.setWindowTitle("Сохранено")

    # def restart_program(self):
    #     """Перезапускает текущее приложение."""
    #     try:
    #         # Создаем временный батч-файл для перезапуска приложения
    #         restart_script = "restart_script.bat"
    #         with open(restart_script, "w") as bat_file:
    #             bat_file.write("timeout /t 5\n")
    #             bat_file.write('start "" "{}" {}\n'.format(sys.executable, " ".join(f'"{arg}"' for arg in sys.argv)))
    #             bat_file.write("del \"%~f0\" & exit")  # Команда для удаления батч-файла после выполнения
    #
    #         # Выполняем батч-файл
    #         subprocess.Popen(restart_script, shell=True)
    #
    #         # Завершаем текущее приложение
    #         QApplication.quit()
    #
    #     except Exception as e:
    #         QMessageBox.critical(None, "Ошибка перезапуска", str(e))

    def show_employee_info_popup(self, event):
        # Создайте виджет для затемнения и добавьте его на основной виджет
        self.dim_widget = QWidget(self)
        self.dim_widget.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.dim_widget.resize(self.size())
        self.dim_widget.show()

        # Затем покажите всплывающее окно с информацией о сотруднике
        self.popup = EmployeeInfoPopup(self, self.username)
        self.popup.show()

    def show_qr_popup(self, event):
        # Создайте виджет для затемнения и добавьте его на основной виджет
        self.dim_widget = QWidget(self)
        self.dim_widget.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.dim_widget.resize(self.size())
        self.dim_widget.show()

        # Затем покажите всплывающее окно
        self.popup = QRCodePopup('qrcode.png', self)
        self.popup.show()

    def update_chart(self):
        # Обновление графика
        self.ui.bar_charts_cont.removeWidget(self.chartView)
        self.chartView.deleteLater()

        # Создание нового графика
        self.create_bar_graph()

        # Добавление нового графика в контейнер виджета
        self.ui.bar_charts_cont.addWidget(self.chartView)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

    def create_bar_graph(self):
        yearList = {}
        wealth = {}

        rowCount = 0

        with open('unique_csv/sells.csv', encoding='utf-8') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',')
            for row in csvReader:

                if rowCount > 0:
                    if row:
                        if not row[2] in yearList:
                            yearList[row[2]] = []
                            yearList[row[2]].append({"name": row[0], "wealth": row[4]})

                        else:
                            yearList[row[2]].append({"name": row[0], "wealth": row[4]})

                rowCount += 1

        nameList = []
        for x in yearList:
            for z in yearList[x]:
                if not z["name"] in nameList:
                    nameList.append(z["name"])
                if not z["name"] in wealth:
                    wealth[z["name"]] = []
                    wealth[z["name"]].append(float(z["wealth"]))
                else:
                    wealth[z["name"]].append(float(z["wealth"]))
        self.barSeries = QtCharts.QBarSeries()

        for x in nameList:
            setattr(self, "set" + str(x), QtCharts.QBarSet(str(x)))
            self.barSeries.append(getattr(self, "set" + str(x)))

            getattr(self, "set" + str(x)).append(wealth[x])
            self.barSeries.append(getattr(self, "set" + str(x)))

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.barSeries)
        self.chart.setTitle("График Продаж")

        self.categories = yearList
        self.axisX = QtCharts.QBarCategoryAxis()
        self.axisX.append(self.categories)
        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom)

        self.axisY = QtCharts.QValueAxis()
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)

        self.barSeries.attachAxis(self.axisX)
        self.barSeries.attachAxis(self.axisY)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QtCharts.QChartView(self.chart)

        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.chartView.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.chartView.sizePolicy().hasHeightForWidth())

        self.chartView.setSizePolicy(sizePolicy)
        self.chartView.setMinimumSize(QSize(0, 300))

        self.ui.bar_charts_cont.addWidget(self.chartView)


class QRCodePopup(QDialog):
    def __init__(self, qr_image_path, parent=None):
        super(QRCodePopup, self).__init__(parent, QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('QR Code')
        self.setModal(True)
        self.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('qrcode.png')
        self.label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))  # Увеличиваем изображение
        self.layout.addWidget(self.label)

    # Переопределяем метод, чтобы закрыть окно при клике мышью
    def mousePressEvent(self, event):
        # Удалите виджет для затемнения
        self.parent().dim_widget.deleteLater()

        # Затем закройте всплывающее окно
        self.close()


class EmployeeInfoPopup(QDialog):
    def __init__(self, parent=None, username=None):
        super(EmployeeInfoPopup, self).__init__(parent, Qt.FramelessWindowHint)
        self.username = username

        self.setObjectName(u"EmployeeInfoPopup")  # Установите objectName для QDialog
        self.setWindowTitle('Employee Info')
        self.setModal(True)
        self.resize(400, 600)
        user_info = self.get_user_info()

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")  # Установите objectName для centralwidget
        self.layout = QVBoxLayout(self.centralwidget)

        self.first_name_edit = QLineEdit(user_info['first_name'])
        self.first_name_edit.setPlaceholderText("First Name")

        self.last_name_edit = QLineEdit(user_info['last_name'])
        self.last_name_edit.setPlaceholderText("Last Name")

        self.email_edit = QLineEdit(user_info['email'])
        self.email_edit.setPlaceholderText("Email")

        self.phone_edit = QLineEdit(user_info['phone'])
        self.phone_edit.setPlaceholderText("Phone")

        self.position_edit = QLineEdit(user_info['position'])
        self.position_edit.setPlaceholderText("Position")

        self.salary_edit = QLineEdit(str(user_info['salary']))
        self.salary_edit.setPlaceholderText("Salary")

        self.layout.addWidget(QLabel("Name:"))
        self.layout.addWidget(self.first_name_edit)
        self.layout.addWidget(QLabel("Surname:"))
        self.layout.addWidget(self.last_name_edit)
        self.layout.addWidget(QLabel("Email:"))
        self.layout.addWidget(self.email_edit)
        self.layout.addWidget(QLabel("Phone:"))
        self.layout.addWidget(self.phone_edit)
        self.layout.addWidget(QLabel("Position:"))
        self.layout.addWidget(self.position_edit)
        self.layout.addWidget(QLabel("Salary:"))
        self.layout.addWidget(self.salary_edit)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_changes)

        self.layout.addWidget(save_button)
        self.setLayout(self.layout)

        self.setStyleSheet("""
        QDialog#EmployeeInfoPopup {
            background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.023, stop:0 rgba(85, 80, 190, 255), stop:1 rgba(74, 202, 255, 255));
            border-radius: 40px;
        }
        QLineEdit {
            min-height: 40px;
            border-radius: 20px;
            background-color: #FFFFFF;
            padding-left: 20px;
            color: rgb(140, 140, 140);
        }
        QLineEdit:hover {
            border: 2px solid rgb(139, 142, 139);
        }
        QPushButton {
            min-height: 45px;
            border-radius: 20px;
            background-color: rgb(70, 90, 190);
            color: #FFFFFF;
        }
        QPushButton:hover {
            border: 2px solid rgb(255, 255, 255);
        }
        QLabel {
            color: rgb(255, 255, 255);
        }
        """)

    def get_user_info(self):
        conn = sqlite3.connect(users_bd)
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, email, phone, position, salary FROM users WHERE name=?", (self.username,))
        user_info = cursor.fetchone()
        conn.close()

        if user_info is None:
            return {
                'first_name': '',
                'last_name': '',
                'email': '',
                'phone': '',
                'position': '',
                'salary': ''  # Для зарплаты используем пустую строку
            }

        return {
            'first_name': user_info[0],
            'last_name': user_info[1],
            'email': user_info[2],
            'phone': user_info[3],
            'position': user_info[4],
            'salary': user_info[5]
        }

    def save_changes(self):
        print("Saving changes...")
        print(f"New info: {self.first_name_edit.text()}, {self.last_name_edit.text()}, {self.email_edit.text()}, {self.phone_edit.text()}, {self.position_edit.text()}, {self.salary_edit.text()}")
        print(f"Username: {self.username}")

        try:  # Добавим эту строку
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()

            # Обновить данные пользователя
            cursor.execute("""
                UPDATE users 
                SET first_name=?, last_name=?, email=?, phone=?, position=?, salary=?
                WHERE name=?
            """, (
                self.first_name_edit.text(),
                self.last_name_edit.text(),
                self.email_edit.text(),
                self.phone_edit.text(),
                self.position_edit.text(),
                float(self.salary_edit.text()),
                self.username
            ))

            conn.commit()
            conn.close()
        except Exception as e:  # Добавим этот блок
            print(f"Error updating database: {e}")

        self.parent().dim_widget.deleteLater()
        self.close()

    def mousePressEvent(self, event):
        self.parent().dim_widget.deleteLater()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Проверяем, сохранено ли имя пользователя
    try:
        with open(user_data, 'rb') as f:
            username, login_time = pickle.load(f)
            # Если с момента входа прошло более 8 часов, требуем повторного входа
            if time.time() - login_time > 8 * 60 * 60:  # 8 часов
                raise FileNotFoundError
            window = SplashScreen()
    except FileNotFoundError:
        window = LoginUI()
    window.show()
    sys.exit(app.exec())




