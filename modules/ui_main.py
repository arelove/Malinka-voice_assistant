# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1816, 1016)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1816, 1016))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.64, fx:0.5, fy:0.5, stop:0.0681818 rgba(49, 37, 117, 216), stop:0.528409 rgba(133, 151, 179, 246), stop:1 rgba(28, 17, 62, 255));\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////"
                        "////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(162, 94, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    "
                        "background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(162, 94, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(162, 94, 0);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* ////////////////////////////"
                        "/////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(162, 94, 0)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(162, 94, 0); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(133, 70, 0); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
" "
                        "   background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(162, 94, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px;"
                        " }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(162, 94, 0); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(162, 94, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
""
                        "QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(162, 94, 0);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
""
                        "    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8p"
                        "x;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(162, 94, 0);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-b"
                        "ottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(162, 94, 0);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-lef"
                        "t-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////////////////"
                        "///////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-to"
                        "p-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(162, 94, 0);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);"
                        "\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(162, 94, 0);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb"
                        "(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.gridLayout_3 = QGridLayout(self.styleSheet)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy1.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy1)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy1.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy1)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Peak 5pt"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 9pt \"Peak 5pt\";")
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tetris_button = QPushButton(self.rightButtons)
        self.tetris_button.setObjectName(u"tetris_button")
        self.tetris_button.setMinimumSize(QSize(28, 28))
        self.tetris_button.setMaximumSize(QSize(28, 28))
        self.tetris_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"images/icons/tetris1_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tetris_button.setIcon(icon1)
        self.tetris_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.tetris_button)

        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"\n"
"background-repeat: no-repeat;")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 751, 721))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(40, 120, 321, 211))
        self.frame_24.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"border-radius: 10px")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_24)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 321, 211))
        self.avatar_earning_layout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.avatar_earning_layout.setObjectName(u"avatar_earning_layout")
        self.avatar_earning_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.horizontalLayoutWidget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_25 = QFrame(self.frame_3)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(10, 10, 251, 71))
        self.frame_25.setStyleSheet(u" background: rgba(45, 45, 73, 190);\n"
"font: 12pt \"Courier New\";")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_3 = QWidget(self.frame_25)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 251, 71))
        self.avatar_layout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.avatar_layout.setObjectName(u"avatar_layout")
        self.avatar_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_6 = QWidget(self.frame_3)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 100, 301, 91))
        self.earning_layout_inside = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.earning_layout_inside.setObjectName(u"earning_layout_inside")
        self.earning_layout_inside.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.horizontalLayoutWidget_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 281, 16))
        self.label_2.setStyleSheet(u"font: 10pt \"Courier New\";")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 281, 16))
        self.label_4.setStyleSheet(u"font: 10pt \"Courier New\";")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 50, 281, 16))
        self.label_5.setStyleSheet(u"font: 10pt \"Courier New\";")

        self.earning_layout_inside.addWidget(self.frame_5)


        self.avatar_earning_layout.addWidget(self.frame_3)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(400, 120, 321, 211))
        self.frame_14.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px;\n"
"background-image: url(images/images/dollar_bg);")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_5 = QWidget(self.frame_14)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 321, 211))
        self.currency_widget_layout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.currency_widget_layout.setObjectName(u"currency_widget_layout")
        self.currency_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 40, 291, 41))
        self.label_3.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"font: 20pt \"Peak 5pt\";\n"
