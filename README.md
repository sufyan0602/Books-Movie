# 📚 Media Library

A personal media tracking app for physical books and movies. Built with Python and SQLite.

## Overview

This project lets you manage a local directory of your physical book and movie collection — add entries, list them, search by title, and track read/watched status.

Built in phases:
- **Phase 1** ✅ — Python + SQLite backend (current)
- **Phase 2** — Web frontend
- **Phase 3** — Migrate from SQLite to PostgreSQL

---

## Features (Phase 1)

- Add a book or movie to the library
- List all books or movies
- Search by title (partial match)
- Mark a book as `READ` / `UNREAD`
- Mark a movie as `WATCHED` / `UNWATCHED`
- Automatically records the date each entry was added

---

## Project Structure

```
media-library/
├── database.py       # Creates the SQLite database and tables
├── main.py           # All core functions
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

## Usage

### Setup

```bash
python database.py   # Creates the database and tables
```

### Example

```python
from main import *

# Add entries
add_book("Red Rising", "Pierce Brown", "Sci-Fi", 2014)
add_movie("Interstellar", "Christopher Nolan", "Sci-Fi", 2014)

# List all
list_book()
list_movie()

# Search
search_books("rising")
search_movies("inter")

# Update status
update_book_status(1, "READ")
update_movie_status(1, "WATCHED")
```

---

## Tech Stack

- Python 3
- SQLite3 (built-in)

---

## Roadmap

- [ ] Web frontend (Flask or FastAPI)
- [ ] PostgreSQL migration
- [ ] Filter by genre or year
- [ ] Delete entries
- [ ] Export to CSV
