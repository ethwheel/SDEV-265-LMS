import sqlite3
from search import search_book
#add a book to the database
def add_book(title, author, isbn):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    #inserting the book into the db
    try:
        cursor.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", 
                       (title, author, isbn))
        conn.commit()
        print("Book added successfully!")
        #each ISBN should(?) be unique, if 2 exist there is a problem(?)
    except sqlite3.IntegrityError:
        print("Error: ISBN already exists.")
    
    conn.close()

#updated delete to use search book and confirmations
def delete_book(query, field="title"):
    book_id = search_book(query, field)
    if not book_id:
        print("No book found to delete.")
        return
    
    confirmation = input(f"Are you sure you want to delete book ID {book_id}? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        return
    
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    affected_rows = cursor.rowcount
    
    if affected_rows > 0:
        print("Book successfully deleted.")
    else:
        print("No book found.")
    
    conn.commit()
    conn.close()

#updating book details 
def update_book(query, field="title"):
    book_id = search_book(query, field)
    if not book_id:
        print("No book found to update.")
        return
    
    confirmation = input(f"Are you sure you want to update book ID {book_id}? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Update canceled.")
        return
    
    title = input("Enter new title (leave blank to keep unchanged): ").strip()
    author = input("Enter new author (leave blank to keep unchanged): ").strip()
    isbn = input("Enter new ISBN (leave blank to keep unchanged): ").strip()
    
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    updates = []
    values = []
    #no idea but it works
    if title:
        updates.append("title = ?")
        values.append(title)
    if author:
        updates.append("author = ?")
        values.append(author)
    if isbn:
        updates.append("isbn = ?")
        values.append(isbn)
    
    if updates:
        values.append(book_id)
        query = f"UPDATE books SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, values)
        conn.commit()
        print("Book updated successfully.")
    else:
        print("No changes provided.")
    
    conn.close()