"color: rgb(255, 255, 255);")
        self.frame_21 = QFrame(self.frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(40, 360, 681, 341))
        self.frame_21.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.bar_charts = QStackedWidget(self.frame_21)
        self.bar_charts.setObjectName(u"bar_charts")
        self.bar_charts.setGeometry(QRect(0, 0, 681, 341))
        self.bar_charts_conta = QWidget()
        self.bar_charts_conta.setObjectName(u"bar_charts_conta")
        self.bar_charts_conta.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayoutWidget = QWidget(self.bar_charts_conta)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 681, 341))
        self.bar_charts_cont = QVBoxLayout(self.verticalLayoutWidget)
        self.bar_charts_cont.setObjectName(u"bar_charts_cont")
        self.bar_charts_cont.setContentsMargins(0, 0, 0, 0)
        self.bar_charts.addWidget(self.bar_charts_conta)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.bar_charts.addWidget(self.page_4)
        self.frame_26 = QFrame(self.home)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(740, 0, 1001, 711))
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_12 = QFrame(self.frame_26)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(530, 110, 421, 581))
        self.frame_12.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(30, 30, 161, 161))
        self.frame_13.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_13)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 161, 161))
        self.cpu_progress_bar = QVBoxLayout(self.verticalLayoutWidget_2)
        self.cpu_progress_bar.setObjectName(u"cpu_progress_bar")
        self.cpu_progress_bar.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(230, 30, 161, 161))
        self.frame_18.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame_18)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 161, 161))
        self.gpu_progress_bar = QVBoxLayout(self.verticalLayoutWidget_3)
        self.gpu_progress_bar.setObjectName(u"gpu_progress_bar")
        self.gpu_progress_bar.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(30, 220, 361, 331))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame_19)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 361, 331))
        self.console_dialogue_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.console_dialogue_layout.setObjectName(u"console_dialogue_layout")
        self.console_dialogue_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.horizontalLayoutWidget)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setGeometry(QRect(0, 0, 361, 331))
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame_53)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-2, 0, 361, 331))
        self.frame_2.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalScrollBar_3 = QScrollBar(self.frame_2)
        self.verticalScrollBar_3.setObjectName(u"verticalScrollBar_3")
        self.verticalScrollBar_3.setGeometry(QRect(350, 0, 16, 331))
        self.verticalScrollBar_3.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 12px;\n"
"    margin: 5px 0 5px 5;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 50px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(45, 45, 68);\n"
"	width: 7px;\n"
"	height: 5px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
""
                        "QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(45, 45, 68);\n"
"	width: 7px;\n"
"	height: 5px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"")
        self.verticalScrollBar_3.setOrientation(Qt.Orientation.Vertical)

        self.console_dialogue_layout.addWidget(self.frame_52)

        self.frame_11 = QFrame(self.frame_26)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(20, 110, 471, 281))
        self.frame_11.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_4 = QWidget(self.frame_11)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 471, 281))
        self.to_do_list_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.to_do_list_layout.setObjectName(u"to_do_list_layout")
        self.to_do_list_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_26)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(30, 420, 131, 271))
        self.frame_22.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_5 = QPushButton(self.frame_22)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 30, 91, 211))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"font: 5pt \"Peak 5pt\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"   color: #c5c5c5;\n"
"   background-color: #2f3047\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   color: #c5c5c5;\n"
"   background-color: #303248;\n"
"}\n"
"\n"
"border-radius: 10px")
        self.frame_20 = QFrame(self.frame_26)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(180, 420, 311, 271))
        self.frame_20.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_16 = QWidget(self.frame_20)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(-1, -1, 311, 271))
        self.donut_layout_dash = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.donut_layout_dash.setObjectName(u"donut_layout_dash")
        self.donut_layout_dash.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.home)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(0, 710, 1721, 181))
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_23 = QFrame(self.frame_27)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(30, 20, 1661, 151))
        self.frame_23.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = QFrame(self.frame_23)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(9, 9, 391, 131))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_5 = QWidget(self.frame_4)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 0, 391, 131))
        self.weather_layout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.weather_layout.setObjectName(u"weather_layout")
        self.weather_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_23)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setGeometry(QRect(420, 10, 781, 131))
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_4 = QWidget(self.frame_54)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 0, 781, 131))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_23)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setGeometry(QRect(1240, 10, 411, 131))
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_13 = QWidget(self.frame_56)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(0, 0, 411, 131))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_44 = QFrame(self.row_2)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setGeometry(QRect(-1, 0, 1661, 861))
        self.frame_45.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);")
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setGeometry(QRect(10, 10, 601, 841))
        self.frame_46.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(43, 45, 54, 180);")
        self.frame_46.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(40, 20, 511, 41))
        self.frame_48.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.label_14 = QLabel(self.frame_48)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(110, 0, 301, 41))
        self.label_14.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 16pt \"Script MT Bold\";\n"
"background-color: rgba(31, 21, 65, 0);\n"
"border-radius: 10px")
        self.frame_49 = QFrame(self.frame_46)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setGeometry(QRect(40, 80, 511, 711))
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_11 = QWidget(self.frame_49)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(0, 0, 511, 361))
        self.use_stat_layout = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.use_stat_layout.setObjectName(u"use_stat_layout")
        self.use_stat_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_45)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setGeometry(QRect(620, 10, 1031, 841))
        self.frame_47.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(43, 45, 54, 180);")
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_10 = QWidget(self.frame_47)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(0, 0, 1031, 841))
        self.pie_graph_layout = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.pie_graph_layout.setObjectName(u"pie_graph_layout")
        self.pie_graph_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_19.addWidget(self.frame_44)


        self.verticalLayout.addWidget(self.row_2)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_6 = QFrame(self.new_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(30, 20, 551, 791))
        self.frame_7.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(20, 20, 511, 41))
        self.frame_9.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 0, 291, 41))
        self.label.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 16pt \"Script MT Bold\";\n"
