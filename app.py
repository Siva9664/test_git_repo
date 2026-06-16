"""
Employee Management System - Command-Line Interface
Handles interactions with the user and displays menus.
"""

from employee_manager import (
    add_employee,
    view_all_employees,
    search_employee,
    update_employee,
    delete_employee,
    list_by_department,
    get_statistics,
)


def get_input(prompt, allow_empty=False):
    """Retrieve user input and strip whitespace."""
    while True:
        val = input(prompt).strip()
        if val or allow_empty:
            return val
        print("⚠️  Input cannot be empty. Please try again.")


def display_menu():
    """Display CLI Menu options."""
    print("\n" + "=" * 45)
    print("      🏢 EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 45)
    print("  1. Add Employee")
    print("  2. View All Employees")
    print("  3. Search Employee by ID")
    print("  4. Update Employee Details")
    print("  5. Delete Employee")
    print("  6. List Employees by Department")
    print("  7. View Employee Statistics")
    print("  8. Exit")
    print("=" * 45)


def handle_add():
    print("\n--- 📝 Add Employee ---")
    name = get_input("Enter Name: ")
    department = get_input("Enter Department: ")
    position = get_input("Enter Position: ")

    emp_id, msg = add_employee(name, department, position)
    if emp_id:
        print(f"✅ Success: {msg} Assigned ID: {emp_id}")
    else:
        print(f"❌ Error: {msg}")


def handle_view():
    print("\n--- 📋 View All Employees ---")
    employees = view_all_employees()
    if not employees:
        print("📭 No records found.")
        return

    print(f"{'ID':<8} | {'Name':<20} | {'Department':<15} | {'Position':<20}")
    print("-" * 70)
    for emp_id, info in employees.items():
        print(
            f"{emp_id:<8} | {info['name']:<20} | {info['department']:<15} | {info['position']:<20}"
        )


def handle_search():
    print("\n--- 🔍 Search Employee ---")
    emp_id = get_input("Enter Employee ID: ")
    record = search_employee(emp_id)
    if record:
        print(f"📌 Employee Details for {record['id']}:")
        print(f"  Name:       {record['name']}")
        print(f"  Department: {record['department']}")
        print(f"  Position:   {record['position']}")
    else:
        print("❌ Employee not found.")


def handle_update():
    print("\n--- 🔄 Update Employee Details ---")
    emp_id = get_input("Enter Employee ID to update: ")
    record = search_employee(emp_id)
    if not record:
        print("❌ Employee not found.")
        return

    print(f"Editing details for {emp_id} (Leave blank to keep current):")
    name = get_input(f"New Name [{record['name']}]: ", allow_empty=True)
    department = get_input(
        f"New Department [{record['department']}]: ", allow_empty=True
    )
    position = get_input(f"New Position [{record['position']}]: ", allow_empty=True)

    success, msg = update_employee(emp_id, name, department, position)
    if success:
        print(f"✅ Success: {msg}")
    else:
        print(f"❌ Error: {msg}")


def handle_delete():
    print("\n--- 🗑️ Delete Employee ---")
    emp_id = get_input("Enter Employee ID to delete: ")
    record = search_employee(emp_id)
    if not record:
        print("❌ Employee not found.")
        return

    confirm = input(
        f"Are you sure you want to delete {record['name']} ({emp_id})? (y/n): "
    )
    if confirm.lower().strip() in ("y", "yes"):
        success, msg = delete_employee(emp_id)
        if success:
            print(f"✅ Success: {msg}")
        else:
            print(f"❌ Error: {msg}")
    else:
        print("❌ Deletion canceled.")


def handle_dept_list():
    print("\n--- 🏢 Department Listing ---")
    department = get_input("Enter Department Name: ")
    results = list_by_department(department)
    if not results:
        print(f"📭 No employees found in department: {department}")
        return

    print(f"\nEmployees in '{department}':")
    print(f"{'ID':<8} | {'Name':<20} | {'Position':<20}")
    print("-" * 55)
    for emp_id, info in results.items():
        print(f"{emp_id:<8} | {info['name']:<20} | {info['position']:<20}")


def handle_stats():
    print("\n--- 📊 Statistics Overview ---")
    stats = get_statistics()
    print(f"Total Employees: {stats['total']}")
    if stats["total"] > 0:
        print("\nDepartment breakdown:")
        for dept, count in stats["departments"].items():
            print(f"  - {dept}: {count}")


def main():
    while True:
        display_menu()
        choice = get_input("Enter choice (1-8): ")
        if choice == "1":
            handle_add()
        elif choice == "2":
            handle_view()
        elif choice == "3":
            handle_search()
        elif choice == "4":
            handle_update()
        elif choice == "5":
            handle_delete()
        elif choice == "6":
            handle_dept_list()
        elif choice == "7":
            handle_stats()
        elif choice == "8":
            print("\n👋 Exiting Employee Management System. Goodbye!")
            break
        else:
            print("⚠️  Invalid Choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
