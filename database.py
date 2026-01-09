import sqlite3

DB_NAME = "futebol.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS times (
        id INTEGER PRIMARY KEY,
        nome TEXT UNIQUE
    )
    """)

    c.execute("""