"background-color: rgba(31, 21, 65, 0);\n"
"border-radius: 10px")
        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(20, 80, 511, 691))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(20, 20, 221, 211))
        self.frame_17.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_35 = QFrame(self.frame_17)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(20, 10, 181, 41))
        self.frame_35.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.label_9 = QLabel(self.frame_35)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, -1, 81, 41))
        self.label_9.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.radioButton_2 = QRadioButton(self.frame_17)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 60, 181, 21))
        self.radioButton_3 = QRadioButton(self.frame_17)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(20, 90, 181, 21))
        self.radioButton_4 = QRadioButton(self.frame_17)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(20, 180, 181, 21))
        self.radioButton_8 = QRadioButton(self.frame_17)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(20, 120, 181, 21))
        self.frame_28 = QFrame(self.frame_15)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(270, 20, 221, 211))
        self.frame_28.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_36 = QFrame(self.frame_28)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(20, 10, 181, 41))
        self.frame_36.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.label_10 = QLabel(self.frame_36)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 0, 81, 41))
        self.label_10.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.radioButton_5 = QRadioButton(self.frame_28)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(20, 60, 181, 21))
        self.radioButton_6 = QRadioButton(self.frame_28)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(20, 90, 181, 21))
        self.frame_43 = QFrame(self.frame_28)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(10, 140, 201, 31))
        self.frame_43.setStyleSheet(u"background-color:rgba(0, 170, 0,0);")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.radioButton_7 = QRadioButton(self.frame_28)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(20, 120, 181, 21))
        self.AccentizerRadioButton = QRadioButton(self.frame_28)
        self.AccentizerRadioButton.setObjectName(u"AccentizerRadioButton")
        self.AccentizerRadioButton.setGeometry(QRect(20, 180, 181, 21))
        self.AccentizerRadioButton.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_37 = QFrame(self.frame_15)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(19, 469, 471, 201))
        self.frame_37.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_12 = QWidget(self.frame_37)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(0, 50, 471, 151))
        self.configure_pc_layout = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.configure_pc_layout.setObjectName(u"configure_pc_layout")
        self.configure_pc_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.frame_37)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setGeometry(QRect(10, 10, 451, 31))
        self.frame_55.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.label_18 = QLabel(self.frame_55)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(90, -10, 291, 51))
        self.label_18.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.frame_38 = QFrame(self.frame_15)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(19, 259, 471, 181))
        self.frame_38.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.dial = QDial(self.frame_38)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(260, 40, 201, 131))
        self.dial_2 = QDial(self.frame_38)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setGeometry(QRect(9, 43, 211, 131))
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(50, 10, 141, 31))
        self.frame_39.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_39)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 0, 111, 31))
        self.label_12.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.frame_42 = QFrame(self.frame_38)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(290, 10, 141, 31))
        self.frame_42.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.label_13 = QLabel(self.frame_42)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 0, 101, 31))
        self.label_13.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(630, 20, 1031, 791))
        self.frame_8.setStyleSheet(u"background-color: rgba(31, 21, 65, 120);\n"
"border-radius: 10px")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(430, 20, 181, 41))
        self.frame_10.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, -5, 131, 51))
        self.label_6.setStyleSheet(u"background-color: rgba(31, 21, 65, 0);\n"
"font: 9pt \"Peak 5pt\";\n"
"border-radius: 10px;\n"
"font: 700 16pt \"Script MT Bold\";")
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(20, 80, 991, 691))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_29 = QFrame(self.frame_16)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(560, 20, 411, 651))
        self.frame_29.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(20, 20, 371, 41))
        self.frame_30.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_30)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 0, 211, 41))
        self.label_7.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.frame_41 = QFrame(self.frame_29)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setGeometry(QRect(20, 380, 361, 251))
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_8 = QWidget(self.frame_41)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(0, 0, 361, 251))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.horizontalLayoutWidget_8)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalScrollBar_4 = QScrollBar(self.frame_40)
        self.verticalScrollBar_4.setObjectName(u"verticalScrollBar_4")
        self.verticalScrollBar_4.setGeometry(QRect(340, 0, 21, 251))
        self.verticalScrollBar_4.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: rgba(23, 25, 34, 250);\n"
"    width: 12px;\n"
"    margin: 5px 0 5px 5;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 50px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(45, 45, 68);\n"
"	width: 7px;\n"
"	height: 5px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SC"
                        "ROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(45, 45, 68);\n"
