# This file handles ALL data storage for the system.

import json  # Import JSON module for data serialization
import os  # Import OS module for file operations

DATA_FOLDER = "data" 

USERS_FILE = os.path.join(DATA_FOLDER, "users.json")  # Path to users JSON
STUDENTS_FILE = os.path.join(DATA_FOLDER, "students.json")  
ATTENDANCE_FILE = os.path.join(DATA_FOLDER, "attendance.json")  
FEES_FILE = os.path.join(DATA_FOLDER, "fees.json")  

# FOLDER CREATION
def ensure_data_folder():
    if not os.path.exists(DATA_FOLDER):  # Check if folder exists
        os.makedirs(DATA_FOLDER) 
        
# GENERIC JSON FUNCTIONS
def load_json(path: str, default_value):
    ensure_data_folder()  # Ensure data folder exists
    if not os.path.exists(path):  
        return default_value  # Return default
    with open(path, "r", encoding="utf-8") as file:  # Open file for reading
        return json.load(file)  # Load and return JSON data

# This function saves data into a JSON file.
def save_json(path: str, data):
    # If the file does not exist, it is created automatically.
    ensure_data_folder()  # Ensure data folder
    with open(path, "w", encoding="utf-8") as file:  # Open file for writing
        json.dump(data, file, indent=2)  

# USERS
def load_users() -> list:
    # Load all users from users.json
    return load_json(USERS_FILE, default_value=[])  


def save_users(users: list):
    # Save all users to users.json
    save_json(USERS_FILE, users)  # Save users list


# STUDENTS
def load_students() -> list:
    return load_json(STUDENTS_FILE, default_value=[])  # Load students


def save_students(students: list):
    save_json(STUDENTS_FILE, students)  # Save students



# ATTENDANCE
def load_attendance() -> list:
    return load_json(ATTENDANCE_FILE, default_value=[])  # Load attendance


def save_attendance(records: list):
    # Save attendance records to attendance.json
    save_json(ATTENDANCE_FILE, records)  # Save attendance


# FEES
def load_fees() -> list:
    # Load all fee payments from fees.json
    return load_json(FEES_FILE, default_value=[])  # Load fees


def save_fees(payments: list):
    save_json(FEES_FILE, payments)  # Save fees
