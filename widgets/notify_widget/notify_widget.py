__author__ = 'Ar3love'

from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QWidget, QVBoxLayout, QHBoxLayout,
                               QPushButton, QLineEdit, QTableWidget,
                               QTableWidgetItem, QTimeEdit,
                               QMessageBox, QDateEdit)
from PySide6.QtCore import Qt, QTimer, QTime, QDateTime, QDate
from playsound import playsound
import csv
import threading


class RemindersWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.load_reminders()

        # Timer to check for reminders
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_reminders)
        self.timer.start(60000)  # Check every minute

    def setup_ui(self):
        main_layout = QHBoxLayout(self)

        # Left side
        left_layout = QVBoxLayout()
        self.reminderLineEdit = QLineEdit()
        left_layout.addWidget(self.reminderLineEdit)
        self.reminderDateEdit = QDateEdit()
        self.reminderDateEdit.setDisplayFormat("yyyy-MM-dd")
        self.reminderDateEdit.setDate(QDate.currentDate())
        left_layout.addWidget(self.reminderDateEdit)
        self.reminderTimeEdit = QTimeEdit()
        self.reminderTimeEdit.setDisplayFormat("HH:mm")
        self.reminderTimeEdit.setTime(QTime.currentTime())
        left_layout.addWidget(self.reminderTimeEdit)
        main_layout.addLayout(left_layout)

        # Center
        self.remindersTable = QTableWidget()
        self.remindersTable.setColumnCount(3)
        self.remindersTable.setHorizontalHeaderLabels(["Дата", "Время", "Напоминание"])
        # After setting up the table
        self.remindersTable.verticalHeader().setVisible(False)  # Hide row numbers
        self.remindersTable.setCornerButtonEnabled(False)  # Hide top-left corner button
        self.remindersTable.setColumnWidth(2, 230)
        main_layout.addWidget(self.remindersTable)

        # Right side
        right_layout = QVBoxLayout()
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_reminder)
        right_layout.addWidget(add_button)
        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_selected_reminder)
        right_layout.addWidget(delete_button)
        main_layout.addLayout(right_layout)

        # Set proportions
        main_layout.setStretch(0, 1)  # Left side
        main_layout.setStretch(1, 3)  # Center
        main_layout.setStretch(2, 1)  # Right side

    def check_reminders(self):
        current_date_time = QDateTime.currentDateTime().toString("yyyy-MM-ddTHH:mm")
        for row in range(self.remindersTable.rowCount()):
            reminder_date_time = self.remindersTable.item(row, 0).text() + "T" + self.remindersTable.item(row, 1).text()
            if reminder_date_time == current_date_time:
                reminder_text = self.remindersTable.item(row, 2).text()
                self.show_notification(reminder_date_time, reminder_text)

    def add_reminder(self):
        reminder_text = self.reminderLineEdit.text()
        reminder_date = self.reminderDateEdit.date().toString("yyyy-MM-dd")
        reminder_time = self.reminderTimeEdit.time().toString("HH:mm")  # Changed to "HH:mm"
        if reminder_text and reminder_date and reminder_time:
            self.add_reminder_to_table([reminder_date, reminder_time, reminder_text])
            self.reminderLineEdit.clear()
            self.save_reminders()

    def show_notification(self, datetime, text):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText(f"Напоминание: {text}")
        message.setWindowTitle("Напоминания")
        message.setStandardButtons(QMessageBox.Ok)
        # Play sound in a separate thread
        threading.Thread(target=lambda: playsound('sounds/notify.wav')).start()
        QTimer.singleShot(10000, message.close)  # Message box will close after 10 seconds
        message.exec()
        # If user clicked "OK", delete the reminder
        if message.clickedButton() == message.button(QMessageBox.Ok):
            self.delete_reminder(datetime, text)

    def delete_reminder(self, datetime, text):
        QTimer.singleShot(10000, lambda: self.delete_reminder_after_interval(datetime, text))  # Delete reminder after 10 seconds

    def delete_reminder_after_interval(self, datetime, text):
        for row in range(self.remindersTable.rowCount()):
            reminder_date_time = self.remindersTable.item(row, 0).text() + "T" + self.remindersTable.item(row, 1).text()
            if reminder_date_time == datetime and self.remindersTable.item(row, 2).text() == text:
                self.remindersTable.removeRow(row)
                self.save_reminders()

    def load_reminders(self):
        try:
            with open('unique_csv/reminders.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.add_reminder_to_table(row)
        except FileNotFoundError:
            pass

    def add_reminder_to_table(self, reminder):
        row_position = self.remindersTable.rowCount()
        self.remindersTable.insertRow(row_position)
        for column, field in enumerate(reminder):
            item = QTableWidgetItem(field)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Make cell non-editable
            self.remindersTable.setItem(row_position, column, item)

    def delete_selected_reminder(self):
        selected_row = self.remindersTable.currentRow()
        if selected_row != -1:
            self.remindersTable.removeRow(selected_row)
            self.save_reminders()

    def save_reminders(self):
        with open('unique_csv/reminders.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in range(self.remindersTable.rowCount()):
                reminder = [self.remindersTable.item(row, column).text() for column in range(self.remindersTable.columnCount())]
                writer.writerow(reminder)


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    widget = RemindersWidget()
    window.setCentralWidget(widget)
    window.show()
    app.exec()
