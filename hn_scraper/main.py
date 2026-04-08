from src.scraper import scrape_hn
from src.db import init_db, insert_posts

# direct imports (NO subprocess)
from scripts.export import export_data
from scripts.test_db import run_tests
from scripts.scheduler import job as run_scheduler_job


def run_scraper(pages):
    init_db()
    data = scrape_hn(pages=pages)
    insert_posts(data)
    print(f"✅ Scraped and stored {len(data)} posts")


def export_csv():
    export_data()


def run_scheduler():
    print("Running one scheduled job manually...")
    run_scheduler_job()


def test_db():
    run_tests()


def menu():
    print("\n=== HN Scraper Control Panel ===")
    print("1. Run Scraper")
    print("2. Export DB → CSV")
    print("3. Run Scheduler (one run)")
    print("4. Test Database")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            pages = int(input("Enter number of pages (default 3): ") or 3)
            run_scraper(pages)
        except ValueError:
            print("❌ Invalid number")

    elif choice == "2":
        export_csv()

    elif choice == "3":
        run_scheduler()

    elif choice == "4":
        test_db()

    elif choice == "5":
        print("Exiting...")
        exit()

    else:
        print("❌ Invalid choice")


def main():
    while True:
        menu()


if __name__ == "__main__":
    main()