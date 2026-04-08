# Web Scraping Projects

## Overview

This repository contains two end-to-end web scraping pipelines demonstrating both static and dynamic data extraction techniques used in real-world scenarios.

---

## Projects

### 1. Static Web Scraper (BeautifulSoup)

**Description**

* Extracts product data from a paginated website
* Handles multi-page navigation using URL patterns

**Features**

* HTTP-based scraping using `requests`
* HTML parsing with `BeautifulSoup`
* Pagination handling
* Data cleaning (price normalization, rating mapping)
* Structured output (CSV, JSON)

**Tech Stack**

* Python
* BeautifulSoup
* Requests
* Pandas

---

### 2. Dynamic Web Scraper (Selenium)

**Description**

* Scrapes JavaScript-rendered content using browser automation
* Handles dynamic page loading and user interaction

**Features**

* Browser automation using Selenium
* Explicit waits (no blind delays)
* Pagination via "Next" button interaction
* Dynamic DOM handling
* Structured data extraction

**Tech Stack**

* Python
* Selenium
* Pandas

---

## Key Concepts Demonstrated

* Static vs Dynamic scraping
* DOM parsing vs browser automation
* Pagination strategies
* Data cleaning and validation
* Reliable scraping using wait conditions

---

## Folder Structure

```
web-scraping-projects/
│
├── static_scraper/
├── dynamic_scraper/
├── requirements.txt
└── README.md
```

---

## Disclaimer

This project is for educational purposes. Data is scraped from publicly available demo websites.
