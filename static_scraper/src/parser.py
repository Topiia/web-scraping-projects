RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def clean_price(price_text):
    return float(price_text.replace("£", "").replace("Â", ""))

def parse_book(book):
    try:
        title = book.h3.a["title"]

        price_tag = book.find("p", class_="price_color")
        price = clean_price(price_tag.text) if price_tag else 0

        rating_raw = book.p["class"][1]
        rating = RATING_MAP.get(rating_raw, 0)

        availability_tag = book.find("p", class_="instock availability")
        availability = availability_tag.text.strip() if availability_tag else "Unknown"

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        }

    except Exception as e:
        print("❌ Error parsing book:", e)
        return None