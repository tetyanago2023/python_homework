# see_also.py

#Task 4: Scraping Structured Data
import requests
from bs4 import BeautifulSoup


def extract_see_also(url):
    """Extracts the 'See also' section from a Wikipedia page."""

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    see_also_header = soup.find(id="See_also")
    if not see_also_header:
        print("No 'See also' section found.")
        return

    see_also_list = see_also_header.find_next("ul")

    if not see_also_list:
        print("No list items found under 'See also'.")
        return

    see_also_links = [li.get_text(strip=True) for li in see_also_list.find_all("li")]

    output_text = "Extracted 'See also' Section:\n"
    output_text += "\n".join(see_also_links)

    with open("see_also.txt", "w", encoding="utf-8") as file:
        file.write(output_text)

    print(output_text)
    print("\nExtraction completed. Results saved in see_also.txt.")


# Wikipedia page of choice
wiki_url = "https://en.wikipedia.org/wiki/Web_scraping"
extract_see_also(wiki_url)
