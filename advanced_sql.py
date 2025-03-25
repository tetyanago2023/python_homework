# advanced_sql.py

import sqlite3

db_path = "./db/lesson.db"

# Task 1: Understanding Subqueries
# Query 1: Retrieve order details for the first 5 orders
query1 = """
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
# Task 2: Complex JOINs with Aggregation
# Query 2: Retrieve the total price of the first 5 orders
query2 = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
"""


def fetch_data():
    # Task 1
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query1)
        results = cursor.fetchall()
        print("Order Details:")
        for row in results:
            print(row)

    # Task 2
        cursor.execute(query2)
        results = cursor.fetchall()
        print("\nTotal Price of First 5 Orders:")
        for row in results:
            print(row)


if __name__ == "__main__":
    fetch_data()
