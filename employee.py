"""
Employee class definition for Employee Management System.
"""


class Employee:
    """Represents an employee record."""

    def __init__(self, emp_id, name, department, position):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position

    def to_string(self):
        """Convert employee to a pipe-delimited string for file storage."""
        return f"{self.emp_id}|{self.name}|{self.department}|{self.position}"

    @staticmethod
    def from_string(data_string):
        """Create an Employee object from a pipe-delimited string."""
        parts = data_string.strip().split("|")
        if len(parts) == 4:
            return Employee(parts[0], parts[1], parts[2], parts[3])
        return None

    def __str__(self):
        return (
            f"ID: {self.emp_id} | Name: {self.name} | "
            f"Dept: {self.department} | Position: {self.position}"
        )

    def __repr__(self):
        return (
            f"Employee('{self.emp_id}', '{self.name}', "
            f"'{self.department}', '{self.position}')"
        )
