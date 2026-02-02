# models_student.py
# This file contains the Student class.

class Student:
    # This class represents a student in the Sibane Pre School system.

    def __init__(self, student_id: str, name: str, age: int, class_name: str,
                 guardian_name: str, guardian_phone: str, medical_notes: str):
        # Constructor to initialize student object
        # Some fields are sensitive and should not be seen by teachers.
        self.student_id = student_id  # Set student ID
        self.name = name  # Set student name
        self.age = age  # Set student age
        self.class_name = class_name  # Set class name
        self.guardian_name = guardian_name  # Set guardian name (sensitive)
        self.guardian_phone = guardian_phone  # Set guardian phone (sensitive)
        self.medical_notes = medical_notes  # Set medical notes (sensitive)

    def to_dict(self) -> dict:
        # Method to convert Student object into a dictionary for JSON saving
        return {  # Return dict with all attributes
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "class_name": self.class_name,
            "guardian_name": self.guardian_name,
            "guardian_phone": self.guardian_phone,
            "medical_notes": self.medical_notes
        }

    @staticmethod
    def from_dict(data: dict) -> "Student":
        # Static method to convert dictionary back into Student object
        return Student(  # Create and return Student from dict
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            class_name=data["class_name"],
            guardian_name=data["guardian_name"],
            guardian_phone=data["guardian_phone"],
            medical_notes=data["medical_notes"]
        )
