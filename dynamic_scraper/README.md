# Dynamic Web Scraper (Selenium)

## Description

A Selenium-based scraper designed to extract data from JavaScript-rendered pages that cannot be handled using traditional HTTP requests.

---

## Features

* JavaScript-rendered content scraping
* Explicit waits for reliable execution
* Pagination via button interaction
* Multi-page data extraction

---

## Tech Stack

* Python
* Selenium
* Pandas

---

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Download ChromeDriver matching your Chrome version

3. Place `chromedriver.exe` in project root (not tracked in Git)

---

## How to Run

```bash
python main.py
```

---

## Output

* `data/quotes.csv`

---

## Key Learning

* Handling dynamic DOM
* Browser automation
* Synchronization using waits
