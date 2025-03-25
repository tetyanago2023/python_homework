# advanced_sql.py

import sqlite3

db_path = "./db/lesson.db"

# Task 1
# Query to fetch the first 5 orders and their line items
query = """
    SELECT o.order_id, l.line_item_id, p.product_name
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    WHERE o.order_id IN (
        SELECT order_id
        FROM orders
        ORDER BY order_id
        LIMIT 5
    )
    ORDER BY o.order_id, l.line_item_id;
"""

def fetch_data():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

if __name__ == "__main__":
    fetch_data()
