# sql_intro.py

#Task 1
import sqlite3
import os

#Task 1: Create a New SQLite Database

def create_database():
    db_path = './db/new.db'

    if os.path.exists(db_path):
        print("Database already exists.")
        return

    try:
        # Connect to the SQLite database (creates a new one if it doesn't exist)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print("Database created and connected successfully.")

# Task 2: Define Database Structure

        # Create Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                major TEXT
            )
        ''')

        # Create Courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Courses (
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                instructor_name TEXT NOT NULL
            )
        ''')

        # Create Enrollments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES Students(student_id),
                FOREIGN KEY (course_id) REFERENCES Courses(course_id)
            )
        ''')

        conn.commit()
        print("Tables created successfully.")

# Task 4: Populate Tables with Data (Task 3 is not present in the Lesson's 7 Assignment!)

        # Insert sample data
        cursor.executemany('''
                    INSERT INTO Students (name, age, major) VALUES (?, ?, ?)
                ''', [
            ('Alice Johnson', 20, 'Computer Science'),
            ('Bob Smith', 22, 'Mathematics'),
            ('Charlie Brown', 19, 'Physics')
        ])

        cursor.executemany('''
                    INSERT INTO Courses (course_name, instructor_name) VALUES (?, ?)
                ''', [
            ('Calculus', 'Dr. Adams'),
            ('Physics', 'Dr. Baker'),
            ('Computer Science', 'Dr. Clark')
        ])

        cursor.executemany('''
                    INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)
                ''', [
            (1, 1),
            (2, 2),
            (3, 3),
            (1, 3)
        ])

        conn.commit()
        print("Sample data inserted successfully.")

# Task 5: QWrite SQL Queries
        # Execute queries and print results
        print("\nAll Students:")
        cursor.execute("SELECT * FROM Students")
        for row in cursor.fetchall():
            print(row)

        print("\nCourses taught by Dr. Baker:")
        cursor.execute("SELECT * FROM Courses WHERE instructor_name = ?", ('Dr. Baker',))
        for row in cursor.fetchall():
            print(row)

        print("\nStudent Enrollments with Course Names:")
        cursor.execute('''
                    SELECT Students.name, Courses.course_name 
                    FROM Enrollments 
                    JOIN Students ON Enrollments.student_id = Students.student_id 
                    JOIN Courses ON Enrollments.course_id = Courses.course_id
                ''')
        for row in cursor.fetchall():
            print(row)

        print("\nStudents Ordered by Age:")
        cursor.execute("SELECT * FROM Students ORDER BY age")
        for row in cursor.fetchall():
            print(row)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    create_database()
