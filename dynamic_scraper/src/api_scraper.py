import requests

BASE_URL = "https://quotes.toscrape.com/api/quotes?page={}"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_api_quotes():
    all_data = []
    page = 1

    while True:
        url = BASE_URL.format(page)

        response = requests.get(url, headers=HEADERS)

        print(f"Status: {response.status_code} for page {page}")

        if response.status_code != 200:
            break

        data = response.json()

        quotes = data.get("quotes", [])

        if not quotes:
            print("No quotes found, stopping...")
            break

        print(f"Page {page} → {len(quotes)} quotes")

        for q in quotes:
            all_data.append({
                "text": q["text"],
                "author": q["author"]["name"]
            })

        if not data.get("has_next"):
            break

        page += 1

    print(f"Total quotes collected: {len(all_data)}")

    return all_data