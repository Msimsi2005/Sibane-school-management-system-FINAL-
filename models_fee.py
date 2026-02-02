# This file contains the FeePayment class.

class FeePayment:
    # This class represents ONE fee payment made by a student.

    def __init__(self, student_id: str, amount: float, date: str, description: str):
        # Constructor to initialize fee payment
        self.student_id = student_id
        self.amount = amount 
        self.date = date  
        self.description = description  

    def to_dict(self) -> dict:
        # Method to convert object to dictionary for JSON saving
        return {  # Return dict with attributes
            "student_id": self.student_id,
            "amount": self.amount,
            "date": self.date,
            "description": self.description
        }
