# assignment3.py

import pandas as pd

# Task 1.1
data = {
    "Name": ["Alice", "Bob", "charlie"],  # Ensure 'charlie' is lowercase in order to follow test-file content re 'charlie'
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

# Task 1.2
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

# Task 1.3
task1_older = task1_with_salary.copy()
task1_older["Age"] += 1

# Task 1.4
task1_older.to_csv("employees.csv", index=False)

print(task1_data_frame)
print(task1_with_salary)
print(task1_older)

