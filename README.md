# 🎓 Student Management System

A command-line based Student Management System developed in Python.

This project demonstrates CRUD operations, JSON & CSV file handling, logging, authentication, input validation, exception handling, and modular programming.

---

## ✨ Features

- 🔐 Admin Login Authentication
- ➕ Add Student
- 👀 View All Students
- 🔍 Search Student
- ✏️ Update Student
- ❌ Delete Student
- 📤 Export Student Records to CSV
- 📥 Import Student Records from CSV
- ✅ Input Validation
- 📝 Logging
- 💾 JSON Database

---

## 📂 Project Structure

```
Student_Management/
│
├── main.py                 # Application entry point
├── student.py              # CRUD operations
├── auth.py                 # Login authentication
├── database.py             # JSON read/write functions
├── validation.py           # Input validation
├── logger.py               # Logging configuration
│
├── students.json           # Student database
├── users.json              # Admin credentials
├── students.csv            # Exported/Imported CSV
├── logs.txt                # Application logs
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.x
- JSON
- CSV
- Logging
- hashlib
- os

(All modules used are from Python's Standard Library.)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project

```bash
cd Student_Management
```

### 3. Run the project

```bash
python main.py
```

---

## 🔑 Default Login

Username

```
akash
```

Password

```
admin123
```

(Change the password in `users.json` if required.) as it's a sample credential and should be changed before real-world use.

---

## 📚 Concepts Demonstrated

- Modular Programming
- CRUD Operations
- File Handling (JSON & CSV)
- Login Authentication
- Password Hashing (SHA-256)
- Exception Handling
- Input Validation
- Logging
- Code Reusability
- Helper Functions

---

## 👨‍💻 Developed By

**Akash Chauhan**

IIT Guwahati

Python Intern @ Delphic Global

Student @ B.Sc. (Hons.) Data Science & Artificial Intelligence