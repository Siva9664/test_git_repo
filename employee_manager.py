"""
Employee Manager - Core Business Logic & Data Persistence
Manages CRUD operations, department listings, stats, and JSON file storage.
"""

import json
import os

DATA_FILE = "employees.json"


def load_employees():
    """Load employee records from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return {}


def save_employees(data):
    """Save employee records to JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except IOError:
        return False


def validate_employee_input(name, department, position):
    """Validate name, department, and position inputs."""
    if not name or not name.strip():
        return False, "Employee name cannot be empty."
    if not department or not department.strip():
        return False, "Department cannot be empty."
    if not position or not position.strip():
        return False, "Position cannot be empty."
    return True, ""


def add_employee(name, department, position):
    """Add a new employee and persist data."""
    is_valid, err_msg = validate_employee_input(name, department, position)
    if not is_valid:
        return None, err_msg

    data = load_employees()

    # Generate sequential ID (EMP001, EMP002, etc.)
    if not data:
        new_id = "EMP001"
    else:
        existing_ids = [int(emp_id.replace("EMP", "")) for emp_id in data.keys()]
        next_id_num = max(existing_ids) + 1
        new_id = f"EMP{next_id_num:03d}"

    data[new_id] = {
        "name": name.strip(),
        "department": department.strip(),
        "position": position.strip(),
    }

    if save_employees(data):
        return new_id, "Employee added successfully."
    return None, "Failed to save employee data."


def view_all_employees():
    """Retrieve all employee records."""
    return load_employees()


def search_employee(emp_id):
    """Search employee by ID."""
    data = load_employees()
    emp_id_upper = emp_id.strip().upper()
    if emp_id_upper in data:
        # Return record with the ID included
        record = data[emp_id_upper].copy()
        record["id"] = emp_id_upper
        return record
    return None


def update_employee(emp_id, name=None, department=None, position=None):
    """Update employee details by ID."""
    data = load_employees()
    emp_id_upper = emp_id.strip().upper()

    if emp_id_upper not in data:
        return False, "Employee not found."

    updated = False
    if name and name.strip():
        data[emp_id_upper]["name"] = name.strip()
        updated = True
    if department and department.strip():
        data[emp_id_upper]["department"] = department.strip()
        updated = True
    if position and position.strip():
        data[emp_id_upper]["position"] = position.strip()
        updated = True

    if not updated:
        return False, "No fields updated."

    if save_employees(data):
        return True, "Employee details updated successfully."
    return False, "Failed to save updated employee data."


def delete_employee(emp_id):
    """Delete employee by ID."""
    data = load_employees()
    emp_id_upper = emp_id.strip().upper()

    if emp_id_upper not in data:
        return False, "Employee not found."

    del data[emp_id_upper]
    if save_employees(data):
        return True, "Employee deleted successfully."
    return False, "Failed to save changes."


def list_by_department(department):
    """List all employees in a specific department."""
    data = load_employees()
    dept_lower = department.strip().lower()
    results = {}
    for emp_id, details in data.items():
        if details["department"].lower() == dept_lower:
            results[emp_id] = details
    return results


def get_statistics():
    """Get high-level statistics of employees."""
    data = load_employees()
    total_employees = len(data)
    if total_employees == 0:
        return {"total": 0, "departments": {}}

    dept_counts = {}
    for details in data.values():
        dept = details["department"]
        dept_counts[dept] = dept_counts.get(dept, 0) + 1

    return {"total": total_employees, "departments": dept_counts}
