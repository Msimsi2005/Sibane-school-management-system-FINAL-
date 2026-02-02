# This file contains the AttendanceRecord class.

class AttendanceRecord:
    # This class represents ONE attendance record for ONE student on ONE date.

    def __init__(self, student_id: str, date: str, status: str, note: str):
        # Constructor to initialize attendance record
        # Save values in the object
        self.student_id = student_id  
        self.date = date  
        self.status = status  
        self.note = note  

    def to_dict(self) -> dict:
        # Method to convert object to dictionary for JSON saving
        return {  
            "student_id": self.student_id,
            "date": self.date,
            "status": self.status,
            "note": self.note
        }
