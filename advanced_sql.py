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

# Task 3: An Insert Transaction Based on Data
# Insert a new order for 'Perez and Sons' with the 5 least expensive products
def insert_order():
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Get customer_id for 'Perez and Sons'
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
        customer_id = cursor.fetchone()[0]

        # Get employee_id for 'Miranda Harris'
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
        employee_id = cursor.fetchone()[0]

        # Get product_ids of 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Insert new order and retrieve order_id
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id;
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]

        # Insert line items for the order
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, 10)
            """, (order_id, product_id))

        conn.commit()
        print(f"New order {order_id} created successfully.")

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
# Task 3
def fetch_new_order_details():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT l.line_item_id, l.quantity, p.product_name
            FROM line_items l
            JOIN products p ON l.product_id = p.product_id
            WHERE l.order_id = (SELECT MAX(order_id) FROM orders)
        """)
        results = cursor.fetchall()
        print("\nNew Order Line Items:")
        for row in results:
            print(row)

if __name__ == "__main__":
    insert_order()
    fetch_data()
    fetch_new_order_details()
