import sqlite3
def conexion():
    return sqlite3.connect("gastos.db")
