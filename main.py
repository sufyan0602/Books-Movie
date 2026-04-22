from datetime import datetime
import sqlite3

DB_PATH = "media_library.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# --- ADD ---

def add_book(title, author, genre, year):
    date_added = datetime.now().strftime("%Y-%m-%d")
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO books (title, author, genre, year, date_added)
            VALUES (?,?,?,?,?)
        """, (title, author, genre, year, date_added))
        conn.commit()
        return cursor.lastrowid

def add_movie(title, director, genre, year):
    date_added = datetime.now().strftime("%Y-%m-%d")
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO movies (title, director, genre, year, date_added)
            VALUES (?,?,?,?,?)
        """, (title, director, genre, year, date_added))
        conn.commit()
        return cursor.lastrowid

# --- LIST ---

def list_books():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()

def list_movies():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies")
        return cursor.fetchall()

# --- SEARCH ---

def search_books(query):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ?", (f"%{query}%",))
        return cursor.fetchall()

def search_movies(query):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE title LIKE ?", (f"%{query}%",))
        return cursor.fetchall()

# --- UPDATE ---

def update_book_status(book_id, status):
    if status not in ["READ", "UNREAD"]:
        raise ValueError("Invalid status. Must be READ or UNREAD")
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"No book found with id {book_id}")
        return True

def update_movie_status(movie_id, status):
    if status not in ["WATCHED", "UNWATCHED"]:
        raise ValueError("Invalid status. Must be WATCHED or UNWATCHED")
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE movies SET status = ? WHERE id = ?", (status, movie_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"No movie found with id {movie_id}")
        return True

# --- DELETE ---

def delete_book(book_id):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"No book found with id {book_id}")
        return True

def delete_movie(movie_id):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"No movie found with id {movie_id}")
        return True

# --- TEST ---

if __name__ == "__main__":
    
    with get_db() as conn:
        conn.execute("DELETE FROM books")
        conn.execute("DELETE FROM movies")
        conn.execute("DELETE FROM sqlite_sequence WHERE name='books'")
        conn.execute("DELETE FROM sqlite_sequence WHERE name='movies'")
        conn.commit()
    # Add
    print("Added book ID:", add_book("Red Rising", "Pierce Brown", "Sci-Fi", 2014))
    print("Added movie ID:", add_movie("Interstellar", "Christopher Nolan", "Sci-Fi", 2014))

    # List
    print("\n-- Books --")
    for book in list_books():
        print(dict(book))

    print("\n-- Movies --")
    for movie in list_movies():
        print(dict(movie))

    # Search
    print("\n-- Search --")
    for result in search_books("red"):
        print(dict(result))

    # Update
    update_book_status(1, "READ")
    update_movie_status(1, "WATCHED")

    # Delete
    delete_book(1)
    print("\n-- Books after delete --")
    for book in list_books():
        print(dict(book))
        
    # Delete 
    delete_movie(1)
    print("\n-- Movies after delete --")
    for movie in list_movies():
        print(dict(movie))