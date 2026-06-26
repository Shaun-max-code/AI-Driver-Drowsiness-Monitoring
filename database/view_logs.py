import sqlite3

conn = sqlite3.connect("gesture_log.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM logs"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()