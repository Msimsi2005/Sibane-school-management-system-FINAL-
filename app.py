# This file controls the main application flow:

from auth import create_default_admin_if_needed, login  
from menus import admin_menu, staff_menu, teacher_menu
from utils import pause, print_line 

def run_app():
    # Main function to run the application
    # Step 1: Ensure there is at least one admin in the system.
    create_default_admin_if_needed()  # Create default admin if none exists

    while True:  # Main loop for the program
        # This is the main loop for the whole program.
        # It keeps running until the user chooses to exit.

        print_line()  # Print separator line
        print("Sibane Pre School Management System")  # Display app title
        print_line()
        print("Login to continue")  # Prompt for login
    #    print("(Default admin: admin / admin123)") 
        print("0) Exit")

        username = input("Username: ").strip()  # Get username input and strip whitespace
        if username == "0":  # Check if user wants to exit
            # Exit the whole system
            print("\nGoodbye!")  # Farewell message
            break  # Break out of loop

        password = input("Password: ").strip()  # Get password input and strip

        # Step 2: Try login
        user = login(username, password)  # Attempt to log in with credentials

        if not user:  # If login failed
            print("\nLogin failed. incorrect username or password.")  # Error message
            pause()  # Wait for user to press enter
            continue  # Go back to login prompt

        # Step 3: Redirect to menu based on role
        if user.role == "admin":  # If user is admin
            admin_menu(user)  # Show admin menu
        elif user.role == "staff":  # If user is staff
            staff_menu(user)  # Show staff menu
        elif user.role == "teacher":  # If user is teacher
            teacher_menu(user)  # Show teacher menu
        else:  # If unknown role
            print("\nUnknown role. Cannot open menu.")  # Error message
            pause()  # Wait
