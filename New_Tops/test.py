import sqlite3


def connect_db():
    conn = sqlite3.connect("Employee.db")
    return conn

    cur.execute("""
            CREATE TABLE Employee Data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                date TEXT,
                status TEXT
            )
        """)
    conn.commit()
    conn.close()





