"""
Student Management System

This module handles user authentication, 
including registration and login.
"""
import hashlib
import json

from logger import logger

from validation import (
    get_login_credentials,
)

USERS_FILE = "users.json"


def load_users():
    """Load all registered users from the JSON file."""

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    except FileNotFoundError:
        logger.warning("users.json not found. Creating a new user database.")
        return []

    except json.JSONDecodeError:
        logger.error("users.json is corrupted.")
        return []

    except OSError as e:
        logger.error(f"Failed to read users.json | {e}")
        return []


def save_users(users):
    """Save all registered users to the JSON file."""

    try:
        with open(USERS_FILE, "w", encoding="utf-8") as json_file:
            json.dump(users, json_file, indent=4)

    except OSError as e:
        logger.error(f"Failed to save users.json | {e}")


def hash_password(password):
    """
    Hash a password using SHA-256.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hashed password.
    """

    return hashlib.sha256(password.encode()).hexdigest()


def login():
    """Authenticate the administrator."""

    users = load_users()

    print("\nLogin")
    print("-" * 50)

    username, password = get_login_credentials()

    hashed_password = hash_password(password)

    if not users:
        logger.error("No administrator account found.")
        print("\n❌ No administrator account found.")
        return None

    admin = users[0]

    if (
        admin["username"] == username
        and admin["password"] == hashed_password
    ):
        logger.info(f"User Logged In | Username={username}")
        print("\n✅ Login Successful!")

        return username

    logger.warning(f"Failed Login Attempt | Username={username}")
    print("\n❌ Invalid username or password.")

    return None