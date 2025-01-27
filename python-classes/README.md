# 🐍 Python - Classes and Objects

Welcome to the **Python - Classes and Objects** project! This project is designed to help you master the foundations of **Object-Oriented Programming (OOP)** in Python. You'll learn how to define and work with **classes**, **objects**, and their attributes/methods while exploring core OOP principles. 🚀

---

## 📖 Learning Objectives  

By completing this project, you'll be able to explain and implement the following concepts with confidence:

### 🏛️ General OOP Principles  
- **What is OOP?**: Programming based on objects and their interactions.  
- **First-class everything**: Everything in Python (functions, classes, objects) is treated as first-class citizens.  

### 🧱 Classes and Objects  
- **What is a class?**: A blueprint for creating objects.  
- **What is an object?**: An instance of a class, representing a real-world entity.  
- **Difference between a class and an object?**: A class is a definition; an object is an instantiation.  

### 📂 Attributes and Properties  
- **What is an attribute?**: A variable bound to an object or class.  
- **Public, Protected, Private attributes**: Controlling access to attributes using naming conventions.  
- **Properties vs. Getters/Setters**: The Pythonic way to manage attribute access.  

### 🔧 Methods  
- **What is a method?**: A function defined within a class to interact with an object.  
- **The `__init__` method**: A special method to initialize object attributes during instantiation.  
- **Data Abstraction, Encapsulation, and Information Hiding**: Keeping implementation details private while exposing functionality.  

### 🛠 Dynamic Features  
- **Dynamically creating attributes**: Adding new attributes to objects or classes on the fly.  
- **Binding attributes**: Associating attributes with specific objects or classes.  
- **The `__dict__` attribute**: Exploring all attributes stored in a class or object.  

### 🔍 Attribute Management  
- **How Python finds attributes**: Understanding the method resolution order.  
- **Using the `getattr` function**: Dynamically accessing attributes of objects.  

---

## ⚙️ Requirements  

### 🖥️ General  
- Use **Ubuntu 20.04 LTS** and **Python 3.8.5**.  
- All code must follow the **pycodestyle (version 2.7.\*)** standard.  
- Each file must include the shebang: `#!/usr/bin/python3`.  
- Add documentation for **modules**, **classes**, and **methods** following the **Google Style Python Docstrings**.  

### ✅ Files  
- Every file should end with a **newline**.  
- All files must be **executable**.  
- Each module/class/method should include meaningful **docstrings**.  

---

## 📚 Resources  

### Recommended Readings  
Before starting the tasks, read/watch the following resources to understand the concepts thoroughly:  
1. **Object-Oriented Programming**: Basics of OOP (skip the "Inheritance" section).  
2. **Python Classes and Objects**: Learn the minimal syntax to create a class.  
3. **Properties vs. Getters/Setters**: A Pythonic approach to managing attributes.  
4. **Learn to Program 9**: An introduction to OOP with practical examples.

---

## 📋 Tasks  

### 0️⃣ My First Square  
Create an empty class `Square` to define a square.  
- **File**: `0-square.py`

---

### 1️⃣ Square with Size  
Define a private attribute `size` for the square.  
- **File**: `1-square.py`  
- Example:
  ```python
  my_square = Square(3)
  print(my_square.__dict__)
  ```

---

### 2️⃣ Size Validation

Validate the type and value of `size` during initialization.

-   Raise a `TypeError` if size is not an integer.
-   Raise a `ValueError` if size is negative.
-   **File**: `2-square.py`

---

### 3️⃣ Area of a Square

Add a method `area` to calculate the area of the square.

-   **File**: `3-square.py`
-   Example:
```python
my_square = Square(4)
print(my_square.area())
```

---

### 4️⃣ Access and Update Private Attribute

Use getters and setters for managing the `size` attribute.

-   **File**: `4-square.py`
-   Example:
```python
my_square = Square(5)
print(my_square.size)
my_square.size = 10
print(my_square.size)
```

---

### 5️⃣ Printing a Square

Add a my_print method to display the square with #.

-   File: 5-square.py
-   Example:
    ```python
    my_square = Square(3)
    my_square.my_print()
    # Output:
    # ###
    # ###
    # ###
    ```

---

### 6️⃣ Coordinates of a Square

Introduce a `position` attribute to control the square's position.

-   Use spaces to represent the `position`.
-   **File**: `6-square.py`
-   Example:
    ```python
    my_square = Square(3, (1, 1))
    my_square.my_print()
    # Output:
    #
    #  ###
    #  ###
    #  ###
    ```

---

## 🚀 How to Run

-   Clone the repository:
```bash
git clone https://github.com/holbertonschool-higher_level_programming.git
```

-   Navigate to the project directory:
```bash
cd python-classes
```

-   Run the example files:
```bash
./<file_name>.py
```
---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

-   Fork the repository.

-   Create a feature branch:
```bash
git checkout -b feature-branch-name
```
-   Commit your changes:
```bash
git commit -m "Description of changes"
```

-   Push to your branch:
```bash
git push origin feature-branch-name
```

-   Open a pull request.