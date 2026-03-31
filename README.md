# Student Management System (CRUD) 🎓

A simple and efficient **Python-based** console application for managing student records. This project implements full CRUD (Create, Read, Update, Delete) operations with data persistence using CSV files.

## 🚀 Key Features

*   **Full Registration:** Capture Student ID, Name, Age, Course, and Status.
*   **Dynamic Search:** Locate students by name (case-insensitive).
*   **Data Validation:** Strict input control to prevent errors (accepts only positive integers and non-empty strings).
*   **CSV Persistence:** Save and load information locally to ensure data is not lost when closing the app.
*   **Modular Architecture:** Clear separation between business logic, validations, and file management.

## 🛠️ Project Structure

The project is organized as follows:

```text
├── src/
│   ├── data/
│   │   └── storage.py      # Logic for saving and loading CSV files.
│   ├── services/
│   │   └── functions.py    # functionsCRUD class with core logic.
│   ├── utils/
│   │   └── validation.py   # Validation functions (Int and String).
│   └── main.py             # Interactive menu and entry point.
└── DataCSV.csv             # File where data is stored.
