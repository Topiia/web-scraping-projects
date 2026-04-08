from src.scraper import scrape_quotes
from src.utils import save_to_csv

def main():
    data = scrape_quotes()
    save_to_csv(data, "data/quotes.csv")

if __name__ == "__main__":
    main()