import sqlite3
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

#delete a book from the database
#Im doing ISBN because im not sure how I would delete with the title
def delete_book(isbn):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    # Fixed tuple formatting by adding a comma: (isbn,) 
    cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
    #checking if we deleted something
    affected_rows = cursor.rowcount

    if affected_rows > 0:
        print("Book successfully deleted.")
    else:
        print("No book found.")

    conn.commit()
    conn.close()
