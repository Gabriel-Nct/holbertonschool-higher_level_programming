# Python Exceptions 🚀

## 📖 Description

This project dives into **Python exceptions**, exploring how to handle errors gracefully in your Python programs. By the end of this project, you'll understand the difference between errors and exceptions, how to handle them properly, and even how to raise custom exceptions when needed.

---

## 🧠 Learning Objectives

By completing this project, you will be able to explain the following concepts:

- Why Python programming is awesome. 🐍✨
- The difference between **errors** and **exceptions**.
- What exceptions are and how to use them effectively.
- When and why exceptions are necessary.
- How to correctly handle exceptions using `try` / `except` blocks.
- The purpose of catching exceptions in your code.
- How to raise built-in exceptions with the `raise` statement.
- When and how to implement clean-up actions using `finally`.

---

## 🛠️ Requirements

### General

- **Allowed editors**: `vi`, `vim`, `emacs`.
- All code will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version **3.8.5**).
- Every file must end with a new line.
- The first line of all scripts must be `#!/usr/bin/python3`.
- **A `README.md` file at the root of the project is mandatory.**
- Code must conform to **pycodestyle** (version **2.7.\***).
- All files must be executable.
- The length of your files will be tested using `wc`.

---

## 📂 Project Tasks

### 0. Safe list printing 📜
Write a function that prints `x` elements of a list.

- **Prototype**: `def safe_print_list(my_list=[], x=0):`
- Uses `try` / `except` to handle out-of-range errors.
- Does **not** import any modules or use `len()`.

📝 **File**: `0-safe_print_list.py`

---

### 1. Safe printing of an integers list 🔢
Write a function that prints an integer using `"{:d}".format()`.

- **Prototype**: `def safe_print_integer(value):`
- Returns `True` if the value is an integer, otherwise `False`.
- Does **not** use `type()` or import any modules.

📝 **File**: `1-safe_print_integer.py`

---

### 2. Print and count integers 🔢🧮
Write a function that prints the first `x` elements of a list, only if they are integers.

- **Prototype**: `def safe_print_list_integers(my_list=[], x=0):`
- Prints integers in the list, ignoring other types.
- Handles `IndexError` if `x` exceeds the list length.

📝 **File**: `2-safe_print_list_integers.py`

---

### 3. Integers division with debug ➗
Write a function that divides two integers and prints the result.

- **Prototype**: `def safe_print_division(a, b):`
- Prints the result in the `finally` block as `Inside result: <value>`.
- Returns the division result or `None` if division fails.

📝 **File**: `3-safe_print_division.py`

---

### 4. Divide a list ➗📋
Write a function that divides element by element two lists.

- **Prototype**: `def list_division(my_list_1, my_list_2, list_length):`
- Returns a new list containing the results of the divisions.
- Handles:
  - `ZeroDivisionError` → prints `division by 0`.
  - `TypeError` → prints `wrong type`.
  - `IndexError` → prints `out of range`.

📝 **File**: `4-list_division.py`

---

### 5. Raise exception 🚩
Write a function that raises a type exception.

- **Prototype**: `def raise_exception():`
- Raises a `TypeError` intentionally.

📝 **File**: `5-raise_exception.py`

---

### 6. Raise a message 🗨️
Write a function that raises a `NameError` with a custom message.

- **Prototype**: `def raise_exception_msg(message=""):`
- Raises a `NameError` with the specified message.

📝 **File**: `6-raise_exception_msg.py`




## 💡 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/holbertonschool-higher_level_programming.git
   cd holbertonschool-higher_level_programming/python-exceptions
   ```
2. Make the scripts executable:
```bash
chmod +x *.py
   ```
3. Run the provided test scripts:
```bash
./0-main.py
   ```