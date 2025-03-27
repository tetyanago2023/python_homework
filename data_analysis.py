# data_analysis.py

# Task 4: Data Retrieval and Analysis with Pandas
import sqlite3
import pandas as pd
from collections import Counter

DB_PATH = "db/scraped_data.db"

def load_data():
    """Loads data from SQLite into a Pandas DataFrame."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM wiki_data", conn)
    conn.close()
    return df

def analyze_data(df):
    """Performs analysis on the scraped data."""
    header_count = df["header"].nunique()
    link_count = df["link"].nunique()

    most_common_header = Counter(df["header"]).most_common(1)
    most_common_link = Counter(df["link"]).most_common(1)

    summary = (
        f"Data Analysis Report:\n"
        f"----------------------\n"
        f"Total unique headers: {header_count}\n"
        f"Total unique links: {link_count}\n"
        f"Most common header: {most_common_header[0] if most_common_header else 'No headers'}\n"
        f"Most common link: {most_common_link[0] if most_common_link else 'No links'}\n"
    )

    with open("assignment10.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    print("Analysis complete. Results saved to assignment10.txt.")

# Load data from database
df = load_data()

# Perform analysis
analyze_data(df)
