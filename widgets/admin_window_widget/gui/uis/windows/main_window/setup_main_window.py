from . functions_main_window import *
from widgets.admin_window_widget.qt_core import *
from widgets.admin_window_widget.gui.core.json_settings import Settings
from widgets.admin_window_widget.gui.core.json_themes import Themes
from widgets.admin_window_widget.gui.widgets import *


class SetupMainWindow:
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Главная",
            "btn_tooltip": "Главная",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_add_user.svg",
            "btn_id": "btn_add_user",
            "btn_text": "Добавить пользователя",
            "btn_tooltip": "Добавить пользователя",
            "show_top": True,
            "is_active": False
        },
    ]

    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    def setup_gui(self):
        self.setWindowTitle(self.settings["app_name"])
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("")

        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        settings = Settings()
        self.settings = settings.items

        themes = Themes()
        self.themes = themes.items

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)