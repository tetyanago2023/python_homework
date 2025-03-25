# sql_intro_2.py

# Task 6: Read Data into a DataFrame

import sqlite3
import pandas as pd

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Create Customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL
    )
''')

# Create Orders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product_name TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
''')

# Insert sample data into Customers
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
cursor.executemany("INSERT INTO Customers (customer_name) VALUES (?)", [(c,) for c in customers])

# Insert sample data into Orders
orders = [
    (1, "Laptop"), (1, "Phone"), (2, "Tablet"), (2, "Laptop"),
    (3, "Monitor"), (1, "Laptop"), (2, "Laptop"), (3, "Tablet"),
    (1, "Phone"), (3, "Monitor"), (2, "Tablet"), (1, "Laptop"),
    (4, "Keyboard"), (4, "Mouse"), (4, "Laptop"), (5, "Tablet"),
    (5, "Phone"), (5, "Monitor"), (4, "Monitor"), (5, "Laptop"),
    (3, "Phone"), (2, "Mouse"), (1, "Keyboard"), (5, "Laptop"),
    (4, "Phone"), (3, "Mouse"), (2, "Monitor"), (5, "Keyboard"),
    (4, "Tablet"), (3, "Laptop"), (2, "Keyboard"), (1, "Tablet")
]
cursor.executemany("INSERT INTO Orders (customer_id, product_name) VALUES (?, ?)", orders)

# Commit changes
conn.commit()

# Read data into a DataFrame
query = '''
    SELECT o.order_id, c.customer_name, o.product_name
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
'''
df = pd.read_sql_query(query, conn)

# Group by customer_name and product_name, then count occurrences
grouped_df = df.groupby(["customer_name", "product_name"]).size().reset_index(name="order_count")

# Print the grouped DataFrame
print("Grouped DataFrame:")
print(grouped_df)

# Sort by order_id
sorted_df = df.sort_values(by=["order_id"], ascending=True)

# Print the last 20 rows
print("Sorted DataFrame, last 20 rows:")
print(sorted_df.tail(20))

# Close connection
conn.close()
