# Python Best Practices

This document outlines best practices for organizing, coding, and maintaining Python projects. By following these guidelines, developers can ensure consistency, readability, and maintainability across projects.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Coding Standards](#coding-standards)
3. [File and Directory Naming](#file-and-directory-naming)
4. [Version Control](#version-control)
5. [Dependencies Management](#dependencies-management)
6. [Testing](#testing)
7. [Documentation](#documentation)
8. [Error Handling](#error-handling)
9. [Logging](#logging)
10. [Security Practices](#security-practices)
11. [Code Reviews](#code-reviews)

---

## 1. Project Structure

Follow a standard directory structure for all projects:

```
project_name/
├── src/               # Source code
│   ├── __init__.py    # Makes src a Python package
│   └── main.py        # Entry point script
├── tests/             # Unit and integration tests
│   └── test_main.py   # Example test file
├── docs/              # Documentation
├── configs/           # Configuration files
├── logs/              # Log files
├── dist/              # Distributions or build outputs
├── requirements.txt   # List of Python dependencies
├── README.md          # Project overview and instructions
└── .gitignore         # Files and directories to exclude from version control
```

---

## 2. Coding Standards

- **PEP 8 Compliance**: Adhere to the Python Enhancement Proposal 8 (PEP 8) guidelines for code formatting.
    - Use 4 spaces for indentation.
    - Limit lines to 79 characters.
    - Use meaningful variable and function names.

- **Docstrings**: Use docstrings to document all functions, classes, and modules.
    ```python
    def example_function(arg1, arg2):
        """
        Description of the function.

        Args:
            arg1 (type): Description of arg1.
            arg2 (type): Description of arg2.

        Returns:
            type: Description of the return value.
        """
    ```

- **Type Hints**: Use type hints for function arguments and return values.
    ```python
    def add_numbers(a: int, b: int) -> int:
        return a + b
    ```

---

## 3. File and Directory Naming

- Use lowercase letters with underscores (`_`) for file and directory names.
- Avoid using spaces or special characters in names.
- Example: `my_project/`, `data_processing.py`.

---

## 4. Version Control

- Use Git for version control.
- Commit messages should be clear and concise:
    - **Format**: `<type>: <description>`
    - Types: `feat` (feature), `fix` (bug fix), `docs` (documentation), `style` (formatting), `test` (testing), `refactor` (code changes), `chore` (maintenance).
    - Example: `fix: resolve edge case in data parser`.

- Create a `.gitignore` file to exclude unnecessary files from version control:
    ```
    # Example .gitignore
    __pycache__/
    *.pyc
    .env
    .vscode/
    ```

---

## 5. Dependencies Management

- Use a `requirements.txt` file to list all project dependencies:
    ```
    flask==2.0.1
    requests==2.26.0
    ```

- Install dependencies using:
    ```bash
    pip install -r requirements.txt
    ```

---

## 6. Testing

- Write tests for all critical functionality.
- Use a testing framework like `unittest` or `pytest`.
- Place all test files in the `tests/` directory.
- Example test structure:
    ```python
    import unittest
    from src.main import add_numbers

    class TestMathFunctions(unittest.TestCase):
        def test_add_numbers(self):
            self.assertEqual(add_numbers(2, 3), 5)
    ```

---

## 7. Documentation

- Maintain a `README.md` file with:
    - Project description
    - Installation instructions
    - Usage examples
    - Contribution guidelines

- Use inline comments to explain complex logic.

---

## 8. Error Handling

- Use `try-except` blocks to handle errors gracefully.
- Avoid using bare `except` statements; specify the exception type.
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    ```

---

## 9. Logging

- Use the `logging` module instead of `print` statements for tracking application behavior.
- Example logging setup:
    ```python
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Application started.")
    ```

---

## 10. Security Practices

- **Environment Variables**: Store sensitive data (e.g., API keys) in `.env` files and use `python-dotenv` to load them.
- **Input Validation**: Validate all user inputs to prevent injection attacks.
- **Dependency Updates**: Regularly update dependencies to patch vulnerabilities.

---

## 11. Code Reviews

- Peer-review all code changes before merging.
- Focus on:
    - Code readability and maintainability.
    - Adherence to best practices.
    - Performance improvements.

---

## Additional Resources

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Pytest Documentation](https://docs.pytest.org/)

---

This template ensures consistency and quality across Python projects. Always adapt these guidelines to your specific project needs.
