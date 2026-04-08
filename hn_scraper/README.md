# Hacker News Scraper Pipeline

## Overview

This project is a structured data pipeline that scrapes Hacker News, processes the data, stores it in a database, and exports it into a dataset format suitable for analysis or AI workflows.

It demonstrates real-world scraping practices including pagination handling, data cleaning, deduplication, and automation.

---

## Features

* Multi-page scraping (pagination support)
* Clean data extraction (title, link, points, author, comments)
* SQLite database storage
* Deduplication using unique constraints
* CSV dataset export
* Interactive CLI control panel
* Scheduler support for automation

---

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas
* SQLite
* Schedule

---

## Project Structure

```
hn_scraper/
│
├── data/                  # Generated data (ignored in git)
│   ├── news.db
│   └── final_dataset.csv
│
├── src/                   # Core logic
│   ├── scraper.py
│   ├── parser.py
│   ├── db.py
│   ├── utils.py
│
├── scripts/               # Utility scripts
│   ├── export.py
│   ├── scheduler.py
│   └── test_db.py
│
├── main.py                # Control panel (entry point)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

Run the control panel:

```bash
python main.py
```

---

## Menu Options

### 1. Run Scraper

* Scrapes Hacker News across multiple pages
* Stores data in SQLite database

### 2. Export DB → CSV

* Converts database data into CSV dataset
* Output:

  ```
  data/final_dataset.csv
  ```

### 3. Run Scheduler

* Runs one automated scraping cycle

### 4. Test Database

* Displays row count and sample data
* Helps verify data integrity

---

## Data Flow

```
Scraper → Database → Export → CSV Dataset
```

---

## Output

* Database:

  ```
  data/news.db
  ```

* Dataset:

  ```
  data/final_dataset.csv
  ```

---

## Notes

* Data files are ignored via `.gitignore`
* Scheduler runs continuously if executed directly
* Duplicate entries are prevented at database level
* Designed for extension (API layer, deployment, etc.)

---

## What This Project Demonstrates

* Web scraping fundamentals (static + structured parsing)
* Handling real-world HTML inconsistencies
* Data pipeline design
* Database integration
* Clean project structuring

---

## Future Improvements

* API layer (Flask/FastAPI)
* Cloud deployment
* Proxy & anti-blocking strategies
* Scheduled automation via cron/Task Scheduler

---

## Author

Built as a practical data engineering and web scraping project.
