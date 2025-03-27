# store_page.py

# Task 1: Storing Data in JSON
import requests
import json
from bs4 import BeautifulSoup


def scrape_wikipedia(url):
    """Scrapes a Wikipedia page and stores title, headers, and links in JSON."""

    # Fetch the page content
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the title
    title = soup.find("h1").get_text(strip=True)

    # Extract all headers (h2, h3, h4)
    headers = [header.get_text(strip=True) for header in soup.find_all(["h2", "h3", "h4"])]

    # Extract all links
    links = {a.get_text(strip=True): a["href"] for a in soup.find_all("a", href=True) if a.get_text(strip=True)}

    # Store data in a dictionary
    page_data = {
        "title": title,
        "headers": headers,
        "links": links
    }

    # Save data to a JSON file
    with open("page.json", "w", encoding="utf-8") as file:
        json.dump(page_data, file, indent=4, ensure_ascii=False)

    print("Scraped data saved to page.json.")


# Wikipedia page of choice
wiki_url = "https://en.wikipedia.org/wiki/Wikipedia:Dashboard"
scrape_wikipedia(wiki_url)
