#initialize db funciton creates db if one doesnt exist
import sqlite3

def initialize_database():
    conn = sqlite3.connect("library.db") #other functions connect to library.db
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
#inserting random books to populate the db
def insert_books():
    books = [
        ("1984", "George Orwell", "9780451524935", 1),
        ("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1),
        ("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1),
        ("Moby-Dick", "Herman Melville", "9781503280786", 1),
        ("Pride and Prejudice", "Jane Austen", "9781503290563", 1),
        ("War and Peace", "Leo Tolstoy", "9781400079988", 1),
        ("Ulysses", "James Joyce", "9781840226355", 1),
        ("The Catcher in the Rye", "J.D. Salinger", "9780316769488", 1),
        ("Brave New World", "Aldous Huxley", "9780060850524", 1),
        ("The Hobbit", "J.R.R. Tolkien", "9780547928227", 1)
    ]
    
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    for book in books:
        try:
            cursor.execute("""
            INSERT INTO books (title, author, isbn, available)
            VALUES (?, ?, ?, ?)
            """, book)
        except sqlite3.IntegrityError:
            pass
    conn.commit()
    conn.close()
