"""
Employee Management System - Main Application
A CLI-based application for managing employee records.

Author: Siva
Department: AIML
"""

from employee_manager import (
    add_employee,
    view_employees,
    search_employee,
    update_employee,
    delete_employee,
)
from utils import display_menu, get_valid_input, confirm_action


def handle_add():
    """Handle the Add Employee workflow."""
    print("\n--- Add New Employee ---")
    name = get_valid_input("Enter employee name: ")
    department = get_valid_input("Enter department: ")
    position = get_valid_input("Enter position: ")
    add_employee(name, department, position)


def handle_search():
    """Handle the Search Employee workflow."""
    print("\n--- Search Employee ---")
    search_term = get_valid_input("Enter search term (ID / Name / Department): ")
    search_employee(search_term)


def handle_update():
    """Handle the Update Employee workflow."""
    print("\n--- Update Employee ---")
    emp_id = get_valid_input("Enter Employee ID to update: ")
    print("(Press Enter to skip a field)")
    name = get_valid_input("New name: ", allow_empty=True) or None
    department = get_valid_input("New department: ", allow_empty=True) or None
    position = get_valid_input("New position: ", allow_empty=True) or None
    update_employee(emp_id, name, department, position)


def handle_delete():
    """Handle the Delete Employee workflow."""
    print("\n--- Delete Employee ---")
    emp_id = get_valid_input("Enter Employee ID to delete: ")
    if confirm_action(f"Are you sure you want to delete {emp_id}?"):
        delete_employee(emp_id)
    else:
        print("❌ Delete cancelled.")


def main():
    """Main application entry point."""
    print("\n🚀 Welcome to the Employee Management System!")

    while True:
        display_menu()
        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            handle_add()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            handle_search()
        elif choice == "4":
            handle_update()
        elif choice == "5":
            handle_delete()
        elif choice == "6":
            print("\n👋 Thank you for using Employee Management System!")
            print("   Goodbye!\n")
            break
        else:
            print("\n⚠️  Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
