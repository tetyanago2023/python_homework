# assignment2.py

import csv
import sys

#Task 2
def read_employees():
    """Reads employee data from a CSV file and returns a dictionary
        with 'fields' as column headers and 'rows' as employee data."""
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

# Task 4
def first_name(row_number):
    """Returns the first name from the given row number in employees["rows"]."""
    first_name_index = column_index("first_name")
    return employees["rows"][row_number][first_name_index]

# Task 5
def employee_find(employee_id):
    """Finds and returns rows with the matching employee_id."""

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    """Finds and returns rows with the matching employee_id using a lambda function."""
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    """Sorts employees["rows"] by last_name column using a lambda function."""
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

# Task 8
def employee_dict(row):
    """Creates a dictionary for an employee from a given row, excluding employee_id."""
    field_names = employees["fields"][1:]  # Skip employee_id
    employee_data = row[1:]  # Skip employee_id value
    return dict(zip(field_names, employee_data))

# Task 9
def all_employees_dict():
    """Creates a dictionary of all employees with employee_id as keys and employee_dict as values."""
    return {row[0]: employee_dict(row) for row in employees["rows"]}

# Call the function and store the result in a global variable
employees = read_employees()
print(employees)

# Store the column index for employee_id
employee_id_column = column_index("employee_id")

# Test Task 8
print(employee_dict(employees["rows"][0]))

# Test Task 9
print(all_employees_dict())
