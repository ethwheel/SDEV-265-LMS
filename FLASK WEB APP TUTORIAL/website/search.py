import sqlite3

import sqlite3

def search_book(query, field="title"):
    """
    Search for books in the database by a given field.
    
    Parameters:
    - query: The search term.
    - field: The database column to search (e.g., "title", "author", "isbn").
      Defaults to "title".
    
    Returns:
    - The book ID of the first matching result, or None if no match is found.
    """
    allowed_fields = ["title", "author", "isbn"]
    if field not in allowed_fields:
        print(f"Invalid search field. Choose one of: {allowed_fields}")
        return None

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql_query = f"SELECT id, title, author, isbn, available FROM books WHERE {field} LIKE ?"
    cursor.execute(sql_query, ('%' + query + '%',))
    result = cursor.fetchone()

    if result:
        book_id, title, author, isbn, available = result
        status = "Available" if available == 1 else "Checked Out"
        print(f"ID: {book_id} | Title: {title} | Author: {author} | ISBN: {isbn} | Status: {status}")
        conn.close()
        return book_id
    else:
        print("No books found matching your query.")
        conn.close()
        return None




