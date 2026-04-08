import sqlite3
import pandas as pd


def export_data():
    conn = sqlite3.connect("data/news.db")

    query = "SELECT * FROM posts"
    df = pd.read_sql_query(query, conn)

    df.to_csv("data/final_dataset.csv", index=False)

    conn.close()

    print("✅ Exported to data/final_dataset.csv")


if __name__ == "__main__":
    export_data()