# task5_storage.py

# Task 5: Optimizing Data Storage - SQLite vs. MongoDB

file_path = "assignment10.txt"

# Open the file in append mode and write the comparison data
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n" + "-"*38 + "\nTask 5: Optimizing Data Storage\n" + "-"*38 + "\n")

    # Adding the comparison table
    file.write("\nComparison: SQLite vs. MongoDB\n\n")
    file.write("| Feature              | SQLite (Relational)                          | MongoDB (Non-Relational)               |\n")
    file.write("|----------------------|--------------------------------|--------------------------------|\n")
    file.write("| **Data Structure**   | Tables with rows and columns (structured schema) | Collections of documents (flexible schema) |\n")
    file.write("| **Storage Type**     | Disk-based, single-file database | Distributed, document-based storage |\n")
    file.write("| **Scalability**      | Limited scalability (local storage) | High scalability (distributed systems) |\n")
    file.write("| **Performance**      | Fast for small datasets | Better for handling large-scale data |\n")
    file.write("| **Complex Queries**  | Supports SQL queries and joins | Uses flexible JSON-like queries |\n")
    file.write("| **Transactions**     | ACID-compliant, supports transactions | Supports atomic operations, but not full ACID compliance |\n")
    file.write("| **Ease of Use**      | Lightweight, easy to set up | Requires database server setup |\n")
    file.write("| **Best Use Case**    | Small-scale projects, prototyping, offline apps | Large-scale applications, big data, real-time analytics |\n")

    # Adding explanation and recommendations
    file.write("\n--------------------------------------\n")
    file.write("Comparison: SQLite vs. MongoDB\n\n")
    file.write("- SQLite is a lightweight relational database that stores data in structured tables. It is easy to use and works well for small-scale projects.\n")
    file.write("- MongoDB is a NoSQL database that stores data in flexible JSON-like documents. It scales better for large-scale applications.\n\n")
    file.write("Recommendations:\n")
    file.write("- For small-scale Wikipedia scraping: SQLite is sufficient due to its simplicity and efficiency.\n")
    file.write("- For large-scale scraping with millions of records: MongoDB is preferred due to its scalability and distributed nature.\n")

print("Task 5 data has been successfully added to assignment10.txt")
