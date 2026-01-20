from database.db import conexion
from datetime import datetime

def create_table():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_expense(amount, category, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        (amount, category, date)
    )
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT amount, category, date FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return expenses
