__author__ = 'Ar3love'

from PySide6.QtWidgets import *
import csv
import sys
from PySide6.QtGui import QFont, QColor, QPainter, QBrush
from PySide6.QtCore import Qt  # Добавить импорт Qt


class BulletDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(QBrush(QColor("white")))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(option.rect.x() + 5, option.rect.y() + option.rect.height() / 2 - 5, 10, 10)
        option.rect.setLeft(option.rect.left() + 20)
        QStyledItemDelegate.paint(self, painter, option, index)
        painter.restore()


class ToDoLister(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Загрузить задачи из CSV-файла
        self.load_tasks_from_csv('unique_csv/tasks.csv')

        self.setAlternatingRowColors(False)
        self.setStyleSheet("""
            QListWidget {
                padding: 20px;
                background: rgb(43, 45, 54);
            }
            QListWidget::item {
                padding: 5px;
                color: white;
            }
            QListWidget::item:hover {
                background: rgb(64, 66, 77);
            }
            QListWidget::item:selected {
                background: rgb(43, 45, 54);
            }
        """)

        self.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.itemChanged.connect(self.update_csv)

        self.setItemDelegate(BulletDelegate(self))

        # Add Buttons
        self.addButton = QPushButton("Добавить")
        self.addButton.clicked.connect(self.add_task)
        self.deleteButton = QPushButton("Удалить")
        self.deleteButton.clicked.connect(self.delete_task)

        # Create layout for buttons
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.addButton)
        button_layout.addWidget(self.deleteButton)

    def load_tasks_from_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        task = row[0]
                        item = QListWidgetItem(task)
                        font = QFont("Courier New", 18)
                        item.setFont(font)
                        item.setFlags(item.flags() | Qt.ItemIsEditable)
                        self.addItem(item)
        except FileNotFoundError:
            pass

    def update_csv(self, item):
        try:
            with open('unique_csv/tasks.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for i in range(self.count()):
                    task_text = self.item(i).text().lstrip("• ")
                    writer.writerow([task_text])
        except Exception as e:
            print(f"Error updating CSV: {e}")

    def add_task(self):
        task, ok = QInputDialog.getText(self, 'Добавить задачу', 'Введите новую задачу:')
        if ok and task:
            item = QListWidgetItem(task)
            font = QFont("Courier New", 18)
            item.setFont(font)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.addItem(item)
            self.update_csv(item)

    def delete_task(self):
        current_item = self.currentItem()
        if current_item:
            row = self.row(current_item)
            self.takeItem(row)
            self.update_csv(current_item)