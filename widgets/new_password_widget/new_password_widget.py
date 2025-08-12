__author__ = 'Ar3love'
import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def update_password(self, username, new_password):
        print(f"Обновление пароля для {username}. Ваш новый пароль: {new_password}")
        sql = '''UPDATE users SET password = ? WHERE name = ?'''
        self.cursor.execute(sql, (new_password, username))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def get_password(self, username):
        sql = '''SELECT password FROM users WHERE name = ?'''
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchone()
        return result[0] if result else None
