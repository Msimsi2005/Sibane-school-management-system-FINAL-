# This file controls ALL terminal menus and actions.
# Admin, Staff, or Teacher.

from models_student import Student
from models_attendance import AttendanceRecord
from models_fee import FeePayment
import database
from utils import pause, print_line
from auth import add_user
from datetime import date


# Student Function to collect student information from user input and create a Student object
def input_student() -> Student:
    print_line() 
    print("ADD NEW STUDENT") 
    print_line() 
    student_id = input("Student ID: ").strip()  # strip is to remove whitespace
    name = input("Full Name: ").strip() 
    age = int(input("Age: ").strip()) 
    class_name = input("Class Name: ").strip() 
    
    # Sensitive information section
    guardian_name = input("Guardian Name: ").strip() 
    guardian_phone = input("Guardian Phone: ").strip()
    medical_notes = input("Medical Notes: ").strip()  
    return Student(  # Create and return a Student object with the collected data
        student_id,
        name,
        age,
        class_name,
        guardian_name,
        guardian_phone,
        medical_notes
    )

# Function to handle the flow of adding a new student to the database
def add_student_flow():
    student = input_student()  # Get student details from user input
    students = database.load_students() 
    for s in students: 
        if s["student_id"] == student.student_id:  
            print("Student ID already exists.")  
            pause() 
            return  
            
    students.append(student.to_dict())  # Add new student as dict to list
    database.save_students(students) 
    print("Student added successfully.") 
    pause() 


# Function to display a list of all students with basic info
def list_students_flow():
    students = database.load_students()  
    print_line()  
    print("STUDENT LIST") 
    print_line()
    if not students:  
        print("No students found.")  
        pause() 
        return  
    for s in students:  # Loop through students
        print(f"{s['student_id']} | {s['name']} | {s['age']} | {s['class_name']}")  # Print basic info
    pause()


# Function to view detailed info of a specific student, with role-based access
def view_student_details_flow(current_user):
    students = database.load_students() 
    sid = input("Enter Student ID: ").strip() 
    for s in students: 
        if s["student_id"] == sid: 
            print_line()  
            print("BASIC INFO")
            print(f"Name: {s['name']}")  
            print(f"Age: {s['age']}") 
            print(f"Class: {s['class_name']}") 
            if current_user.can_view_sensitive_student_info(): 
                print_line() 
                print("SENSITIVE INFO")  
                print(f"Guardian: {s['guardian_name']}") 
                print(f"Phone: {s['guardian_phone']}") 
                print(f"Medical: {s['medical_notes']}") 
            else:  
                print_line() 
                print("Sensitive info hidden for Teachers.") 
            pause() 
            return 
    print("Student not found.") 
    pause() 



# ATTENDANCE
def mark_attendance_flow():
    # Function to mark attendance for a student (Admin and Staff only)
    sid = input("Student ID: ").strip()  
    today = str(date.today())  
    print("1) Present")  
    print("2) Absent") 
    choice = input("Choose: ").strip()  # Get choice
    status = "Present" if choice == "1" else "Absent"  
    note = input("Note: ").strip()  # Get note
    record = AttendanceRecord(sid, today, status, note)  
    records = database.load_attendance()  # Load existing records
    records.append(record.to_dict()) 
    database.save_attendance(records) 
    print("Attendance recorded.") 
    pause()  

def view_attendance_flow():
    # Function to view attendance records for a student (all roles)
    sid = input("Student ID: ").strip() 
    records = database.load_attendance() 
    found = False  # Flag for found records
    for r in records: 
        if r["student_id"] == sid: 
            print(f"{r['date']} | {r['status']} | {r['note']}")
            found = True  # Set flag
    if not found: 
        print("No attendance records found.")  
    pause() 

# FEES
def add_fee_payment_flow():
    # Function to add a fee payment for a student (Admin and Staff only)
    sid = input("Student ID: ").strip()  
    amount = float(input("Amount: ").strip())  
    today = str(date.today())  
    description = input("Description: ").strip() 
    payment = FeePayment(sid, amount, today, description)  # Create payment object
    payments = database.load_fees()  
    payments.append(payment.to_dict())  
    database.save_fees(payments)  
    print("Fee payment saved.")  
    pause()  # Wait


def view_fee_payments_flow():
    # Function to view fee payments for a student (Admin and Staff only)
    sid = input("Student ID: ").strip()  
    payments = database.load_fees() 
    total = 0
    for p in payments:
        if p["student_id"] == sid: 
            print(f"{p['date']} | {p['amount']} | {p['description']}") 
            total += p["amount"]  
    print(f"Total Paid: {total}")  
    pause() 

# USER SETTINGS (ADMIN)
def add_user_flow(current_user):
    # Function to add a new user (Admin only)
    username = input("New Username: ").strip()  
    password = input("New Password: ").strip()  
    print("1) Admin")  
    print("2) Staff")  
    print("3) Teacher")
    role_choice = input("Select Role: ").strip()  
    role_map = {"1": "admin", "2": "staff", "3": "teacher"}  # Map choices to roles
    role = role_map.get(role_choice)  # Get role from map
    if not role:  
        print("Invalid role.")  
        pause()  
        return  
    if add_user(current_user, username, password, role): 
        print("User added successfully.")  # Success
    else:  
        print("Failed to add user.") 
    pause()  


# MENUS BY ROLE
def admin_menu(user):
    # Main menu loop for Admin users
    while True:  
        print_line() 
        print("ADMIN MENU")  
        print("1 Add Student") 
        print("2 List Students") 
        print("3 View Student Details")  
        print("4 Mark Attendance")  
        print("5 View Attendance") 
        print("6 Add Fee Payment")  
        print("7 View Fee Payments") 
        print("8 Add User")  
        print("0 Logout")  
        c = input("Select: ").strip()  # Get choice
        if c == "1": add_student_flow()  
        elif c == "2": list_students_flow()  # Call list students
        elif c == "3": view_student_details_flow(user) 
        elif c == "4": mark_attendance_flow()  
        elif c == "5": view_attendance_flow()  
        elif c == "7": view_fee_payments_flow()  
        elif c == "8": add_user_flow(user)  
        elif c == "0": break  


def staff_menu(user):
    # Main menu loop for Staff users
    while True: 
        print_line() 
        print("STAFF MENU") 
        print("1 Add Student") 
        print("2 List Students") 
        print("3 View Student Details")  
        print("4 Mark Attendance")  
        print("5 View Attendance") 
        print("6 Add Fee Payment")  
        print("7 View Fee Payments")  
        print("0 Logout")  
        c = input("Select: ").strip()  
        if c == "1": add_student_flow() 
        elif c == "2": list_students_flow() 
        elif c == "3": view_student_details_flow(user) 
        elif c == "4": mark_attendance_flow()  
        elif c == "5": view_attendance_flow()  
        elif c == "6": add_fee_payment_flow()  
        elif c == "7": view_fee_payments_flow()
        elif c == "0": break 

# Main menu loop for Teacher users
def teacher_menu(user):
    while True:  
        print_line()  
        print("TEACHER MENU")  
        print("1 List Students") 
        print("2 View Student Details")  
        print("3 View Attendance")
        print("0 Logout")  
        c = input("Select: ").strip() 
        if c == "1": list_students_flow() 
        elif c == "2": view_student_details_flow(user) 
        elif c == "3": view_attendance_flow()  
        elif c == "0": break  # Logout
