# Check in / Check out functions
import sqlite3

def check_out_book(isbn):
    """
    Marks a book as checked out (sets available to 0) if it is currently available.
    """
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check if the book exists and get its current availability
    cursor.execute("SELECT available FROM books WHERE isbn = ?", (isbn))
    result = cursor.fetchone()

    if result is None:
        print("Error: Book not found.")
    elif result[0] == 0:
        print("This book is already checked out.")
    else:
        cursor.execute("UPDATE books SET available = 0 WHERE isbn = ?", (isbn))
        conn.commit()
        print("Book checked out successfully!")

    conn.close()

def check_in_book(isbn):
    """ 
    Marks a book as checked in (sets available to 1) if it is currently checked out.
    """
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check if the book exists and get its current availaility 
    cursor.execute("SELECT available FROM books WHERE isbn = ?", (isbn))
    result = cursor.fetchone()

    if result is None:
        print("Error: Book not found.")
    elif result[0] == 1:
        print("This book is already checked in.")
    else: 
        cursor.execute("UPDATE books SET available = 1 WHERE isbn = ?", (isbn))
        conn.commit()
        print("Book checked in successfully!")

    conn.close()

    
