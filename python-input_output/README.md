# 📂 Python - Input/Output

![Python](https://img.shields.io/badge/Python-3.8.5-blue) ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-orange)

## 🏆 Project Overview  

This project covers **file handling** and **JSON serialization/deserialization** in Python. By the end, you'll master:  
✅ Opening, reading, writing, and closing files.  
✅ Using the `with` statement for proper file handling.  
✅ Manipulating JSON data in Python.  
✅ Working with command-line arguments.  

## 📚 Resources  

🔗 [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)  
🔗 [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)  
🔗 [Dive Into Python 3 - Files](https://diveintopython3.net/files.html)  
🔗 [Automate the Boring Stuff - Reading/Writing Files](https://automatetheboringstuff.com/)  
🔗 [JSON Encoder and Decoder](https://docs.python.org/3/library/json.html)  
🔗 [sys package](https://docs.python.org/3/library/sys.html)  

---

## 🎯 Learning Objectives  

🔹 Understand why Python programming is awesome!  
🔹 Read and write files in Python.  
🔹 Handle file cursors and proper file closing.  
🔹 Work with JSON: serialization & deserialization.  
🔹 Use command-line arguments in scripts.  

---

## ⚙️ Requirements  

### 🐍 Python Scripts  
✔️ Python 3.8.5 (Ubuntu 20.04 LTS)  
✔️ Use `#!/usr/bin/python3` as the first line in scripts.  
✔️ Follow **pycodestyle** (`v2.7.*`).  
✔️ All files must be executable.  
✔️ Include a `README.md` at the root of the project.  

### 📝 Test Cases  
✔️ Store test files in a `tests/` directory.  
✔️ Run tests using:  
```sh
python3 -m doctest ./tests/*
```
✔️ Ensure all modules, classes, and functions have proper docstrings.

## 🚀 Tasks

### 0️⃣ Read a File

📜 **Function:** `read_file(filename="")`  
🔹 Reads a text file (UTF-8) and prints it to `stdout`.  
🔹 Uses the `with` statement for file handling.

----------

### 1️⃣ Write to a File

📜 **Function:** `write_file(filename="", text="")`  
🔹 Writes a string to a file and returns the number of characters written.  
🔹 Creates a new file if it doesn’t exist.  
🔹 Overwrites the file if it already exists.

----------

### 2️⃣ Append to a File

📜 **Function:** `append_write(filename="", text="")`  
🔹 Appends a string at the end of a file.  
🔹 Creates a new file if it doesn’t exist.

----------

### 3️⃣ Convert Object to JSON

📜 **Function:** `to_json_string(my_obj)`  
🔹 Returns the JSON representation of an object as a string.

----------

### 4️⃣ Convert JSON to Object

📜 **Function:** `from_json_string(my_str)`  
🔹 Parses a JSON string and returns a Python object.

----------

### 5️⃣ Save Object to File

📜 **Function:** `save_to_json_file(my_obj, filename)`  
🔹 Saves a Python object to a file using JSON format.

----------

### 6️⃣ Load Object from File

📜 **Function:** `load_from_json_file(filename)`  
🔹 Loads an object from a JSON file.

----------

### 7️⃣ Load, Add, Save

📜 **Script:** `7-add_item.py`  
🔹 Adds command-line arguments to a Python list and saves them in `add_item.json`.

----------

### 8️⃣ Class to JSON

📜 **Function:** `class_to_json(obj)`  
🔹 Returns the dictionary description of an object for JSON serialization.

----------

### 9️⃣ Student Class to JSON

📜 **Class:** `Student`  
🔹 Attributes: `first_name`, `last_name`, `age`.  
🔹 Converts to a dictionary for JSON serialization.

----------

### 🔟 Student Class with Attribute Filtering

📜 **Method:** `to_json(self, attrs=None)`  
🔹 Retrieves a dictionary representation with optional attribute filtering.

----------

### 1️⃣1️⃣ Student Serialization & Deserialization

📜 **Method:** `reload_from_json(self, json)`  
🔹 Loads attributes from a dictionary.

----------

### 1️⃣2️⃣ Pascal's Triangle

📜 **Function:** `pascal_triangle(n)`  
🔹 Generates Pascal’s Triangle up to `n` rows.

## 📁 Repository Structure

```sh
📂 holbertonschool-higher_level_programming
└── 📂 python-input_output
    ├── 📄 0-read_file.py
    ├── 📄 1-write_file.py
    ├── 📄 2-append_write.py
    ├── 📄 3-to_json_string.py
    ├── 📄 4-from_json_string.py
    ├── 📄 5-save_to_json_file.py
    ├── 📄 6-load_from_json_file.py
    ├── 📄 7-add_item.py
    ├── 📄 8-class_to_json.py
    ├── 📄 9-student.py
    ├── 📄 10-student.py
    ├── 📄 11-student.py
    ├── 📄 12-pascal_triangle.py
    └── 📄 README.md
```
## 🤝 Contributing

💡 Contributions are welcome! If you'd like to contribute:

1.  **Fork** the repository.
2.  **Create a new branch**:
```sh
git checkout -b feature-branch
```
3. **Commit your changes**:
```sh
git commit -m "Add new feature"
```
4. **Push to the branch**:
```sh
git push origin feature-branch
```
5. **Submit a Pull Request** 🚀