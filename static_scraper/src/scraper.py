import requests
import time
import logging
from bs4 import BeautifulSoup
from .parser import parse_book

logging.basicConfig(level=logging.INFO)

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_page(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                return response.text
        except Exception:
            pass

        time.sleep(2)

    logging.warning(f"Failed to fetch {url}")
    return None


def scrape_books(pages=1):
    all_data = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        logging.info(f"Scraping page {page}")

        html = fetch_page(url)

        if not html:
            print("❌ No HTML fetched")
            continue

        soup = BeautifulSoup(html, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        print(f"👉 Books found on page {page}: {len(books)}")

        for book in books:
            parsed = parse_book(book)

            if parsed:
                all_data.append(parsed)
            else:
                print("⚠️ Parsing failed for one book")

        time.sleep(1)

    print(f"✅ Total books collected: {len(all_data)}")

    return all_data