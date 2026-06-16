"""
Employee Manager - Core CRUD operations for Employee Management System.
Handles Add, View, Search, Update, and Delete operations.
"""

from employee import Employee

DATA_FILE = "employees.txt"


def load_employees():
    """Load all employees from the data file."""
    employees = []
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                emp = Employee.from_string(line)
                if emp:
                    employees.append(emp)
    except FileNotFoundError:
        pass
    return employees


def save_employees(employees):
    """Save all employees to the data file."""
    with open(DATA_FILE, "w") as file:
        for emp in employees:
            file.write(emp.to_string() + "\n")


def generate_emp_id(employees):
    """Generate the next employee ID."""
    if not employees:
        return "EMP001"
    max_id = max(int(emp.emp_id.replace("EMP", "")) for emp in employees)
    return f"EMP{max_id + 1:03d}"


# ==========================================
# Feature: Add Employee
# ==========================================
def add_employee(name, department, position):
    """
    Add a new employee to the system.

    Args:
        name (str): Employee's full name
        department (str): Department name
        position (str): Job position/title

    Returns:
        Employee: The newly created employee object
    """
    employees = load_employees()
    emp_id = generate_emp_id(employees)
    new_employee = Employee(emp_id, name, department, position)
    employees.append(new_employee)
    save_employees(employees)
    print(f"\n✅ Employee added successfully!")
    print(f"   {new_employee}")
    return new_employee


# ==========================================
# Feature: View All Employees
# ==========================================
def view_employees():
    """
    Display all employees in a formatted table.

    Returns:
        list: List of all Employee objects
    """
    employees = load_employees()
    if not employees:
        print("\n📭 No employees found in the system.")
        return employees

    print("\n" + "=" * 70)
    print(f"{'ID':<10} {'Name':<20} {'Department':<15} {'Position':<20}")
    print("=" * 70)
    for emp in employees:
        print(f"{emp.emp_id:<10} {emp.name:<20} {emp.department:<15} {emp.position:<20}")
    print("=" * 70)
    print(f"Total employees: {len(employees)}")
    return employees


# ==========================================
# Feature: Search Employee
# ==========================================
def search_employee(search_term):
    """
    Search for employees by ID, name, or department.

    Args:
        search_term (str): The search keyword

    Returns:
        list: List of matching Employee objects
    """
    employees = load_employees()
    search_term = search_term.lower()
    results = [
        emp for emp in employees
        if search_term in emp.emp_id.lower()
        or search_term in emp.name.lower()
        or search_term in emp.department.lower()
    ]

    if not results:
        print(f"\n🔍 No employees found matching '{search_term}'.")
    else:
        print(f"\n🔍 Found {len(results)} employee(s):")
        print("-" * 70)
        for emp in results:
            print(f"  {emp}")
    return results


# ==========================================
# Feature: Update Employee
# ==========================================
def update_employee(emp_id, name=None, department=None, position=None):
    """
    Update an existing employee's details.

    Args:
        emp_id (str): Employee ID to update
        name (str, optional): New name
        department (str, optional): New department
        position (str, optional): New position

    Returns:
        Employee or None: Updated employee if found, None otherwise
    """
    employees = load_employees()
    for emp in employees:
        if emp.emp_id.lower() == emp_id.lower():
            if name:
                emp.name = name
            if department:
                emp.department = department
            if position:
                emp.position = position
            save_employees(employees)
            print(f"\n✅ Employee {emp_id} updated successfully!")
            print(f"   {emp}")
            return emp

    print(f"\n❌ Employee with ID '{emp_id}' not found.")
    return None


# ==========================================
# Feature: Delete Employee
# ==========================================
def delete_employee(emp_id):
    """
    Delete an employee from the system.

    Args:
        emp_id (str): Employee ID to delete

    Returns:
        bool: True if deleted successfully, False otherwise
    """
    employees = load_employees()
    original_count = len(employees)
    employees = [emp for emp in employees if emp.emp_id.lower() != emp_id.lower()]

    if len(employees) < original_count:
        save_employees(employees)
        print(f"\n✅ Employee {emp_id} deleted successfully!")
        return True
    else:
        print(f"\n❌ Employee with ID '{emp_id}' not found.")
        return False
