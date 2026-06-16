# 🏢 Employee Management System

A command-line Employee Management Application built with Python for managing employee records efficiently.

## 📋 Features

- ✅ **Add Employee** – Register new employees with ID, name, department, and position
- ✅ **View Employees** – Display all employee records in a formatted table
- ✅ **Search Employee** – Find employees by ID, name, or department
- ✅ **Update Employee** – Modify existing employee details
- ✅ **Delete Employee** – Remove employee records
- ✅ **Persistent Storage** – Employee data saved to `employees.txt`

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/employee-management-system.git

# Navigate to the project directory
cd employee-management-system

# Run the application
python app.py
```

## 📁 Project Structure

```
employee-management-system/
│
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── app.py                 # Main application with menu system
├── employee.py            # Employee class definition
├── employee_manager.py    # Core CRUD operations
├── utils.py               # Utility/helper functions
├── employees.txt          # Employee data storage
├── tests/
│   └── test_employee.py   # Unit tests
└── .github/
    └── workflows/
        └── python-app.yml # GitHub Actions CI/CD
```

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

## 🌿 Branch Strategy

| Branch | Description |
|--------|-------------|
| `main` | Stable production code |
| `develop` | Integration branch |
| `feature-add-employee` | Add employee feature |
| `feature-delete-employee` | Delete employee feature |
| `feature-search-employee` | Search employee feature |
| `feature-update-employee` | Update employee feature |

## 👥 Sample Employee Data

| Employee ID | Name          | Department | Position          |
|-------------|---------------|------------|-------------------|
| EMP001      | John Doe      | HR         | Manager           |
| EMP002      | Alice Smith   | IT         | Software Engineer |
| EMP003      | Robert Brown  | Finance    | Accountant        |

## 📝 Git Workflow

This project follows the **Git Feature Branch Workflow**:

1. Create a feature branch from `develop`
2. Make changes and commit
3. Push the branch and create a Pull Request
4. Review, resolve conflicts if any, and merge
5. Tag releases on `main`

## 🏷️ Releases

- `v1.0.0` – Initial release with basic CRUD operations
- `v1.1.0` – Added search functionality
- `v1.2.0` – Added update functionality

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

- **Siva** – AIML Department, AI Intern