"	width: 7px;\n"
"	height: 5px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"")
        self.verticalScrollBar_4.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.frame_40)

        self.frame_58 = QFrame(self.frame_29)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setGeometry(QRect(20, 70, 371, 261))
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_15 = QWidget(self.frame_58)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(0, 0, 371, 261))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.QR_code_frame_3 = QFrame(self.horizontalLayoutWidget_15)
        self.QR_code_frame_3.setObjectName(u"QR_code_frame_3")
        self.QR_code_frame_3.setStyleSheet(u"background-color: rgba(23, 25, 34, 150);")
        self.QR_code_frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.QR_code_frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_51 = QFrame(self.QR_code_frame_3)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setGeometry(QRect(90, 10, 191, 31))
        self.frame_51.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.label_16 = QLabel(self.frame_51)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(80, 0, 41, 31))
        self.label_16.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 10pt \"Script MT Bold\";")
        self.Email_mail_edit = QLineEdit(self.QR_code_frame_3)
        self.Email_mail_edit.setObjectName(u"Email_mail_edit")
        self.Email_mail_edit.setGeometry(QRect(20, 80, 331, 40))
        self.Email_password_edit = QLineEdit(self.QR_code_frame_3)
        self.Email_password_edit.setObjectName(u"Email_password_edit")
        self.Email_password_edit.setGeometry(QRect(20, 130, 331, 40))
        self.Button_save_email = QPushButton(self.QR_code_frame_3)
        self.Button_save_email.setObjectName(u"Button_save_email")
        self.Button_save_email.setGeometry(QRect(290, 230, 71, 20))
        self.Button_save_email.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(23, 25, 34, 250);\n"
"border-radius: 10px;\n"
"border-color: rgba(23, 25, 34, 250);\n"
"font: 5pt \"Peak 5pt\";\n"
"font: 700 7pt \"Script MT Bold\";\n"
"}\n"
"QPushButton:hover {\n"
"   border-color: rgba(23, 25, 54, 250);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:  #FF8C00;\n"
"   border-color:  #FF8C00;\n"
"}")

        self.horizontalLayout_11.addWidget(self.QR_code_frame_3)

        self.frame_31 = QFrame(self.frame_16)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(20, 20, 521, 361))
        self.frame_31.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(20, 20, 481, 41))
        self.frame_33.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_33)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(100, 0, 311, 41))
        self.label_11.setStyleSheet(u"background-color: rgba(43, 45, 54, 0);\n"
"font: 12pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.QR_code_frame = QFrame(self.frame_31)
        self.QR_code_frame.setObjectName(u"QR_code_frame")
        self.QR_code_frame.setGeometry(QRect(20, 70, 260, 260))
        self.QR_code_frame.setStyleSheet(u"background-color: rgba(23, 25, 34, 150);")
        self.QR_code_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.QR_code_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_7 = QWidget(self.QR_code_frame)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 261, 261))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.QR_code_frame_2 = QFrame(self.frame_31)
        self.QR_code_frame_2.setObjectName(u"QR_code_frame_2")
        self.QR_code_frame_2.setGeometry(QRect(290, 70, 211, 260))
        self.QR_code_frame_2.setStyleSheet(u"background-color: rgba(23, 25, 34, 150);")
        self.QR_code_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.QR_code_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_14 = QWidget(self.QR_code_frame_2)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(-1, -1, 211, 261))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.horizontalLayoutWidget_14)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgba(23, 25, 34, 150);")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_NewPass = QLineEdit(self.frame_57)
        self.lineEdit_NewPass.setObjectName(u"lineEdit_NewPass")
        self.lineEdit_NewPass.setGeometry(QRect(10, 110, 191, 40))
        self.lineEdit_NewPassConfirm = QLineEdit(self.frame_57)
        self.lineEdit_NewPassConfirm.setObjectName(u"lineEdit_NewPassConfirm")
        self.lineEdit_NewPassConfirm.setGeometry(QRect(10, 160, 191, 40))
        self.Button_save_password = QPushButton(self.frame_57)
        self.Button_save_password.setObjectName(u"Button_save_password")
        self.Button_save_password.setGeometry(QRect(130, 230, 71, 20))
        self.Button_save_password.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(23, 25, 34, 250);\n"
