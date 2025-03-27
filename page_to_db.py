# page_to_db.py

# Task 3: Storing Data in a Database
import sqlite3
import requests
from bs4 import BeautifulSoup

DB_PATH = "db/scraped_data.db"


def create_database():
    """Creates SQLite database and wiki_data table if not exists."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS wiki_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        header TEXT,
        link TEXT
    )
    """)

    conn.commit()
    conn.close()


def scrape_wikipedia(url):
    """Scrapes a Wikipedia page and stores data in SQLite."""
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title").text.strip() if soup.find("title") else "No Title"

    headers = [header.text.strip() for header in soup.find_all(["h1", "h2", "h3"])]

    links = [a["href"] for a in soup.find_all("a", href=True)]

    insert_into_db(title, headers, links)


def insert_into_db(title, headers, links):
    """Inserts a limited amount of data into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Limit data to avoid too many rows
    limited_headers = headers[:10]  # Store only first 10 headers
    limited_links = links[:50]      # Store only first 50 links

    for header in limited_headers:
        for link in limited_links:
            cursor.execute("INSERT INTO wiki_data (title, header, link) VALUES (?, ?, ?)",
                           (title, header, link))

    conn.commit()
    conn.close()
    print("Limited data inserted into the database.")


def fetch_and_save_data():
    """Fetches stored data from SQLite and saves output to page_db.txt."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM wiki_data")
    data = cursor.fetchall()

    conn.close()

    with open("page_db.txt", "w", encoding="utf-8") as file:
        for row in data:
            file.write(f"{row}\n")

    print("Stored data retrieved and saved to page_db.txt.")


create_database()

# Scrape Wikipedia and store data
wiki_url = "https://en.wikipedia.org/wiki/Module:Yesno"
scrape_wikipedia(wiki_url)

fetch_and_save_data()
