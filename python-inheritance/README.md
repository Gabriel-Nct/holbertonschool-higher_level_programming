# 🐍 Python - Inheritance

## 📌 Project Overview  
Welcome to the **Python Inheritance** project! 🚀 This project will help you understand the concept of inheritance in Python, allowing you to build more efficient and reusable code.  

By the end of this project, you will be able to explain key inheritance concepts without relying on Google! 🔥  

---

## 📚 Resources  

Here are some useful materials to deepen your understanding:  

- 📖 [Inheritance](https://example.com)  
- 📖 [Multiple inheritance](https://example.com)  
- 📖 [Inheritance in Python](https://example.com)  
- 📖 [Learn to Program 10: Inheritance Magic Methods](https://example.com)  

---

## 🎯 Learning Objectives  

By completing this project, you will learn:  

✅ What is a superclass, base class, or parent class  
✅ What is a subclass  
✅ How to list all attributes and methods of a class or instance  
✅ When an instance can have new attributes  
✅ How to inherit a class from another  
✅ How to define a class with multiple base classes  
✅ What is the default class every class inherits from  
✅ How to override a method or attribute inherited from a base class  
✅ Which attributes or methods are available by heritage to subclasses  
✅ The purpose of inheritance  
✅ When and how to use `isinstance`, `issubclass`, `type`, and `super` functions  

---

## ⚙️ Requirements  

### 🐍 Python Scripts  

- Code editors allowed: `vi`, `vim`, `emacs`  
- All scripts must be interpreted on **Ubuntu 20.04 LTS** with **Python 3.8.5**  
- Each file must end with a new line  
- The first line of all scripts must be: `#!/usr/bin/python3`  
- **PEP 8 style guide** enforced (`pycodestyle` version 2.7.\*)  
- All files must be executable  

### 🧪 Python Test Cases  

- Test files should be stored in the `tests/` directory  
- Tests should be executed using:  
  ```bash
  python3 -m doctest ./tests/*
  ```
- All modules, classes, and functions must have **documentation**

## 📂 Project Structure

```bash
📦 python-inheritance
├── 📄 0-lookup.py
├── 📄 1-my_list.py
├── 📄 2-is_same_class.py
├── 📄 3-is_kind_of_class.py
├── 📄 4-inherits_from.py
├── 📄 5-base_geometry.py
├── 📄 6-base_geometry.py
├── 📄 7-base_geometry.py
├── 📄 8-rectangle.py
├── 📄 9-rectangle.py
├── 📄 10-square.py
├── 📄 11-square.py
└── 📂 tests
```
## 🚀 Getting Started

### 🔹 Clone the repository
```sh
git clone https://github.com/your_username/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-inheritance
```

### 🔹 Run test cases
```sh
python3 -m doctest ./tests/*
```

### 🔹 Run Python scripts
Each script is executable, so you can run them directly:
```sh
./0-lookup.py
```

## 📝 Task Breakdown

### ✅ Task 0: Lookup

Write a function `lookup(obj)` that returns a list of available attributes and methods of an object.

###  ✅ Task 1: My List

Create a class `MyList` that inherits from `list` and adds a method `print_sorted()` that prints a sorted version of the list.

###  ✅ Task 2: Exact same object

Write a function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`.

###  ✅ Task 3: Same class or inherit from

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

###  ✅ Task 4: Only sub class of

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

###  ✅ Task 5: Geometry module

Write an empty class `BaseGeometry`.

###  ✅ Task 6: Improve Geometry

Write a class `BaseGeometry` (based on `5-base_geometry.py`).

###  ✅ Task 7: Integer validator

Write a class `BaseGeometry` (based on `6-base_geometry.py`).

-   Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
-   Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    -   you can assume `name` is always a string
    -   if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    -   if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`

###  ✅ Task 8: Rectangle

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

-   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    -   `width` and `height` must be private. No getter or setter
    -   `width` and `height` must be positive integers, validated by `integer_validator`

###  ✅ Task 9: Full rectangle

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

-   Instantiation with `width` and `height`: `def __init__(self, width, height):`:
    -   `width` and `height` must be private. No getter or setter
    -   `width` and `height` must be positive integers validated by `integer_validator`
-   the `area()` method must be implemented
-   `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

###  ✅ Task 10: Square #1

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

-   Instantiation with `size`: `def __init__(self, size):`:
    -   `size` must be private. No getter or setter
    -   `size` must be a positive integer, validated by `integer_validator`
-   the `area()` method must be implemented

###  ✅ Task 11: Square #2

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

-   Instantiation with `size`: `def __init__(self, size):`:
    -   `size` must be private. No getter or setter
    -   `size` must be a positive integer, validated by `integer_validator`
-   the `area()` method must be implemented
-   `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

## 🤝 Contributing

Contributions are welcome! Feel free to open a pull request or suggest improvements via issues.

## 📜 License

This project is part of **Holberton School's higher-level programming curriculum**.
