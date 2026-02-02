# This file handles login and user creation.
# It also converts stored user dictionaries into actual User objects.

from models_user import Admin, Staff, Teacher  
import database 

def create_default_admin_if_needed():
    users = database.load_users()  
    if len(users) == 0:  
        default = { 
            "username": "admin",
            "password": "admin123",
            "role": "admin"
        }
        users.append(default)
        database.save_users(users)  

# Function to convert user dictionary to User object:
def user_dict_to_object(user_dict):
    role = user_dict["role"]  
    if role == "admin": 
        return Admin(user_dict["username"], user_dict["password"]) 
    if role == "staff":  
        return Staff(user_dict["username"], user_dict["password"]) 
    if role == "teacher": 
        return Teacher(user_dict["username"], user_dict["password"])  # Return Teacher object

    return None 
    
 # Function to authenticate user login
def login(username: str, password: str):
    users = database.load_users()  
    for u in users: 
        if u["username"] == username and u["password"] == password:
            # If match, convert dict to object and return it.
            return user_dict_to_object(u)  # Return user object
    return None  # Return None if no match


# Function to add a new user (admin only)
def add_user(current_user, new_username: str, new_password: str, new_role: str) -> bool:
    if not current_user.can_add_users():
        return False 
    users = database.load_users()  
    # Make sure username is not already used.
    for u in users:  
        if u["username"] == new_username:  
            return False  # Return false if duplicate
            
    # Add new user dictionary.
    users.append({  # Append new user dict
        "username": new_username,
        "password": new_password,
        "role": new_role
    })
    database.save_users(users) 
    return True 
