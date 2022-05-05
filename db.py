import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file,check_same_thread=False)
        self.cursor = self.connection.cursor()
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id, ))
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM  `users` WHERE `user_id` = ? ", (user_id, )).fetchall()
            return bool(len(result))
    def set_firstname(self, user_id, firstname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `first_name` = ? WHERE `user_id`= ? ", (firstname, user_id,))
    def set_address(self, user_id, address):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `address` = ? WHERE `user_id`= ? ", (address, user_id,))
    def set_phone(self, user_id, phone_number):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `phone_number` = ? WHERE `user_id`= ? ", (phone_number, user_id,))
    def set_birth(self, user_id, birth_date):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `birth_date` = ? WHERE `user_id`= ? ", (birth_date, user_id,))
    def get_user(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM  `users` WHERE `user_id` = ? ", (user_id, )).fetchall()
            print(result)
            return result[0]
    