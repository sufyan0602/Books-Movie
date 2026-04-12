# 📚 Media Library

A personal media tracking app for books and movies. Built with Python and SQLite.

## Overview

Manage a local collection of your books and movies — add entries, list them, search by title, track read/watched status, and delete entries.

---

## Project Structure

```
media-library/
├── database.py       # Creates the SQLite database and tables
├── main.py           # All core CRUD functions
└── media_library.db  # Auto-generated SQLite database
```

---

## Database Schema

```sql
books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    genre TEXT,
    year INTEGER,
    status TEXT,
    date_added TEXT
)

movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    director TEXT,
    genre TEXT,
    year INTEGER,
    status TEXT,
    date_added TEXT
)
```

---

## Setup

```bash
python database.py   # Creates the database and tables
```

---

## Usage

```python
from main import *

# Add entries
add_book("Red Rising", "Pierce Brown", "Sci-Fi", 2014)
add_movie("Interstellar", "Christopher Nolan", "Sci-Fi", 2014)

# List all
list_book()
list_movie()

# Search by title
search_books("rising")
search_movies("inter")

# Update status
update_book_status(1, "READ")
update_movie_status(1, "WATCHED")

# Delete
delete_book(1)
delete_movie(1)
```

---

## Tech Stack

- Python 3
- SQLite3 (built-in)

---

## Roadmap

- [ ] Web frontend (Flask)
- [ ] PostgreSQL migration
- [ ] Filter by genre or year
- [x] Delete entries
- [ ] Export to CSV
