# models_attendance.py
# This file contains the AttendanceRecord class.

class AttendanceRecord:
    # This class represents ONE attendance record for ONE student on ONE date.

    def __init__(self, student_id: str, date: str, status: str, note: str):
        # Constructor to initialize attendance record
        # Save values in the object
        self.student_id = student_id  # Set student ID
        self.date = date  # Set date
        self.status = status  # Set status ("Present" or "Absent")
        self.note = note  # Set optional note

    def to_dict(self) -> dict:
        # Method to convert object to dictionary for JSON saving
        return {  # Return dict with attributes
            "student_id": self.student_id,
            "date": self.date,
            "status": self.status,
            "note": self.note
        }
