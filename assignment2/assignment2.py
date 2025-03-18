# assignment2.py

import csv
import sys

#Task 2
def read_employees():
    employees_data = {"fields": [], "rows": []}
    file_path = "../csv/employees.csv"

    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_data["fields"] = row  # Store headers
                    if len(row) < 4:
                        print("Error: Expected at least 4 fields in the CSV header.")
                        sys.exit(1)
                else:
                    employees_data["rows"].append(row)  # Store rows
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return employees_data

# Task 3: Find Column Index
def column_index(column_name):
    """Returns the index of the requested column name in employees['fields']."""
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Error: Column '{column_name}' not found in the CSV file.")
        sys.exit(1)

# Call the function and store the result in a global variable
employees = read_employees()
# Store employee_id column index globally
employee_id_column = column_index("employee_id")

print(employees)
