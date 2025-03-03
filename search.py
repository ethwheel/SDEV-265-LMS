def search_book(query, field="title"):
    """
    Search for books in the database by a given field.
    
    Parameters:
    - query: The search term.
    - field: The database column to search (e.g., "title", "author", "isbn").
      Defaults to "title".
    """
    # Validate that the field is allowed to avoid SQL injection.
    allowed_fields = ["title", "author", "isbn"]
    if field not in allowed_fields:
        print(f"Invalid search field. Choose one of: {allowed_fields}")
        return

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Construct the SQL query. Using string formatting for the column is safe here because we've validated 'field'.
    sql_query = f"SELECT id, title, author, isbn, available FROM books WHERE {field} LIKE ?"
    # Use wildcards for a partial match.
    cursor.execute(sql_query, ('%' + query + '%',))
    results = cursor.fetchall()

    if results:
        print("Search results:")
        for row in results:
            id, title, author, isbn, available = row
            status = "Available" if available == 1 else "Checked Out"
            print(f"ID: {id} | Title: {title} | Author: {author} | ISBN: {isbn} | Status: {status}")
    else:
        print("No books found matching your query.")

    conn.close()
