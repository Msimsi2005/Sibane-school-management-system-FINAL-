# menus.py
# This file controls ALL terminal menus and actions.
# Menus change depending on the user's role:
# Admin, Staff, or Teacher.

from models_student import Student
from models_attendance import AttendanceRecord
from models_fee import FeePayment
import database
from utils import pause, print_line
from auth import add_user
from datetime import date

# =====================================================
# STUDENT FUNCTIONS
# =====================================================

def input_student() -> Student:
    # Function to collect student information from user input and create a Student object
    print_line()  # Print a separator line
    print("ADD NEW STUDENT")  # Display the title
    print_line()  # Print another separator line
    student_id = input("Student ID: ").strip()  # Prompt for student ID and remove whitespace
    name = input("Full Name: ").strip()  # Prompt for full name and strip whitespace
    age = int(input("Age: ").strip())  # Prompt for age, strip, and convert to int
    class_name = input("Class Name: ").strip()  # Prompt for class name and strip
    # Sensitive information section
    guardian_name = input("Guardian Name: ").strip()  # Prompt for guardian name
    guardian_phone = input("Guardian Phone: ").strip()  # Prompt for guardian phone
    medical_notes = input("Medical Notes: ").strip()  # Prompt for medical notes
    return Student(  # Create and return a Student object with the collected data
        student_id,
        name,
        age,
        class_name,
        guardian_name,
        guardian_phone,
        medical_notes
    )


def add_student_flow():
    # Function to handle the flow of adding a new student to the database
    student = input_student()  # Get student details from user input
    students = database.load_students()  # Load existing students from database
    # Prevent duplicate student IDs
    for s in students:  # Loop through existing students
        if s["student_id"] == student.student_id:  # Check if ID already exists
            print("Student ID already exists.")  # Inform user of duplicate
            pause()  # Wait for user to press enter
            return  # Exit the function
    students.append(student.to_dict())  # Add new student as dict to list
    database.save_students(students)  # Save updated list to database
    print("Student added successfully.")  # Confirm addition
    pause()  # Wait for user


def list_students_flow():
    # Function to display a list of all students with basic info
    students = database.load_students()  # Load students from database
    print_line()  # Print separator
    print("STUDENT LIST")  # Title
    print_line()  # Separator
    if not students:  # Check if no students
        print("No students found.")  # Message if empty
        pause()  # Wait
        return  # Exit
    for s in students:  # Loop through students
        print(f"{s['student_id']} | {s['name']} | {s['age']} | {s['class_name']}")  # Print basic info
    pause()  # Wait


def view_student_details_flow(current_user):
    # Function to view detailed info of a specific student, with role-based access
    students = database.load_students()  # Load students
    sid = input("Enter Student ID: ").strip()  # Prompt for student ID
    for s in students:  # Loop through students
        if s["student_id"] == sid:  # Find matching ID
            print_line()  # Separator
            print("BASIC INFO")  # Section title
            print(f"Name: {s['name']}")  # Print name
            print(f"Age: {s['age']}")  # Print age
            print(f"Class: {s['class_name']}")  # Print class
            if current_user.can_view_sensitive_student_info():  # Check permission
                print_line()  # Separator
                print("SENSITIVE INFO")  # Section title
                print(f"Guardian: {s['guardian_name']}")  # Print guardian
                print(f"Phone: {s['guardian_phone']}")  # Print phone
                print(f"Medical: {s['medical_notes']}")  # Print medical notes
            else:  # If no permission
                print_line()  # Separator
                print("Sensitive info hidden for Teachers.")  # Message
            pause()  # Wait
            return  # Exit
    print("Student not found.")  # If not found
    pause()  # Wait



# ATTENDANCE

def mark_attendance_flow():
    # Function to mark attendance for a student (Admin and Staff only)
    sid = input("Student ID: ").strip()  # Get student ID
    today = str(date.today())  # Get today's date as string
    print("1) Present")  # Option 1
    print("2) Absent")  # Option 2
    choice = input("Choose: ").strip()  # Get choice
    status = "Present" if choice == "1" else "Absent"  # Set status based on choice
    note = input("Note: ").strip()  # Get note
    record = AttendanceRecord(sid, today, status, note)  # Create record object
    records = database.load_attendance()  # Load existing records
    records.append(record.to_dict())  # Add new record
    database.save_attendance(records)  # Save to database
    print("Attendance recorded.")  # Confirm
    pause()  # Wait


def view_attendance_flow():
    # Function to view attendance records for a student (all roles)
    sid = input("Student ID: ").strip()  # Get student ID
    records = database.load_attendance()  # Load records
    found = False  # Flag for found records
    for r in records:  # Loop through records
        if r["student_id"] == sid:  # Match student ID
            print(f"{r['date']} | {r['status']} | {r['note']}")  # Print record
            found = True  # Set flag
    if not found:  # If no records
        print("No attendance records found.")  # Message
    pause()  # Wait



