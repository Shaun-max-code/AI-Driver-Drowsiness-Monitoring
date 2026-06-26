import sqlite3
from datetime import datetime

def log_event(gesture, action):

    conn = sqlite3.connect("gesture_log.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO logs
        (timestamp, gesture, action)
        VALUES (?, ?, ?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            gesture,
            action
        )
    )

    conn.commit()
    conn.close()