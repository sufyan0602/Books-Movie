import sqlite3

connect = sqlite3.connect("media_library.db")
cursor = connect.cursor()

cursor.execute("""     
               CREATE TABLE IF NOT EXISTS books(
                   
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                genre TEXT,
                year INTEGER,
                status TEXT,
                date_added TEXT
               )
               """)

cursor.execute("""     
               CREATE TABLE IF NOT EXISTS movies(
                   
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                director TEXT,
                genre TEXT,
                year INTEGER,
                status TEXT,
                date_added TEXT
               )
               """)

connect.commit()