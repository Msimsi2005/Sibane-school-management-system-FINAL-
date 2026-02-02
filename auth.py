# auth.py
# This file handles login and user creation.
# It also converts stored user dictionaries into actual User objects.

from models_user import Admin, Staff, Teacher  # Import user model classes
import database  # Import database functions

def create_default_admin_if_needed():
    # Function to create a default admin if no users exist
    users = database.load_users()  # Load existing users from database
    if len(users) == 0:  # Check if no users
        # Create first admin user.
        default = {  # Define default admin dict
            "username": "admin",
            "password": "admin123",
            "role": "admin"
        }
        users.append(default)  # Add to users list
        database.save_users(users)  # Save to database

def user_dict_to_object(user_dict):
    # Function to convert user dictionary to User object
    role = user_dict["role"]  # Get role from dict
    if role == "admin":  # If admin
        return Admin(user_dict["username"], user_dict["password"])  # Return Admin object
    if role == "staff":  # If staff
        return Staff(user_dict["username"], user_dict["password"])  # Return Staff object
    if role == "teacher":  # If teacher
        return Teacher(user_dict["username"], user_dict["password"])  # Return Teacher object
    # If role is unknown, return None .
    return None  # Return None for unknown role

def login(username: str, password: str):
    # Function to authenticate user login
    users = database.load_users()  # Load users
    for u in users:  # Loop through users
        if u["username"] == username and u["password"] == password:  # Check match
            # If match, convert dict to object and return it.
            return user_dict_to_object(u)  # Return user object
    # If no match found, return None.
    return None  # Return None if no match

def add_user(current_user, new_username: str, new_password: str, new_role: str) -> bool:
    # Function to add a new user (admin only)
    if not current_user.can_add_users():  # Check permission
        return False  # Return false if not allowed
    users = database.load_users()  # Load users
    # Make sure username is not already used.
    for u in users:  # Loop through users
        if u["username"] == new_username:  # Check if username exists
            return False  # Return false if duplicate
    # Add new user dictionary.
    users.append({  # Append new user dict
        "username": new_username,
        "password": new_password,
        "role": new_role
    })
    database.save_users(users)  # Save users
    return True  # Return true on success
