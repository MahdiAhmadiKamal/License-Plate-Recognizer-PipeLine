import sqlite3
from difflib import SequenceMatcher


connection = sqlite3.connect("license_plates.db")
cursor = connection.cursor()
for data in cursor.execute("SELECT * FROM license_plates"):
    
    print(data)

# r = cursor.execute("SELECT * FROM license_plates")
# rr = r.fetchall()
# print(rr)

# print(SequenceMatcher(None, "Amir", "Amin").ratio())