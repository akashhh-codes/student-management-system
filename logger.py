"""
Student Management System

This module configures the application's logging settings
and provides a reusable logger instance.
"""
import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)