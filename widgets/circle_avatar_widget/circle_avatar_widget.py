__author__ = 'Ar3love'

from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import sqlite3


class CircleAvatar(QWidget):
    def __init__(self, pixmap_path, parent=None):
        super().__init__(parent)
        self.pixmap_path = pixmap_path or 'images/images/avatar.jpg'

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Включить сглаживание
        pixmap = QPixmap(self.pixmap_path)
        # Нарисовать аватар
        path = QPainterPath()
        path.addEllipse(0, 0, self.width(), self.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, self.width(), self.height(), pixmap)


class MainCircleWidget(QWidget):
    def __init__(self, username):
        super().__init__()

        self.username = username

        # Создать макеты
        avatar_layout = QHBoxLayout()
        name_layout = QVBoxLayout()

        user_info = self.get_user_info()

        # Создать аватар
        self.avatar = CircleAvatar(user_info['avatar_path'])
        self.avatar.setFixedSize(50, 50)  # Установить размер аватара
        self.avatar.mousePressEvent = self.change_avatar  # Добавьте это

        # Создать метки для имени и фамилии
        name_label = QLabel(user_info['first_name'])
        surname_label = QLabel(user_info['last_name'])

        # Изменить шрифт для меток имени и фамилии

        # Добавить метки в макет name_layout
        name_layout.addWidget(name_label)
        name_layout.addWidget(surname_label)

        # Добавить аватар и макет name_layout в макет avatar_layout
        avatar_layout.addWidget(self.avatar)
        avatar_layout.addSpacing(15)  # Добавить пространство
        avatar_layout.addLayout(name_layout)

        # Установить avatar_layout как макет главного виджета
        self.setLayout(avatar_layout)

    def get_user_info(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, avatar_path FROM users WHERE name=?", (self.username,))
        user_info = cursor.fetchone()
        conn.close()

        return {
            'first_name': user_info[0],
            'last_name': user_info[1],
            'avatar_path': user_info[2]
        }

    def change_avatar(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите новый аватар", "", "Изображения (*.png *.xpm *.jpg);;Все файлы (*)", options=options)
        if file_name:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET avatar_path=? WHERE name=?", (file_name, self.username))
            conn.commit()
            conn.close()

            self.avatar.pixmap_path = file_name
            self.avatar.update()  # Обновите виджет, чтобы отобразить новый аватар


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainCircleWidget()
    form.show()
    sys.exit(app.exec())
