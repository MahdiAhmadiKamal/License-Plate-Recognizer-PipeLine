import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("license_plates.db")
        self.cursor = self.connection.cursor()

    def get_data(self):
        
        results = self.cursor.execute("SELECT * FROM license_plates")
        license_plates_list = results.fetchall()
        return license_plates_list
