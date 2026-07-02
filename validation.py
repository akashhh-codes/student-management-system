"""
Student Management System

This module contains reusable input validation functions
used throughout the application.
"""
def student_exists(student_id, students):
    """
    Check whether a student ID already exists.

    Returns:
        bool: True if the student ID exists, otherwise False.
    """

    for student in students:
        if student["id"] == student_id:
            return True
    return False


def get_valid_student_id(students):
    """Validate numeric Student ID."""
    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_exists(student_id, students):
                print("❌ Student ID already exists. Please enter a different ID.\n")
            else:
                return student_id

        except ValueError:
            print("❌ Please enter a valid numeric Student ID.\n")


def get_valid_name():
    """Validate the student's name."""
    while True:
        name = input("Enter Name: ").strip()

        if name == "":
            print("❌ Name cannot be empty.\n")
        else:
            return name
        

def get_valid_age():
    """Validate that the student's age is between 2 and 90."""
    while True:
        try:
            age = int(input("Enter Age: "))

            if 2 <= age <= 90:
                return age

            print("❌ Age must be between 02 and 90.\n")

        except ValueError:
            print("❌ Please enter a valid age.\n")


def get_valid_course():
    """Validate the course name."""
    while True:
        course = input("Enter Course: ").strip()

        if course == "":
            print("❌ Course name cannot be empty.\n")
        else:
            return course


def get_valid_marks():
    """Validate Marks."""
    while True:
        try:
            marks = float(input("Enter Marks: "))

            if 0 <= marks <= 100:
                return marks

            print("❌ Marks must be between 0 and 100.\n")

        except ValueError:
            print("❌ Please enter valid marks.\n")


def get_valid_phone():
    """Validate Indian mobile number."""

    while True:
        phone = input("Enter Phone Number: ").strip()

        if not phone.isdigit():
            print("❌ Phone number should contain only digits.\n")
            continue

        if len(phone) != 10:
            print("❌ Phone number must contain exactly 10 digits.\n")
            continue

        if phone[0] not in "6789":
            print("❌ Indian mobile numbers must start with 6, 7, 8 or 9.\n")
            continue

        return phone
    

def get_valid_email():
    """Validate the email address."""
    while True:
        email = input("Enter Email: ").strip()

        if "@" in email and "." in email:
            return email

        print("❌ Enter a valid email address.\n")
    

def get_login_credentials():
    """
    Get login credentials from the user.

    Returns:
        tuple: (username, password)
    """

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ")

    return username, password


def get_search_student_id():
    """Get a valid Student ID for search, update, or delete operations."""
    while True:
        try:
            student_id = int(input("Enter Student ID: "))
            return student_id

        except ValueError:
            print("❌ Please enter a valid numeric Student ID.\n")