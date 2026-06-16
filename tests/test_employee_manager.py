"""
pytest unit tests for employee_manager.py
Covers employee creation, update, deletion, search, listing, and statistics.
"""

import os
import pytest
import employee_manager


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Fixture to reset the database file before and after each test."""
    # Backup original DATA_FILE path if it exists
    original_file = employee_manager.DATA_FILE
    employee_manager.DATA_FILE = "test_employees.json"

    # Ensure clean state
    if os.path.exists(employee_manager.DATA_FILE):
        os.remove(employee_manager.DATA_FILE)

    yield

    # Clean up after test
    if os.path.exists(employee_manager.DATA_FILE):
        os.remove(employee_manager.DATA_FILE)

    employee_manager.DATA_FILE = original_file


def test_add_employee():
    """Test adding a new employee record."""
    emp_id, msg = employee_manager.add_employee(
        "Siva", "AIML", "AI Intern"
    )
    assert emp_id == "EMP001"
    assert "successfully" in msg

    # Verify data in DB
    record = employee_manager.search_employee("EMP001")
    assert record is not None
    assert record["name"] == "Siva"
    assert record["department"] == "AIML"
    assert record["position"] == "AI Intern"


def test_add_employee_invalid():
    """Test validation constraints on employee input."""
    # Empty name
    emp_id, msg = employee_manager.add_employee("", "IT", "Engineer")
    assert emp_id is None
    assert "name" in msg.lower()

    # Empty department
    emp_id, msg = employee_manager.add_employee("John", "   ", "Engineer")
    assert emp_id is None
    assert "department" in msg.lower()


def test_search_employee():
    """Test searching for an employee record."""
    # Add a mock record
    employee_manager.add_employee("Alice Smith", "IT", "Engineer")

    record = employee_manager.search_employee("EMP001")
    assert record is not None
    assert record["name"] == "Alice Smith"
    assert record["id"] == "EMP001"

    # Search non-existing
    record_none = employee_manager.search_employee("EMP999")
    assert record_none is None


def test_update_employee():
    """Test updating details of an existing employee."""
    employee_manager.add_employee("Robert Brown", "Finance", "Accountant")

    # Perform partial update
    success, msg = employee_manager.update_employee(
        "EMP001", name="Bob Brown", position="Lead Accountant"
    )
    assert success is True
    assert "updated successfully" in msg

    # Verify updates
    record = employee_manager.search_employee("EMP001")
    assert record["name"] == "Bob Brown"
    assert record["position"] == "Lead Accountant"
    assert record["department"] == "Finance"  # Unchanged


def test_update_employee_not_found():
    """Test updating details of a non-existent employee."""
    success, msg = employee_manager.update_employee(
        "EMP999", name="Ghost"
    )
    assert success is False
    assert "not found" in msg.lower()


def test_delete_employee():
    """Test deleting an employee record."""
    employee_manager.add_employee("Jane Doe", "HR", "Recruiter")

    # Delete existing
    success, msg = employee_manager.delete_employee("EMP001")
    assert success is True
    assert "deleted successfully" in msg

    # Verify deletion
    record = employee_manager.search_employee("EMP001")
    assert record is None


def test_delete_employee_not_found():
    """Test deleting a non-existent employee."""
    success, msg = employee_manager.delete_employee("EMP999")
    assert success is False
    assert "not found" in msg.lower()


def test_list_by_department():
    """Test department filtering."""
    employee_manager.add_employee("Dev A", "IT", "Dev")
    employee_manager.add_employee("Dev B", "IT", "QA")
    employee_manager.add_employee("Manager C", "HR", "Lead")

    it_list = employee_manager.list_by_department("IT")
    assert len(it_list) == 2
    assert "EMP001" in it_list
    assert "EMP002" in it_list

    hr_list = employee_manager.list_by_department("HR")
    assert len(hr_list) == 1
    assert "EMP003" in hr_list


def test_statistics():
    """Test generation of stats."""
    # Empty database stats
    empty_stats = employee_manager.get_statistics()
    assert empty_stats["total"] == 0

    # Populated database stats
    employee_manager.add_employee("E1", "IT", "Pos")
    employee_manager.add_employee("E2", "IT", "Pos")
    employee_manager.add_employee("E3", "HR", "Pos")

    stats = employee_manager.get_statistics()
    assert stats["total"] == 3
    assert stats["departments"]["IT"] == 2
    assert stats["departments"]["HR"] == 1
