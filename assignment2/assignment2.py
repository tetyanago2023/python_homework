# assignment2.py

import csv
import sys
import os
import custom_module


# Task 2
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


# Task 3
def column_index(column_name):
    """Returns the index of the given column name in employees["fields"]."""
    return employees["fields"].index(column_name)


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


# Task 10
def get_this_value():
    """Returns the value of the THISVALUE environment variable."""
    return os.getenv("THISVALUE")

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Task 12
def read_minutes():
    """Reads minutes1.csv and minutes2.csv and returns two dictionaries with data stored as tuples."""

    def read_csv(file_path):
        minutes_data = {"fields": [], "rows": []}
        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for index, row in enumerate(reader):
                    if index == 0:
                        minutes_data["fields"] = row  # Store headers
                    else:
                        minutes_data["rows"].append(tuple(row))  # Store rows as tuples
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            sys.exit(1)
        return minutes_data

    minutes1 = read_csv("../csv/minutes1.csv")
    minutes2 = read_csv("../csv/minutes2.csv")
    return minutes1, minutes2

# Task 13
def create_minutes_set():
    """Creates a set containing unique rows from minutes1 and minutes2."""
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

# Call the function and store the result in a global variable
employees = read_employees()
print(employees)

# Store the column index for employee_id
employee_id_column = column_index("employee_id")

# Test Task 8
print(employee_dict(employees["rows"][0]))

# Test Task 9
print(all_employees_dict())

# Test Task 10
print(get_this_value())

# Test Task 11
set_that_secret("abracadabra")
print(custom_module.secret)  # Should print "abracadabra"

# Test Task 12
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Test Task 13
minutes_set = create_minutes_set()
print(minutes_set)
