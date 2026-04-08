import sqlite3


def run_tests():
    conn = sqlite3.connect("data/news.db")
    cursor = conn.cursor()

    print("\n📊 Total rows:")
    cursor.execute("SELECT COUNT(*) FROM posts")
    print(cursor.fetchone()[0])

    print("\n📌 Sample rows:")
    cursor.execute("SELECT * FROM posts LIMIT 5")
    for row in cursor.fetchall():
        print(row)

    print("\n🔥 Top posts:")
    cursor.execute("SELECT title, points FROM posts ORDER BY points DESC LIMIT 5")
    for row in cursor.fetchall():
        print(row)

    conn.close()


if __name__ == "__main__":
    run_tests()