# FEES

def add_fee_payment_flow():
    # Function to add a fee payment for a student (Admin and Staff only)
    sid = input("Student ID: ").strip()  # Get student ID
    amount = float(input("Amount: ").strip())  # Get amount as float
    today = str(date.today())  # Today's date
    description = input("Description: ").strip()  # Get description
    payment = FeePayment(sid, amount, today, description)  # Create payment object
    payments = database.load_fees()  # Load existing payments
    payments.append(payment.to_dict())  # Add new payment
    database.save_fees(payments)  # Save to database
    print("Fee payment saved.")  # Confirm
    pause()  # Wait


def view_fee_payments_flow():
    # Function to view fee payments for a student (Admin and Staff only)
    sid = input("Student ID: ").strip()  # Get student ID
    payments = database.load_fees()  # Load payments
    total = 0  # Initialize total
    for p in payments:  # Loop through payments
        if p["student_id"] == sid:  # Match student ID
            print(f"{p['date']} | {p['amount']} | {p['description']}")  # Print payment
            total += p["amount"]  # Add to total
    print(f"Total Paid: {total}")  # Print total
    pause()  # Wait



# USER SETTINGS (ADMIN)

def add_user_flow(current_user):
    # Function to add a new user (Admin only)
    username = input("New Username: ").strip()  # Get username
    password = input("New Password: ").strip()  # Get password
    print("1) Admin")  # Option 1
    print("2) Staff")  # Option 2
    print("3) Teacher")  # Option 3
    role_choice = input("Select Role: ").strip()  # Get role choice
    role_map = {"1": "admin", "2": "staff", "3": "teacher"}  # Map choices to roles
    role = role_map.get(role_choice)  # Get role from map
    if not role:  # If invalid choice
        print("Invalid role.")  # Message
        pause()  # Wait
        return  # Exit
    if add_user(current_user, username, password, role):  # Try to add user
        print("User added successfully.")  # Success
    else:  # If failed
        print("Failed to add user.")  # Failure
    pause()  # Wait


# MENUS BY ROLE

def admin_menu(user):
    # Main menu loop for Admin users
    while True:  # Infinite loop until logout
        print_line()  # Separator
        print("ADMIN MENU")  # Title
        print("1 Add Student")  # Option 1
        print("2 List Students")  # Option 2
        print("3 View Student Details")  # Option 3
        print("4 Mark Attendance")  # Option 4
        print("5 View Attendance")  # Option 5
        print("6 Add Fee Payment")  # Option 6
        print("7 View Fee Payments")  # Option 7
        print("8 Add User")  # Option 8
        print("0 Logout")  # Option 0
        c = input("Select: ").strip()  # Get choice
        if c == "1": add_student_flow()  # Call add student
        elif c == "2": list_students_flow()  # Call list students
        elif c == "3": view_student_details_flow(user)  # Call view details
        elif c == "4": mark_attendance_flow()  # Call mark attendance
        elif c == "5": view_attendance_flow()  # Call view attendance
        elif c == "6": add_fee_payment_flow()  # Call add fee
        elif c == "7": view_fee_payments_flow()  # Call view fees
        elif c == "8": add_user_flow(user)  # Call add user
        elif c == "0": break  # Break loop to logout


def staff_menu(user):
    # Main menu loop for Staff users
    while True:  # Loop
        print_line()  # Separator
        print("STAFF MENU")  # Title
        print("1 Add Student")  # Option 1
        print("2 List Students")  # Option 2
        print("3 View Student Details")  # Option 3
        print("4 Mark Attendance")  # Option 4
        print("5 View Attendance")  # Option 5
        print("6 Add Fee Payment")  # Option 6
        print("7 View Fee Payments")  # Option 7
        print("0 Logout")  # Option 0
        c = input("Select: ").strip()  # Get choice
        if c == "1": add_student_flow()  # Add student
        elif c == "2": list_students_flow()  # List students
        elif c == "3": view_student_details_flow(user)  # View details
        elif c == "4": mark_attendance_flow()  # Mark attendance
        elif c == "5": view_attendance_flow()  # View attendance
        elif c == "6": add_fee_payment_flow()  # Add fee
        elif c == "7": view_fee_payments_flow()  # View fees
        elif c == "0": break  # Logout


def teacher_menu(user):
    # Main menu loop for Teacher users
    while True:  # Loop
        print_line()  # Separator
        print("TEACHER MENU")  # Title
        print("1 List Students")  # Option 1
        print("2 View Student Details")  # Option 2
        print("3 View Attendance")  # Option 3
        print("0 Logout")  # Option 0
        c = input("Select: ").strip()  # Get choice
        if c == "1": list_students_flow()  # List students
        elif c == "2": view_student_details_flow(user)  # View details
        elif c == "3": view_attendance_flow()  # View attendance
        elif c == "0": break  # Logout
