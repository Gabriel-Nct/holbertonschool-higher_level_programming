# Python - Test-driven Development

## Description

This project focuses on learning and implementing **Test-driven Development (TDD)** in Python. You will explore how to write tests before the actual code, ensuring the reliability and correctness of your programs. This approach emphasizes handling edge cases and creating comprehensive documentation.

By following TDD principles, you will gain hands-on experience with:

-   Writing functional documentation for modules and functions.
-   Designing effective test cases.
-   Handling edge cases gracefully in Python scripts.

## Background Context

Key principles to follow in this project:

1.  Write both **documentation** and **tests** before writing any implementation code.
2.  Intranet checks for Python projects will only be released after the first deadline to encourage TDD practices.
3.  Collaborate with peers to design test cases and cover edge cases effectively, but work on implementations independently.
4.  Never assume user input is correct—think critically about all possible edge cases.

## Resources

To help you through this project, refer to the following resources:

-   [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
-   doctest – Testing through documentation
-   Unit Tests in Python

----------

## Learning Objectives

By the end of this project, you will be able to:

-   Understand why Python programming is powerful and awesome.
-   Define interactive tests and explain their purpose.
-   Recognize the importance of tests and edge-case management.
-   Write effective **Docstrings** for testing purposes.
-   Document modules and functions clearly and thoroughly.
-   Use basic options and flags to create and run tests.
-   Identify and handle edge cases effectively in Python programs.

----------

## Requirements

### Python Scripts

-   Editors allowed: **vi**, **vim**, **emacs**.
-   All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3 (version 3.8.5).
-   Each file must end with a **new line**.
-   The first line of each script must be: `#!/usr/bin/python3`.
-   A `README.md` file is mandatory at the root of the project folder.
-   Code must comply with **pycodestyle** (version 2.7.*).
-   All scripts must be executable.
-   File length will be verified using the `wc` command.

### Python Test Cases

-   Editors allowed: **vi**, **vim**, **emacs**.
-   All test files must end with a **new line**.
-   Test files should reside in a dedicated **tests** folder.
-   Test files must have the `.txt` extension.
-   Use the following command to run tests:
```bash
python3 -m doctest ./tests/*
```
- All modules and functions must include documentation:

    -   For modules:
    ```bash
    python3 -c 'print(__import__("my_module").__doc__)'
    ```
    -   For functions:
    ```bash
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    ```
-   Documentation must be meaningful, clearly explaining the purpose of the module or function.

## Tasks

### Task 0: Integers Addition

Write a function that adds two integers.

-   Prototype: `def add_integer(a, b=98):`
-   Ensure type validation for integers or floats, raising a `TypeError` otherwise.
-   Returns: The integer result of the addition.
-   Constraints: No imports allowed.

### Task 1: Divide a Matrix

Write a function to divide all elements of a matrix by a number.

-   Prototype: `def matrix_divided(matrix, div):`
-   Validate the matrix, its elements, and divisor, raising appropriate exceptions.
-   Returns: A new matrix with elements rounded to two decimal places.

### Task 2: Say My Name

Write a function that prints: `My name is <first name> <last name>`.

-   Prototype: `def say_my_name(first_name, last_name=""):`
-   Validate that both arguments are strings, raising a `TypeError` otherwise.

### Task 3: Print Square

Write a function to print a square using the `#` character.

-   Prototype: `def print_square(size):`
-   Validate the size, ensuring it’s an integer and non-negative.
-   Raise exceptions for invalid input values or types.

### Task 4: Text indentation 

Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

-   Prototype: `def text_indentation(text):`
-   Text must be a string, otherwise raise a TypeError exception with the message text must be a string
-   There should be no space at the beginning or at the end of each printed line

### Task 5: Max integer - Unittest 

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
In this task, you will write unittests for the function

-   Prototype: `def max_integer(list=[]):`
-   Your test file should be inside a folder tests
-   You have to use the unittest module
-   Your test file should be python files (extension: .py)

----------

## Repository

**GitHub repository:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming)  