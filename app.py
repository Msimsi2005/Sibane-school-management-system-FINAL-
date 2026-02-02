# This file controls the main application flow:

from auth import create_default_admin_if_needed, login  
from menus import admin_menu, staff_menu, teacher_menu
from utils import pause, print_line 

def run_app():
    
    create_default_admin_if_needed()  
    while True: 

        print_line()  
        print("Sibane Pre School Management System")  
        print_line()
        print("Login to continue")
    #    print("(Default admin: admin / admin123)") 
        print("0) Exit")

        username = input("Username: ").strip()
        if username == "0":  
            print("\nGoodbye!")
            break

        password = input("Password: ").strip()

        user = login(username, password) 

        if not user:  
            print("\nLogin failed. incorrect username or password.")
            pause() 
            continue
            
        if user.role == "admin":  
            admin_menu(user)
        elif user.role == "staff":  
            staff_menu(user) 
        elif user.role == "teacher": 
            teacher_menu(user) 
        else:  
            print("\nUnknown role. Cannot open menu.")  
            pause() 
