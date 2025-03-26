# soup_scrape.py

# Task 2: Extracting Elements with BeautifulSoup
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Web_scraping"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

bold_texts = [b.get_text() for b in soup.find_all("b")]

images = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]

with open("soup_scrape.txt", "w", encoding="utf-8") as file:
    file.write("List of Bold Text:\n")
    file.write("\n".join(bold_texts))
    file.write("\n\nList of Image Sources:\n")
    file.write("\n".join(images))

print("Extraction complete. Results saved in soup_scrape.txt")
