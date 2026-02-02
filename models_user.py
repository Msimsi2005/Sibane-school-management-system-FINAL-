# This file contains USER classes (Admin, Staff, Teacher).
# i used an ABSTRACT class to enforce that every user type must have a role and permissions.

from abc import ABC, abstractmethod  # Import ABC for abstract base class

class User(ABC):
    # This is the ABSTRACT BASE CLASS (ABC).
    def __init__(self, username: str, password: str):
        # Constructor for User base class
        # Store username and password.
        self.username = username  
        self.password = password  

    @property
    @abstractmethod
    def role(self) -> str:
        # Abstract property: Every child class MUST provide its role name.
        pass  # Must be implemented by subclasses

    def can_view_sensitive_student_info(self) -> bool:
        # Method to check if user can view sensitive info
        return False  # Default to False

    def can_add_users(self) -> bool:
        # Method to check if user can add users
        return False  # Default to False


class Admin(User):
    # Admin inherits from User.
    
    @property
    def role(self) -> str:
        # Property to get Admin role name.
        return "admin" 

    def can_view_sensitive_student_info(self) -> bool:
        # Override: Admin can view sensitive info.
        return True  # Return True

    def can_add_users(self) -> bool:
        # Override: Admin can create new users (admin/staff/teacher).
        return True  # Return True


class Staff(User):
# Staff inherits from User.
    
    @property
    def role(self) -> str:
        # Property to get Staff role name.
        return "staff"  

    def can_view_sensitive_student_info(self) -> bool:
        return True 

# Teacher inherits from User
class Teacher(User):
    
    @property
    def role(self) -> str:
        # Property to get Teacher role name.
        return "teacher"  
