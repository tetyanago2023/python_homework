# sql_intro.py

import sqlite3
import os

# Task 1: Create a New SQLite Database
db_path = "../db/magazines.db"

os.makedirs(os.path.dirname(db_path), exist_ok=True)


def connect_db():
    """Connect to the database and enable foreign key constraints."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = 1")  # Ensure foreign keys are enforced
    return conn

# Task 2: Define Database Structure
def create_tables(conn):
    """Create database tables if they do not exist."""
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id) ON DELETE CASCADE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id) ON DELETE CASCADE,
            FOREIGN KEY (magazine_id) REFERENCES magazines(id) ON DELETE CASCADE,
            UNIQUE (subscriber_id, magazine_id)  
        );
    """)

    conn.commit()
    print("Database tables ensured.")

# Task 4: Populate Tables with Data
def insert_publisher(conn, name):
    """Insert a publisher if it doesn't already exist."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Added publisher: {name}")
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")


def insert_magazine(conn, name, publisher_name):
    """Insert a magazine if it doesn't already exist, ensuring publisher exists."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (publisher_name,))
        publisher = cursor.fetchone()
        if not publisher:
            print(f"Publisher '{publisher_name}' not found. Cannot add magazine '{name}'.")
            return

        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher[0]))
        conn.commit()
        print(f"Added magazine: {name}")
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists.")


def insert_subscriber(conn, name, address):
    """Insert a subscriber only if (name, address) does not already exist."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
            return

        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
        print(f"Added subscriber: {name}, {address}")

    except sqlite3.Error as e:
        print(f"Error inserting subscriber: {e}")

def insert_subscription(conn, subscriber_name, subscriber_address, magazine_name, expiration_date):
    """Insert a subscription if it doesn't already exist."""
    try:
        cursor = conn.cursor()

        # Get subscriber ID
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?",
                       (subscriber_name, subscriber_address))
        subscriber = cursor.fetchone()
        if not subscriber:
            print(f"Subscriber '{subscriber_name}' at '{subscriber_address}' not found.")
            return

        # Get magazine ID
        cursor.execute("SELECT id FROM magazines WHERE name = ?", (magazine_name,))
        magazine = cursor.fetchone()
        if not magazine:
            print(f"Magazine '{magazine_name}' not found.")
            return

        # Insert subscription
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                       (subscriber[0], magazine[0], expiration_date))
        conn.commit()
        print(f"Added subscription: {subscriber_name} → {magazine_name} (Expires: {expiration_date})")

    except sqlite3.IntegrityError:
        print(f"Subscription for '{subscriber_name}' to '{magazine_name}' already exists.")

# Task 5: Write SQL Queries

def get_all_subscribers(conn):
    """Retrieve and print all subscribers."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subscribers;")
        rows = cursor.fetchall()
        print("\nAll Subscribers:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error retrieving subscribers: {e}")

def get_all_magazines_sorted(conn):
    """Retrieve and print all magazines sorted by name."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines ORDER BY name;")
        rows = cursor.fetchall()
        print("\nAll Magazines (Sorted by Name):")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error retrieving magazines: {e}")

def get_magazines_by_publisher(conn, publisher_name):
    """Retrieve and print magazines for a given publisher."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT magazines.id, magazines.name, publishers.name AS publisher
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.id
            WHERE publishers.name = ?;
        """, (publisher_name,))
        rows = cursor.fetchall()
        print(f"\nMagazines published by '{publisher_name}':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error retrieving magazines for publisher '{publisher_name}': {e}")


# Main script execution
try:
    conn = connect_db()
    create_tables(conn)

    # Insert sample publishers
    insert_publisher(conn, "Tech Media")
    insert_publisher(conn, "Science Today")
    insert_publisher(conn, "Health Weekly")

    # Insert sample magazines
    insert_magazine(conn, "AI Monthly", "Tech Media")
    insert_magazine(conn, "Space Exploration", "Science Today")
    insert_magazine(conn, "Healthy Living", "Health Weekly")

    # Insert sample subscribers
    insert_subscriber(conn, "Alice Johnson", "123 Maple St")
    insert_subscriber(conn, "Bob Smith", "456 Oak St")
    insert_subscriber(conn, "Charlie Davis", "789 Pine St")

    # Insert sample subscriptions
    insert_subscription(conn, "Alice Johnson", "123 Maple St", "AI Monthly", "2025-12-31")
    insert_subscription(conn, "Bob Smith", "456 Oak St", "Space Exploration", "2025-11-15")
    insert_subscription(conn, "Charlie Davis", "789 Pine St", "Healthy Living", "2025-10-01")

    # Run queries and print results
    get_all_subscribers(conn)
    get_all_magazines_sorted(conn)
    get_magazines_by_publisher(conn, "Tech Media")  # Change publisher name if needed

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    if conn:
        conn.close()
        print("Database connection closed.")
