"""
Unit tests for Employee Management System.
Tests cover Employee class and CRUD operations.
"""

import os
import sys
import unittest

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from employee import Employee
from employee_manager import (
    add_employee,
    load_employees,
    save_employees,
    search_employee,
    update_employee,
    delete_employee,
    generate_emp_id,
    DATA_FILE,
)


class TestEmployee(unittest.TestCase):
    """Test cases for the Employee class."""

    def test_employee_creation(self):
        """Test creating an Employee object."""
        emp = Employee("EMP001", "John Doe", "HR", "Manager")
        self.assertEqual(emp.emp_id, "EMP001")
        self.assertEqual(emp.name, "John Doe")
        self.assertEqual(emp.department, "HR")
        self.assertEqual(emp.position, "Manager")

    def test_employee_to_string(self):
        """Test converting Employee to string format."""
        emp = Employee("EMP001", "John Doe", "HR", "Manager")
        result = emp.to_string()
        self.assertEqual(result, "EMP001|John Doe|HR|Manager")

    def test_employee_from_string(self):
        """Test creating Employee from string format."""
        emp = Employee.from_string("EMP002|Alice Smith|IT|Software Engineer")
        self.assertIsNotNone(emp)
        self.assertEqual(emp.emp_id, "EMP002")
        self.assertEqual(emp.name, "Alice Smith")
        self.assertEqual(emp.department, "IT")
        self.assertEqual(emp.position, "Software Engineer")

    def test_employee_from_invalid_string(self):
        """Test creating Employee from invalid string returns None."""
        emp = Employee.from_string("invalid data")
        self.assertIsNone(emp)

    def test_employee_str(self):
        """Test Employee __str__ representation."""
        emp = Employee("EMP001", "John Doe", "HR", "Manager")
        result = str(emp)
        self.assertIn("EMP001", result)
        self.assertIn("John Doe", result)


class TestEmployeeManager(unittest.TestCase):
    """Test cases for Employee Manager CRUD operations."""

    def setUp(self):
        """Set up test fixtures - create a test data file."""
        self.test_employees = [
            Employee("EMP001", "John Doe", "HR", "Manager"),
            Employee("EMP002", "Alice Smith", "IT", "Software Engineer"),
            Employee("EMP003", "Robert Brown", "Finance", "Accountant"),
        ]
        save_employees(self.test_employees)

    def tearDown(self):
        """Clean up - remove test data file."""
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

    def test_load_employees(self):
        """Test loading employees from file."""
        employees = load_employees()
        self.assertEqual(len(employees), 3)
        self.assertEqual(employees[0].name, "John Doe")

    def test_save_and_load_employees(self):
        """Test save and load round-trip."""
        save_employees(self.test_employees)
        loaded = load_employees()
        self.assertEqual(len(loaded), len(self.test_employees))
        for original, loaded_emp in zip(self.test_employees, loaded):
            self.assertEqual(original.emp_id, loaded_emp.emp_id)
            self.assertEqual(original.name, loaded_emp.name)

    def test_generate_emp_id_empty(self):
        """Test ID generation with no existing employees."""
        result = generate_emp_id([])
        self.assertEqual(result, "EMP001")

    def test_generate_emp_id_existing(self):
        """Test ID generation with existing employees."""
        result = generate_emp_id(self.test_employees)
        self.assertEqual(result, "EMP004")

    def test_add_employee(self):
        """Test adding a new employee."""
        new_emp = add_employee("Jane Wilson", "Marketing", "Designer")
        self.assertEqual(new_emp.emp_id, "EMP004")
        self.assertEqual(new_emp.name, "Jane Wilson")
        # Verify it was saved
        employees = load_employees()
        self.assertEqual(len(employees), 4)

    def test_search_employee_by_name(self):
        """Test searching employee by name."""
        results = search_employee("Alice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Alice Smith")

    def test_search_employee_by_department(self):
        """Test searching employee by department."""
        results = search_employee("IT")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].department, "IT")

    def test_search_employee_by_id(self):
        """Test searching employee by ID."""
        results = search_employee("EMP003")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Robert Brown")

    def test_search_employee_not_found(self):
        """Test searching for non-existent employee."""
        results = search_employee("NonExistent")
        self.assertEqual(len(results), 0)

    def test_update_employee(self):
        """Test updating employee details."""
        result = update_employee("EMP001", name="John Updated")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "John Updated")
        # Verify persistence
        employees = load_employees()
        self.assertEqual(employees[0].name, "John Updated")

    def test_update_employee_not_found(self):
        """Test updating non-existent employee."""
        result = update_employee("EMP999", name="Ghost")
        self.assertIsNone(result)

    def test_delete_employee(self):
        """Test deleting an employee."""
        result = delete_employee("EMP002")
        self.assertTrue(result)
        employees = load_employees()
        self.assertEqual(len(employees), 2)

    def test_delete_employee_not_found(self):
        """Test deleting non-existent employee."""
        result = delete_employee("EMP999")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
