# 🐍 Python - Advanced OOP: Abstract Classes & Interfaces

Welcome to this project on **Advanced Object-Oriented Programming (OOP) in Python**! 🐍  
Here, you'll explore **abstract classes**, **interfaces**, **duck typing**, **multiple inheritance**, and **mixins**, equipping you with essential OOP skills for designing robust Python applications.

---

## 📜 Table of Contents

1. [📖 Introduction](#-introduction)  
2. [🎯 Learning Goals](#-learning-goals)  
3. [⚙️ Prerequisites](#-prerequisites)  
4. [📂 Project Structure](#-project-structure)  
5. [📚 Recommended Resources](#-recommended-resources)  
6. [🚀 Running the Project](#-running-the-project)  
7. [📝 Task Breakdown](#-task-breakdown)  
   - [0. Defining an Abstract Animal Class](#0-defining-an-abstract-animal-class)  
   - [1. Implementing Shapes with Duck Typing](#1-implementing-shapes-with-duck-typing)  
   - [2. Enhancing Python Lists](#2-enhancing-python-lists)  
   - [3. Tracking Iteration with CountedIterator](#3-tracking-iteration-with-countediterator)  
   - [4. Combining Behaviors with Multiple Inheritance](#4-combining-behaviors-with-multiple-inheritance)  
   - [5. Leveraging Mixins for Code Reusability](#5-leveraging-mixins-for-code-reusability)  
8. [🤝 Contribution Guidelines](#-contribution-guidelines)  

---

## 📖 Introduction

This project is designed to help you **master key OOP principles** in Python, including:  

- 🏛 **Abstract Base Classes (ABCs) & Interfaces**  
- 🦆 **Duck Typing & Polymorphism**  
- 🔗 **Inheritance & Method Overriding**  
- 🎭 **Multiple Inheritance & Method Resolution Order (MRO)**  
- 🧩 **Mixins for Modular Code Design**  

By the end, you'll be comfortable with **structuring scalable and maintainable Python applications**! 🚀  

---

## 🎯 Learning Goals

Through this project, you will:  

✔ **Use Abstract Base Classes (ABCs)** with Python’s `abc` module.  
✔ **Implement Interfaces & Duck Typing** for flexible design patterns.  
✔ **Extend Built-in Classes** to customize functionality.  
✔ **Master Multiple Inheritance & MRO** for complex class hierarchies.  
✔ **Use Mixins Effectively** for code reuse across different classes.  

---

## ⚙️ Prerequisites

### **Python Environment**
- **Python Version:** Python 3.8+  
- **Code Style:** PEP 8 compliant (`pycodestyle` recommended)  
- **Execution:**  
  - All scripts must start with:  
    ```python
    #!/usr/bin/python3
    ```
  - Ensure scripts are **executable** (`chmod +x script.py`)  

### **Documentation**
- Use **Google-style Python docstrings** for:  
  - **Modules**, **Classes**, **Methods**, and **Functions**  

---

## 📂 Project Structure

### 0️⃣ Abstract Animal Class and its Subclasses
📌 **File:** `task_00_abc.py`  
🏛 **Concepts:** Abstract Classes, Method Overriding  

✔ Create an **abstract class** `Animal` with an abstract method `sound()`.  
✔ Implement two subclasses:  
   - `Dog` → Returns `"Bark"`  
   - `Cat` → Returns `"Meow"`  

---

### 1️⃣ Shapes, Interfaces, and Duck Typing
📌 **File:** `task_01_duck_typing.py`  
🦆 **Concepts:** Interfaces, Duck Typing  

✔ Create an **abstract class** `Shape` with methods `area()` & `perimeter()`.  
✔ Implement two concrete classes:  
   - `Circle(radius)`  
   - `Rectangle(width, height)`  
✔ Define a **duck-typed function** `shape_info(shape)`.  

---

### 2️⃣ Extending the Python List with Notifications
📌 **File:** `task_02_verboselist.py`  
📜 **Concepts:** Inheritance, Overriding Built-in Methods  

✔ Create a subclass `VerboseList` extending Python’s `list`.  
✔ Override `append()`, `extend()`, `remove()`, and `pop()` to print messages.  

---

### 3️⃣ CountedIterator - Keeping Track of Iteration
📌 **File:** `task_03_countediterator.py`  
🔄 **Concepts:** Custom Iterators  

✔ Extend Python’s `iter()` to track the number of iterated items.  
✔ Implement a **custom iterator** `CountedIterator`.  

---

### 4️⃣ The Enigmatic FlyingFish - Exploring Multiple Inheritance
📌 **File:** `task_04_flyingfish.py`  
🦅🐟 **Concepts:** Multiple Inheritance, Method Resolution Order (MRO)  

✔ Create classes `Fish` & `Bird` with `swim()`, `fly()`, and `habitat()`.  
✔ Create `FlyingFish` inheriting from both.  

---

### 5️⃣ The Mystical Dragon - Mastering Mixins
📌 **File:** `task_05_dragon.py`  
🧩 **Concepts:** Mixins, Code Reusability  

✔ Implement mixins `SwimMixin` & `FlyMixin`.  
✔ Create a `Dragon` class inheriting from both mixins.  

---

## 📚 Recommended Resources

### **Articles & Docs**

-   📖 [Abstract Base Classes (ABCs) in Python](https://docs.python.org/3/library/abc.html)
-   🔹 [Understanding Duck Typing](https://realpython.com/lessons/duck-typing/)
-   🦆 [OOP Principles in Python](https://realpython.com/python3-object-oriented-programming/)

### **Videos & Tutorials**

-   🎥 [Corey Schafer - OOP Series](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)

## 🤝 Contribution 

🚀 **Want to contribute?**  

1️⃣ Fork the repository.  
2️⃣ Create a new branch:  
   ```bash
   git checkout -b feature-branch-name
   ```
3️⃣ Commit your changes:  
   ```bash
   git commit -m "Add a new feature"
   ```
4️⃣ Push to your branch:  
   ```bash
   git push origin feature-branch-name
   ```
5️⃣ Open a **Pull Request**!  

---