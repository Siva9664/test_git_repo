"""
Utility functions for Employee Management System.
"""


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("  🏢 EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("  1. Add Employee")
    print("  2. View All Employees")
    print("  3. Search Employee")
    print("  4. Update Employee")
    print("  5. Delete Employee")
    print("  6. Exit")
    print("=" * 40)


def get_valid_input(prompt, allow_empty=False):
    """
    Get validated non-empty input from user.

    Args:
        prompt (str): Input prompt to display
        allow_empty (bool): Whether empty input is allowed

    Returns:
        str: User input (stripped)
    """
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("⚠️  This field cannot be empty. Please try again.")


def confirm_action(message):
    """
    Ask user to confirm an action.

    Args:
        message (str): Confirmation message

    Returns:
        bool: True if confirmed, False otherwise
    """
    response = input(f"{message} (y/n): ").strip().lower()
    return response in ("y", "yes")
