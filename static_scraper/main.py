from src.scraper import scrape_books
from src.utils import save_to_csv, save_to_json

def main():
    data = scrape_books(pages=5)
    save_to_csv(data, "data/books.csv")
    save_to_json(data, "data/books.json")

if __name__ == "__main__":
    main()