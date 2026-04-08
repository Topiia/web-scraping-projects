import requests
import logging
from bs4 import BeautifulSoup
from .parser import parse_posts

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://news.ycombinator.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch(url, retries=3):
    for _ in range(retries):
        try:
            res = requests.get(url, headers=HEADERS, timeout=5)
            if res.status_code == 200:
                return res
        except Exception:
            pass
    return None


def scrape_hn(pages=3):
    url = BASE_URL
    all_data = []

    for _ in range(pages):
        logging.info(f"Scraping: {url}")

        response = fetch(url)
        if not response:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        posts = parse_posts(soup)
        all_data.extend(posts)

        more_link = soup.find("a", string="More")
        if more_link:
            url = BASE_URL + more_link["href"]
        else:
            break

    logging.info(f"Total collected: {len(all_data)}")

    return all_data