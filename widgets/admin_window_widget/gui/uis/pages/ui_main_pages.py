from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget, QLineEdit)

from . resources_rc import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(650, 602)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(130, 20, 251, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(30, 0, 211, 31))
        self.frame_7.setStyleSheet(u"background-color: rgba(33, 37, 43, 220);\n"
"border-radius: 15px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 0, 151, 31))
        self.label_3.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 13pt \"Berlin Sans FB Demi\";")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 80, 211, 31))
        self.frame_3.setStyleSheet(u"background-color: rgba(33, 37, 43, 220);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 0, 141, 31))
        self.label_4.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Berlin Sans FB Demi\";")
        self.Log_admin_button = QPushButton(self.frame)
        self.Log_admin_button.setObjectName(u"Log_admin_button")
        self.Log_admin_button.setEnabled(True)
        self.Log_admin_button.setGeometry(QRect(300, 80, 150, 30))
        self.Log_admin_button.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setFamilies([u"Berlin Sans FB Demi"])
        font.setPointSize(10)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.Log_admin_button.setFont(font)
        self.Log_admin_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Log_admin_button.setStyleSheet(u"\n"
"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 10pt \"Berlin Sans FB Demi\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	font: 700 10pt \"Script MT Bold\";\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Log_admin_button.setIcon(icon)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 150, 211, 31))
        self.frame_4.setStyleSheet(u"background-color: rgba(33, 37, 43, 220);\n"
"border-radius: 15px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 0, 191, 31))
        self.label_5.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Berlin Sans FB Demi\";")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 220, 211, 31))
        self.frame_5.setStyleSheet(u"background-color: rgba(33, 37, 43, 220);\n"
"border-radius: 15px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 0, 181, 31))
        self.label_6.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Berlin Sans FB Demi\";")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 290, 211, 31))
        self.frame_6.setStyleSheet(u"background-color: rgba(33, 37, 43, 220);\n"
"border-radius: 15px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 0, 171, 31))
        self.label_7.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Berlin Sans FB Demi\";")
        self.Log_admin_button_2 = QPushButton(self.frame)
        self.Log_admin_button_2.setObjectName(u"Log_admin_button_2")
        self.Log_admin_button_2.setGeometry(QRect(300, 150, 150, 30))
        self.Log_admin_button_2.setMinimumSize(QSize(150, 30))
        self.Log_admin_button_2.setFont(font)
        self.Log_admin_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.Log_admin_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 10pt \"Berlin Sans FB Demi\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	font: 700 10pt \"Script MT Bold\";\n"
"}")
        self.Log_admin_button_2.setIcon(icon)
        self.Log_admin_button_3 = QPushButton(self.frame)
        self.Log_admin_button_3.setObjectName(u"Log_admin_button_3")
        self.Log_admin_button_3.setGeometry(QRect(300, 220, 150, 30))
        self.Log_admin_button_3.setMinimumSize(QSize(150, 30))
        self.Log_admin_button_3.setFont(font)
        self.Log_admin_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.Log_admin_button_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 10pt \"Berlin Sans FB Demi\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	font: 700 10pt \"Script MT Bold\";\n"
"}")
        self.Log_admin_button_3.setIcon(icon)
        self.Log_admin_button_4 = QPushButton(self.frame)
        self.Log_admin_button_4.setObjectName(u"Log_admin_button_4")
        self.Log_admin_button_4.setGeometry(QRect(300, 290, 150, 30))
        self.Log_admin_button_4.setMinimumSize(QSize(150, 30))
        self.Log_admin_button_4.setFont(font)
        self.Log_admin_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.Log_admin_button_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 10pt \"Berlin Sans FB Demi\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	font: 700 10pt \"Script MT Bold\";\n"
"}")
        self.Log_admin_button_4.setIcon(icon)

        self.page_1_layout.addWidget(self.frame)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 630, 582))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_8 = QFrame(self.page_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.Login_edit_admin = QLineEdit(self.frame_8)
        self.Login_edit_admin.setObjectName(u"Login_edit_admin")
        self.Login_edit_admin.setGeometry(QRect(100, 120, 310, 40))
        self.Login_edit_admin.setStyleSheet(u"QLineEdit{\n"
"	min-height: 40px;\n"
"	border-radius: 20px;\n"
"	background-color: #FFFFFF;\n"
"	padding-left: 20px;\n"
"	color: rgb(140, 140, 140);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(139, 142, 139);\n"
"}")
        self.Pass_edit_admin = QLineEdit(self.frame_8)
        self.Pass_edit_admin.setObjectName(u"Pass_edit_admin")
        self.Pass_edit_admin.setGeometry(QRect(100, 170, 310, 40))
        self.Pass_edit_admin.setStyleSheet(u"QLineEdit{\n"
"	min-height: 40px;\n"
"	border-radius: 20px;\n"
"	background-color: #FFFFFF;\n"
"	padding-left: 20px;\n"
"	color: rgb(140, 140, 140);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid rgb(139, 142, 139);\n"
"}")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 80, 331, 20))
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255,255, 255);\n"
"}\n"
"font: 700 12pt \"Script MT Bold\";")
        self.login_button = QPushButton(self.frame_8)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(100, 250, 310, 45))
        self.login_button.setStyleSheet(u"\n"
"QPushButton#login_button{\n"
"	min-height: 45px;\n"
"	border-radius: 20px;\n"
"	background-color: #FF7F50;\n"
"	color: #FFFFFF;\n"
"	font: 700 10pt \"Script MT Bold\";\n"
"}\n"
"\n"
"QPushButton#login_button:hover{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	font: 700 10pt \"Script MT Bold\";\n"
"}")

        self.horizontalLayout.addWidget(self.frame_8)


        self.page_3_layout.addLayout(self.horizontalLayout)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u041b\u043e\u0433\u043e\u0432", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"\u0410\u0434\u043c\u0438\u043d \u043f\u0430\u043d\u0435\u043b\u044c", None))
        self.Log_admin_button.setText(QCoreApplication.translate("MainPages", u" \u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u043e\u0439 \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"\u041f\u043e\u043f\u044b\u0442\u043a\u0438 \u0430\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u0437\u0430\u043f\u0443\u0441\u043a\u043e\u0432", None))
        self.Log_admin_button_2.setText(QCoreApplication.translate("MainPages", u" \u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.Log_admin_button_3.setText(QCoreApplication.translate("MainPages", u" \u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.Log_admin_button_4.setText(QCoreApplication.translate("MainPages", u" \u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.Login_edit_admin.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.Pass_edit_admin.setPlaceholderText(QCoreApplication.translate("MainPages", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"\u0421\u043c\u0435\u043d\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0433\u043e \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.login_button.setText(QCoreApplication.translate("MainPages", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

