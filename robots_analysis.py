# robots_analysis.py

# Task 3: Ethical Web Scraping
import requests

URL = "https://en.wikipedia.org/robots.txt"

response = requests.get(URL)

robots_text = response.text

restricted_sections = []
user_agent_rules = {}

# Parse the robots.txt file
lines = robots_text.split("\n")
current_agent = None

for line in lines:
    line = line.strip()
    if line.startswith("User-agent:"):
        current_agent = line.split(": ")[1]
        user_agent_rules[current_agent] = []
    elif line.startswith("Disallow:") and current_agent:
        disallowed_path = line.split(": ")[1] if len(line.split(": ")) > 1 else ""
        user_agent_rules[current_agent].append(disallowed_path)
        restricted_sections.append(disallowed_path)

with open("ethical_scraping.txt", "w", encoding="utf-8") as file:
    file.write("Restricted Sections for Crawling:\n")
    file.write("\n".join(set(restricted_sections)))

    file.write("\n\nUser Agent Specific Rules:\n")
    for agent, rules in user_agent_rules.items():
        file.write(f"\n{agent}:\n")
        file.write("\n".join(rules))

    file.write("\n\nPurpose of robots.txt and Ethical Scraping:\n")
    file.write("The robots.txt file is used by websites to define rules for web crawlers, "
               "restricting access to certain parts of the site. This prevents server overload, "
               "protects sensitive information, and ensures ethical data scraping practices. "
               "By respecting these rules, web scrapers can operate legally and responsibly, "
               "without violating a site's terms of service.\n")

print("Analysis complete. Results saved in ethical_scraping.txt")
