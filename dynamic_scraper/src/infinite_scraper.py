from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scrape_infinite_quotes():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/scroll")

    wait = WebDriverWait(driver, 10)

    all_data = []

    last_count = 0

    while True:
        # wait for quotes
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        current_count = len(quotes)

        print(f"Current quotes: {current_count}")

        # stop condition
        if current_count == last_count:
            print("No new data loaded. Stopping...")
            break

        last_count = current_count

        # scroll to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

    # extract data after full load
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text

        all_data.append({
            "text": text,
            "author": author
        })

    driver.quit()

    print(f"Total quotes collected: {len(all_data)}")

    return all_data