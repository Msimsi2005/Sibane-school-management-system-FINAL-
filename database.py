# database.py
# This file handles ALL data storage for the system.

import json  # Import JSON module for data serialization
import os  # Import OS module for file operations

# this is the Folder where all data files will be stored
DATA_FOLDER = "data"  # Define data folder path

# Individual JSON files
USERS_FILE = os.path.join(DATA_FOLDER, "users.json")  # Path to users JSON
STUDENTS_FILE = os.path.join(DATA_FOLDER, "students.json")  # Path to students JSON
ATTENDANCE_FILE = os.path.join(DATA_FOLDER, "attendance.json")  # Path to attendance JSON
FEES_FILE = os.path.join(DATA_FOLDER, "fees.json")  # Path to fees JSON



# FOLDER CREATION

def ensure_data_folder():
    # This function checks if the data folder exists.
    # If it does NOT exist, it creates meaning the user never has to create JSON files manually.
    if not os.path.exists(DATA_FOLDER):  # Check if folder exists
        os.makedirs(DATA_FOLDER)  # Create folder if not



# GENERIC JSON FUNCTIONS

def load_json(path: str, default_value):
    # This function loads data from a JSON file.
    # If the file does not exist, it returns the default value.
    ensure_data_folder()  # Ensure data folder exists
    if not os.path.exists(path):  # Check if file exists
        # File not found - return empty list or default value
        return default_value  # Return default
    with open(path, "r", encoding="utf-8") as file:  # Open file for reading
        return json.load(file)  # Load and return JSON data


def save_json(path: str, data):
    # This function saves data into a JSON file.
    # If the file does not exist, it is created automatically.
    ensure_data_folder()  # Ensure data folder
    with open(path, "w", encoding="utf-8") as file:  # Open file for writing
        json.dump(data, file, indent=2)  # Dump data with indentation



# USERS

def load_users() -> list:
    # Load all users from users.json
    return load_json(USERS_FILE, default_value=[])  # Load users with empty list default


def save_users(users: list):
    # Save all users to users.json
    save_json(USERS_FILE, users)  # Save users list


# STUDENTS

def load_students() -> list:
    # Load all students from students.json
    return load_json(STUDENTS_FILE, default_value=[])  # Load students


def save_students(students: list):
    # Save all students to students.json
    save_json(STUDENTS_FILE, students)  # Save students



# ATTENDANCE


def load_attendance() -> list:
    # Load all attendance records from attendance.json
    return load_json(ATTENDANCE_FILE, default_value=[])  # Load attendance


def save_attendance(records: list):
    # Save attendance records to attendance.json
    save_json(ATTENDANCE_FILE, records)  # Save attendance


# FEES

def load_fees() -> list:
    # Load all fee payments from fees.json
    return load_json(FEES_FILE, default_value=[])  # Load fees


def save_fees(payments: list):
    # Save fee payments to fees.json
    save_json(FEES_FILE, payments)  # Save fees
