# This file contains USER classes (Admin, Staff, Teacher).
# i used an ABSTRACT class to enforce that every user type must have a role and permissions.

from abc import ABC, abstractmethod  # Import ABC for abstract base class

class User(ABC):
    # This is the ABSTRACT BASE CLASS (ABC).
    def __init__(self, username: str, password: str):
        # Constructor for User base class
        # Store username and password.
        self.username = username  # Set username
        self.password = password  # Set password

    @property
    @abstractmethod
    def role(self) -> str:
        # Abstract property: Every child class MUST provide its role name.
        pass  # Must be implemented by subclasses

    def can_view_sensitive_student_info(self) -> bool:
        # Method to check if user can view sensitive info
        # By default, users cannot view sensitive info.
        # Child classes can override by returning True.
        return False  # Default to False

    def can_add_users(self) -> bool:
        # Method to check if user can add users
        # By default, users cannot create other users.
        return False  # Default to False


class Admin(User):
    # Admin inherits from User.
    # Inheritance means Admin automatically gets everything from User.
    @property
    def role(self) -> str:
        # Property to get Admin role name.
        return "admin"  # Return admin role

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
        return "staff"  # Return staff role

    def can_view_sensitive_student_info(self) -> bool:
        # Override: Staff can see sensitive info (because they do registration).
        return True  # Return True


class Teacher(User):
    # Teacher inherits from User.
    @property
    def role(self) -> str:
        # Property to get Teacher role name.
        return "teacher"  # Return teacher role

    # Teacher does NOT override can_view_sensitive_student_info(),
    # so it stays False (restricted).