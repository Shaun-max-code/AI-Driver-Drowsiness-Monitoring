import sqlite3

conn = sqlite3.connect("gesture_log.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    gesture TEXT,
    action TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")