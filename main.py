from datetime import datetime 
import sqlite3

def add_book(title, author, genre, year):  
    date_added = datetime.now().strftime("%Y-%m-%d")
    with sqlite3.connect("media_library.db") as connect: 
        cursor = connect.cursor()
        cursor.execute("""--sql
            INSERT INTO books (title, author, genre, year, date_added)
            VALUES (?,?,?,?,?)
        """, (title, author, genre, year, date_added))
        connect.commit()

def add_movie(title, director, genre, year):
    date_added = datetime.now().strftime("%Y-%m-%d")
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
            INSERT INTO movies(title, director, genre, year, date_added)
            VALUES (?,?,?,?,?)
        """, (title, director, genre, year, date_added))
        connect.commit()

def list_book():
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
            SELECT * FROM books
        """)
        rows = cursor.fetchall()
    for row in rows:
        print(row)

def list_movie():
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
            SELECT * FROM movies
        """)
        rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_books(searchword):
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
            SELECT * FROM books WHERE title LIKE ?
        """, ("%" + searchword + "%",))
        rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_movies(searchword):
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
            SELECT * FROM movies WHERE title LIKE ?
        """, ("%" + searchword + "%",))
        rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_book_status(book_id, status):
    if status not in ["READ", "UNREAD"]:
        raise ValueError("Invalid status. Must be READ or UNREAD")
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
            UPDATE books SET status = ? WHERE id = ?
        """, (status, book_id))
        connect.commit()

def update_movie_status(movie_id, status):
    if status not in ["WATCHED", "UNWATCHED"]:
            raise ValueError("Invalid status. Must be WATCHED or UNWATCHED")
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
            UPDATE movies SET status = ? WHERE id = ?
        """, (status, movie_id))
        connect.commit()

def delete_book(book_id):
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
                DELETE FROM books where id = ?
                       """,(book_id,))
        connect.commit()
        
def delete_movie(movie_id):
    with sqlite3.connect("media_library.db") as connect:
        cursor = connect.cursor()
        cursor.execute("""--sql
                DELETE FROM movies where id = ?
                       """,(movie_id,))
        connect.commit()

if __name__ == "__main__":
    add_book("Red Rising", "Pierce Brown", "Sci-Fi", 2014)
    add_movie("Interstellar", "Christopher Nolan", "Sci-Fi", 2014)
    search_books("red")
    search_movies("stellar")
    update_book_status(1, "READ")
    update_movie_status(1, "WATCHED")
    list_book()
    list_movie()
