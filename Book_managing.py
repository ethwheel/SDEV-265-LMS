#initialize db funciton creates db if one doesnt exist
import sqlite3

def initialize_database():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT UNIQUE NOT NULL,
        available INTEGER DEFAULT 1
    )
    """)
    
    conn.commit()
    conn.close()
