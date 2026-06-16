# 🏢 Employee Management System

[![Notification Pipeline](https://github.com/Siva9664/test_git_repo/actions/workflows/every-push.yml/badge.svg)](https://github.com/Siva9664/test_git_repo/actions/workflows/every-push.yml)
[![Pytest Suite CI](https://github.com/Siva9664/test_git_repo/actions/workflows/pytest-ci.yml/badge.svg)](https://github.com/Siva9664/test_git_repo/actions/workflows/pytest-ci.yml)
[![Syntax Build Verification](https://github.com/Siva9664/test_git_repo/actions/workflows/syntax-validation.yml/badge.svg)](https://github.com/Siva9664/test_git_repo/actions/workflows/syntax-validation.yml)

An industry-standard Command Line Interface (CLI) application developed in Python to manage employee records. The system utilizes structured JSON persistence, features input validation, department-wise filtering, statistics aggregation, and includes a full suite of automated unit tests.

---

## 🚀 Key Features

* **CRUD Operations:** Easily add, view, update, and delete employee records.
* **Structured Storage:** Automatically saves records to `employees.json` for persistence.
* **Advanced Filters:** List employees by specific departments.
* **System Stats:** View real-time totals and department-wise employee counts.
* **Input Validation:** Restricts empty fields or incorrect formats.
* **CI/CD Integration:** Automatically validates Python syntax and runs test suites via GitHub Actions.

---

## 📁 Project Structure

```
employee-management-system/
├── .github/
│   └── workflows/
│       ├── every-push.yml          # Trigger Notification Workflow
│       ├── pytest-ci.yml           # Automated Testing Workflow
│       └── syntax-validation.yml   # Build Syntax Verification
├── tests/
│   ├── __init__.py
│   └── test_employee_manager.py    # Pytest unit tests
├── .gitignore                      # Git ignored files configuration
├── README.md                       # Comprehensive guide
├── requirements.txt                # Project dependencies
├── app.py                          # Main CLI application
├── employee_manager.py             # Business logic & JSON storage
└── employees.json                  # Persistent JSON storage
```

---

## 🛠️ Installation Instructions

### Prerequisites
* Python 3.11 or higher
* Git

### Step-by-Step Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Siva9664/test_git_repo.git
   cd test_git_repo
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage Examples

To run the application:
```bash
python app.py
```

### Main CLI Interface
```text
=============================================
      🏢 EMPLOYEE MANAGEMENT SYSTEM
=============================================
  1. Add Employee
  2. View All Employees
  3. Search Employee by ID
  4. Update Employee Details
  5. Delete Employee
  6. List Employees by Department
  7. View Employee Statistics
  8. Exit
=============================================
```

---

## 🧪 Running Tests

To run the automated test suite locally:
```bash
# Install pytest first
pip install pytest

# Run the test suite
pytest tests/ -v
```

---

## 🤝 Contribution Guidelines

This repository follows the **Git Feature Branch Workflow**.
1. Create a descriptive issue on GitHub describing your work.
2. Fork the repository or create a new branch locally:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Implement your changes, write tests, and commit with meaningful messages (e.g., `feat: add department listing`).
4. Ensure all local tests pass.
5. Push your branch to remote and open a Pull Request targeting the `develop` branch.
