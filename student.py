"""
Student Management System

This module contains all CRUD operations related to student records,
including adding, viewing, searching, updating, deleting, and
exporting student data.
"""

import csv
import os

from database import load_students, save_students
from logger import logger
from validation import (
    student_exists,
    get_valid_student_id,
    get_valid_name,
    get_valid_age,
    get_valid_course,
    get_valid_marks,
    get_valid_phone,
    get_valid_email,
    get_search_student_id
)


def find_student_by_id(student_id, students):
    """
    Search for a student by ID.

    Returns:
        dict: Student record if found.
        None: If no matching student exists.
    """
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def display_student(student):
    """Display a student's details in a formatted layout."""

    print(f"ID      : {student['id']}")
    print(f"Name    : {student['name']}")
    print(f"Age     : {student['age']}")
    print(f"Course  : {student['course']}")
    print(f"Marks   : {student['marks']}")
    print(f"Phone   : {student['phone']}")
    print(f"Email   : {student['email']}")
    print("-" * 50)

# --------------------------
# CRUD Functions
# --------------------------

def add_student():
    """Add a new student after validating all input fields."""
    students = load_students()
    student_id = get_valid_student_id(students)

    name = get_valid_name()
    age = get_valid_age()
    course = get_valid_course()
    marks = get_valid_marks()
    phone = get_valid_phone()
    email = get_valid_email()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "phone": phone,
        "email": email
    }

    students.append(student)
    save_students(students)

    logger.info(f"Student Added | ID={student_id} | Name={name}")

    print(f"\n✅ Student '{name}' added successfully.")


def view_students():
    """Display all student records stored in the database."""
    students = load_students()

    if not students:
        logger.warning("View Students | No student records found.")

        print("\nNo student records found.")
        return

    logger.info(f"Viewed All Students | Total Records={len(students)}")
    print("\n" + "=" * 50)
    print("           ALL STUDENT RECORDS")
    print("=" * 50)

    for student in students:
        display_student(student) 


def search_student():
    """Search and display a student using their Student ID."""
    students = load_students()
    student_id = get_search_student_id()
    student = find_student_by_id(student_id, students)

    if student:
        logger.info(f"Student Searched | ID={student_id} | Found")

        print("\nStudent Found")
        print("-" * 50)
        display_student(student)
    else:

        logger.warning(f"Student Search Failed | ID={student_id}")

        print("\n❌ Student not found.")


def update_student():
    """Update one or more fields of an existing student."""
    students = load_students()
    student_id = get_search_student_id()
    student = find_student_by_id(student_id, students)

    if not student:
        logger.warning(f"Student Update Failed | ID={student_id}")

        print("\n❌ Student not found.")
        return
    
    logger.info(f"Student Update Started | ID={student_id}")

    print("\nCurrent Student Details")
    print("-" * 50)

    display_student(student)

    while True:
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Course")
        print("4. Marks")
        print("5. Phone")
        print("6. Email")
        print("7. Update Everything")
        print("8. Cancel")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            student["name"] = get_valid_name()

        elif choice == "2":
            student["age"] = get_valid_age()

        elif choice == "3":
            student["course"] = get_valid_course()

        elif choice == "4":
            student["marks"] = get_valid_marks()

        elif choice == "5":
            student["phone"] = get_valid_phone()

        elif choice == "6":
            student["email"] = get_valid_email()

        elif choice == "7":
            student["name"] = get_valid_name()
            student["age"] = get_valid_age()
            student["course"] = get_valid_course()
            student["marks"] = get_valid_marks()
            student["phone"] = get_valid_phone()
            student["email"] = get_valid_email()

        elif choice == "8":
            logger.info(f"Student Update Cancelled | ID={student_id}")

            print("\nUpdate cancelled.")
            return

        else:
            print("\n❌ Invalid choice.")
            continue

        print("\nUpdated Student Details")
        print("-" * 50)

        display_student(student)

        # Keep asking until the user enters a valid Y/N response.
        while True:
            another = input("\nDo you want to update another field? (Y/N): ").strip().upper()

            if another == "Y":
                break

            elif another == "N":
                save_students(students)

                logger.info(f"Student Updated | ID={student_id}")

                print("\n✅ Student updated successfully.")

                return

            else:
                print("❌ Please enter Y or N.")


def delete_student():
    """Delete a student record after user confirmation."""
    students = load_students()
    student_id = get_search_student_id()
    student = find_student_by_id(student_id, students)

    if not student: 
        logger.warning(f"Student Delete Failed | ID={student_id}")

        print("\n❌ Student not found.")
        return

    logger.info(f"Student Delete Started | ID={student_id}")

    print("\nStudent Found")
    print("-" * 50)
    
    display_student(student)

    choice = input("Are you sure you want to delete this student? (Y/N): ").strip().upper()

    if choice == "Y":
        students.remove(student)
        save_students(students)

        logger.info(f"Student Deleted | ID={student_id}")

        print("\n✅ Student deleted successfully.")
    else:

        logger.info(f"Student Deletion Cancelled | ID={student_id}")

        print("\nDeletion cancelled.")


def export_to_csv():
    """Export all student records to a CSV file."""
    students = load_students()

    if not students:
        logger.warning("CSV Export Failed | No student records found.")

        print("\n❌ No student records found.")
        return
    
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        
        fieldnames = [
            "id",
            "name",
            "age",
            "course",
            "marks",
            "phone",
            "email",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(students)

    logger.info(f"Student Records Exported to CSV | Total Records={len(students)}")

    print("\n✅ Student records exported successfully to 'students.csv'.")


def import_from_csv():
    """Import student records from a CSV file."""

    print("\nImport Student Records")
    print("-" * 50)

    csv_file_path = input("Enter CSV file path: ").strip()

    if not os.path.isfile(csv_file_path):
        logger.warning(f"CSV Import Failed | File Not Found | {csv_file_path}")
        print("\n❌ CSV file not found.")
        return

    students = load_students()

    imported_count = 0
    skipped_count = 0

    required_fields = [
        "id",
        "name",
        "age",
        "course",
        "marks",
        "phone",
        "email"
    ]

    try:
        with open(csv_file_path, "r", newline="", encoding="utf-8") as csv_file:

            reader = csv.DictReader(csv_file)

            if reader.fieldnames is None or set(reader.fieldnames) != set(required_fields):
                logger.error(f"CSV Import Failed | Invalid CSV Format | File={csv_file_path}")

                print("\n❌ Invalid CSV format.")
                print("Required columns are:")
                print(", ".join(required_fields))
                return

            for row in reader:

                student = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "age": int(row["age"]),
                    "course": row["course"],
                    "marks": float(row["marks"]),
                    "phone": row["phone"],
                    "email": row["email"]
                }

                if student_exists(student["id"], students):
                    skipped_count += 1
                    continue

                students.append(student)
                imported_count += 1

        save_students(students)

        logger.info(f"CSV Imported | File={csv_file_path} | Imported={imported_count} | Skipped={skipped_count}")

        print("\n✅ CSV Import Completed")
        print("-" * 50)
        print(f"Imported Records : {imported_count}")
        print(f"Skipped Records  : {skipped_count}")

        if imported_count == 0 and skipped_count > 0:
            print("\nℹ️ All records already exist in the database.")

    except (ValueError, KeyError, csv.Error, OSError) as e:
        logger.error(f"CSV Import Failed | {e}")

        print("\n❌ Failed to import CSV file.")