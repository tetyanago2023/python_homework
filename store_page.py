# store_page.py

# Task 1: Storing Data in JSON
import requests
import json
import csv
from bs4 import BeautifulSoup


def scrape_wikipedia(url):
    """Scrapes a Wikipedia page and stores title, headers, and links in JSON."""

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").get_text(strip=True)

    headers = [header.get_text(strip=True) for header in soup.find_all(["h2", "h3", "h4"])]

    links = {a.get_text(strip=True): a["href"] for a in soup.find_all("a", href=True) if a.get_text(strip=True)}

    page_data = {
        "title": title,
        "headers": headers,
        "links": links
    }

    with open("page.json", "w", encoding="utf-8") as file:
        json.dump(page_data, file, indent=4, ensure_ascii=False)

    print("Scraped data saved to page.json.")

    # Task 2: Storing Data in CSV
    images = [img["src"] for img in soup.find_all("img", src=True)]

    with open("images.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Image Source"])

        for img_src in images:
            writer.writerow([img_src])

    print("Image sources saved to images.csv.")

wiki_url = "https://en.wikipedia.org/wiki/Wikipedia:Dashboard"
scrape_wikipedia(wiki_url)
