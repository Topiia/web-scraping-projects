from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_quotes():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/js/")

    wait = WebDriverWait(driver, 10)

    all_data = []

    while True:
        # wait until quotes load
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        print(f"Quotes found on page: {len(quotes)}")

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text

            all_data.append({
                "text": text,
                "author": author
            })

        # try clicking next
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
            next_button.click()

            # wait for page to change (new quotes load)
            wait.until(EC.staleness_of(quotes[0]))

        except:
            print("No more pages")
            break

    driver.quit()
    print(f"Total quotes collected: {len(all_data)}")

    return all_data