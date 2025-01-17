# Python - Import & Modules

## Description
This project introduces the fundamental concepts of importing and using modules in Python. It explores how to write reusable code, leverage built-in Python modules, and execute scripts with command-line arguments.

## Resources
### Read or Watch:
- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command Line Arguments](https://docs.python.org/3/library/sys.html#sys.argv)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

### Manual Pages:
- `python3`

## Learning Objectives
By the end of this project, you will be able to:
- Explain why Python programming is awesome.
- Import functions from another file.
- Use imported functions effectively.
- Create and use your own modules.
- Use the built-in function `dir()`.
- Prevent execution of code in a script when imported.
- Utilize command-line arguments in Python programs.

## Requirements
### General:
- Editors allowed: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on **Ubuntu 22.04 LTS** using Python 3 (version 3.10.*).
- All files must end with a new line.
- The first line of all Python files must be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code must follow the [pycodestyle](https://pypi.org/project/pycodestyle/) (version 2.7.*).
- All files must be executable.
- File lengths will be tested using the `wc` command.

## Tasks

### 0. Import a Simple Function from a Simple File
Write a program that imports the function `def add(a, b):` from `add_0.py` and prints the result of the addition `1 + 2 = 3`.

**Requirements:**
- Use `print` with string formatting.
- Use the variables `a` and `b` for arguments.
- Do not execute code when imported.

### 1. My First Toolbox!
Write a program that imports functions from `calculator_1.py`, performs basic arithmetic, and prints the results.

**Requirements:**
- Use `print` no more than four times.
- Use only the variables `a` and `b` for function calls.
- Call each arithmetic function exactly once.

### 2. How to Make a Script Dynamic!
Write a program that prints the number of and list of its command-line arguments.

**Requirements:**
- Print the number of arguments, followed by their list.
- Format output to show the position and value of each argument.

### 3. Infinite Addition
Write a program that calculates and prints the sum of all command-line arguments.

**Requirements:**
- Handle integers cast from strings.
- Handle large numbers without overflow.

### 4. Who Are You?
Write a program that prints all the names defined in the compiled `hidden_4.pyc` module, except those starting with `__`.

**Requirements:**
- Display names in alphabetical order.
- Skip names starting with `__`.

### 5. Everything can be imported 
Write a program that imports the variable a from the file `variable_load_5.py` and prints its value.

**Requirements:**
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported


---

## Repository
- **GitHub Repository:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming)
- **Directory:** `python-import_modules`
- Files:
  - `0-add.py`
  - `1-calculation.py`
  - `2-args.py`
  - `3-infinite_add.py`
  - `4-hidden_discovery.py`
  - `5-variable_load.py`
 