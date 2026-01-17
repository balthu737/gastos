import sqlite3
def conexion():
    return sqlite3.connect("gastos.db")

def crear():
    conn = conexion()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()