"border-radius: 10px;\n"
"border-color: rgba(23, 25, 34, 250);\n"
"font: 5pt \"Peak 5pt\";\n"
"font: 700 7pt \"Script MT Bold\";\n"
"}\n"
"QPushButton:hover {\n"
"   border-color: rgba(23, 25, 54, 250);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:  #FF8C00;\n"
"   border-color:  #FF8C00;\n"
"}")
        self.frame_50 = QFrame(self.frame_57)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setGeometry(QRect(10, 10, 191, 31))
        self.frame_50.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_50)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 0, 111, 31))
        self.label_15.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 10pt \"Script MT Bold\";")
        self.lineEdit_CurrentPass = QLineEdit(self.frame_57)
        self.lineEdit_CurrentPass.setObjectName(u"lineEdit_CurrentPass")
        self.lineEdit_CurrentPass.setGeometry(QRect(10, 60, 191, 40))

        self.horizontalLayout_10.addWidget(self.frame_57)

        self.frame_32 = QFrame(self.frame_16)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(20, 399, 521, 271))
        self.frame_32.setStyleSheet(u"background-color: rgba(43, 45, 54, 180);")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(20, 20, 481, 41))
        self.frame_34.setStyleSheet(u"background-color: rgba(23, 25, 34, 250);")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.frame_34)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 0, 241, 41))
        self.label_8.setStyleSheet(u"font: 9pt \"Peak 5pt\";\n"
"font: 700 14pt \"Script MT Bold\";")
        self.horizontalLayoutWidget_9 = QWidget(self.frame_32)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(20, 70, 481, 191))
        self.Current_settings_layout = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.Current_settings_layout.setObjectName(u"Current_settings_layout")
        self.Current_settings_layout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1500, 830, 121, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(23, 25, 34, 250);\n"
"border-radius: 15px;\n"
"border-color: rgba(23, 25, 34, 250);\n"
"font: 5pt \"Peak 5pt\";\n"
"font: 700 10pt \"Script MT Bold\";\n"
"}\n"
"QPushButton:hover {\n"
"   border-color: rgba(23, 25, 54, 250);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:  #FF8C00;\n"
"   border-color:  #FF8C00;\n"
"}")
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1370, 830, 111, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(23, 25, 34, 250);\n"
"border-radius: 15px;\n"
"border-color: rgba(23, 25, 34, 250);\n"
"font: 5pt \"Peak 5pt\";\n"
"font: 700 10pt \"Script MT Bold\";\n"
"}\n"
"QPushButton:hover {\n"
"   border-color: rgba(23, 25, 54, 250);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:  #FF8C00;\n"
"   border-color:  #FF8C00;\n"
"}")
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 830, 171, 31))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(23, 25, 34, 250);\n"
"border-radius: 15px;\n"
"border-color: rgba(23, 25, 34, 250);\n"
"font: 5pt \"Peak 5pt\";\n"
"font: 700 10pt \"Script MT Bold\";\n"
"}\n"
"QPushButton:hover {\n"
"   border-color: rgba(23, 25, 54, 250);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color:  #FF8C00;\n"
"   border-color:  #FF8C00;\n"
"}")

        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_4)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout_3.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.bar_charts.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"P3LOVE", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Voice assistant / dashboard", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 ", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Больше", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Больше", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Закрыть", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Поделиться", None))  # Share
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Тонкие настройки", None))  #Adjustments (Это для работы с QT Translate)
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"Больше", None))  # More
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**PY3LOVE**  An interface created by Ar3love.  MIREA License  Created by: Ar3love\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">PY3LOVE</span>  An interface created by Ar3love.  MIREA License  Created by: Ar3love</p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Voice assistant", None))
#if QT_CONFIG(tooltip)
        self.tetris_button.setToolTip(QCoreApplication.translate("MainWindow", u"Tetris", None))
#endif // QT_CONFIG(tooltip)
        self.tetris_button.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Tap on me", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442\u0430", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u043a\u0435\u0440", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Baya", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Kseniya", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"GTTS", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"TeraGirl", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Silero", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"GTTS", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"TeraTTS", None))
        self.AccentizerRadioButton.setText(QCoreApplication.translate("MainWindow", u"Accentizer", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u041f\u041a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u043e\u043c\u043a\u043e\u0441\u0442\u044c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0447\u0442\u044b", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.Email_mail_edit.setText("")
        self.Email_mail_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0432\u0430\u0448 \u043f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441:", None))
        self.Email_password_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.Button_save_email.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0430\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438", None))
        self.lineEdit_NewPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEdit_NewPassConfirm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.Button_save_password.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_CurrentPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u043e\u0434\u0441\u043a\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Сообщения", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Печать", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Выход", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"prod. by: ar3love", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1", None))
    # retranslateUi

