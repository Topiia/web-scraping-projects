import schedule
import time
import logging

from src.scraper import scrape_hn
from src.db import init_db, insert_posts

logging.basicConfig(level=logging.INFO)


def job():
    logging.info("Starting scheduled scraping...")

    init_db()
    data = scrape_hn(pages=3)
    insert_posts(data)

    logging.info("Scraping completed.")


if __name__ == "__main__":
    schedule.every().day.at("09:00").do(job)

    job()  # run once immediately

    while True:
        schedule.run_pending()
        time.sleep(60)