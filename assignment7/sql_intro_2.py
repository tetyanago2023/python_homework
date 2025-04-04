# sql_intro_2.py

# Task 6: Read Data into a DataFrame

import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query to join line_items and products
query = """
SELECT 
    line_items.line_item_id, 
    line_items.quantity, 
    line_items.product_id, 
    products.product_name, 
    products.price
FROM 
    line_items
JOIN 
    products
ON 
    line_items.product_id = products.product_id
"""

# Load data into DataFrame
df = pd.read_sql_query(query, conn)

# Print first 5 rows
print("Initial DataFrame:")
print(df.head())

# Add 'total' column
df['total'] = df['quantity'] * df['price']

# Print updated DataFrame
print("\nDataFrame with 'total' column:")
print(df.head())

# Group by product_id and aggregate
summary_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})

# Print grouped DataFrame
print("\nDataFrame grouped by product_id and aggregated")
print(summary_df.head())

# Rename columns for clarity
summary_df.rename(columns={
    'line_item_id': 'order_count',
    'total': 'total_cost'
}, inplace=True)

# Sort by product_name
summary_df.sort_values('product_name', inplace=True)

# Print final summary
print("\nGrouped and sorted summary:")
print(summary_df.head())

# Save to CSV
df.to_csv("order_summary.csv", index=False, float_format='%.2f')

# Close connection
conn.close()
