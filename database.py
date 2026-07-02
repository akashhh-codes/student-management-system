"""
Student Management System

This module handles reading and writing student records
to the JSON database.
"""

import json

from logger import logger

FILE_NAME = "students.json"


def load_students():
    """Load and return all student records from the JSON database."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        logger.warning(f"{FILE_NAME} not found. Creating a new database.")
        return []

    except json.JSONDecodeError:
        logger.error(f"{FILE_NAME} contains invalid JSON.")
        return []

    except OSError as e:
        logger.error(f"Error reading {FILE_NAME}: {e}")
        return []


def save_students(students):
    """Save all student records to the JSON database."""

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

    except OSError as e:
        logger.error(f"Error saving {FILE_NAME}: {e}")
        print("\n❌ Unable to save student records.")