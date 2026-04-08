import sqlite3


def init_db():
    conn = sqlite3.connect("data/news.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rank INTEGER,
            title TEXT UNIQUE,
            link TEXT,
            points INTEGER,
            author TEXT,
            comments INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_posts(data):
    conn = sqlite3.connect("data/news.db")
    cursor = conn.cursor()

    for item in data:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO posts (rank, title, link, points, author, comments)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                item["rank"],
                item["title"],
                item["link"],
                item["points"],
                item["author"],
                item["comments"]
            ))
        except Exception:
            pass

    conn.commit()
    conn.close()