#from src.scraper import scrape_quotes
#from src.infinite_scraper import scrape_infinite_quotes
from src.api_scraper import scrape_api_quotes
from src.utils import save_to_csv

def main():
    # data = scrape_quotes()
    # save_to_csv(data, "data/quotes.csv")
    # data = scrape_infinite_quotes()
    # save_to_csv(data, "data/infinite_quotes.csv")
    data = scrape_api_quotes()
    save_to_csv(data, "data/api_quotes.csv")

if __name__ == "__main__":
    main()