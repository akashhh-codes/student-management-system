"""
Student Management System

This is the main entry point of the application.
It displays the menu and routes user requests
to the appropriate CRUD operations.
"""

from logger import logger
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    export_to_csv,
    import_from_csv,
)

from auth import login


def display_auth_menu():
    """Display the authentication menu."""

    print("\n" + "=" * 40)
    print("        ADMIN LOGIN")
    print("=" * 40)
    print("1. Login")
    print("2. Exit")


def display_student_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("    STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Export to CSV")
    print("7. Import from CSV")
    print("8. Logout")


# Authentication and Main Menu Loop
while True:

    display_auth_menu()

    choice = input("\nEnter your choice (1-2): ")

    if choice == "1":

        logged_in_user = login()

        if logged_in_user:

            print(f"\n✅ Welcome, {logged_in_user}!")

            while True:

                display_student_menu()

                choice = input("\nEnter your choice (1-8): ")

                if choice == "1":
                    add_student()

                elif choice == "2":
                    view_students()

                elif choice == "3":
                    search_student()

                elif choice == "4":
                    update_student()

                elif choice == "5":
                    delete_student()

                elif choice == "6":
                    export_to_csv()

                elif choice == "7":
                    import_from_csv()

                elif choice == "8":
                    logger.info(f"User Logged Out | Username={logged_in_user}")

                    print("\n✅ Logged out successfully.")

                    break

                else:
                    print("\n❌ Invalid choice! Please enter a number between 1 and 8.")

    elif choice == "2":

        print("\nThank you for using Student Management System!")
        print("Developed by Akash Chauhan.")
        break

    else:

        print("\n❌ Invalid choice! Please enter 1 or 2.")