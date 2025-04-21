# 🐍 Python - Everything is Object

## 📘 Description

Welcome to a deep dive into the heart of Python!  
This project is different from others. It focuses on understanding how Python handles objects, references, and the underlying mechanics that drive variable behavior.

### ⚠️ Ever experienced this?

```python
a = 1
b = a
a = 2
print(b)  # ➡️ 1
```

No surprise there. But what about:

```python
l = [1, 2, 3]
m = l
l[0] = 'x'
print(m)  # ➡️ ['x', 2, 3]
```

😲 Boom. Mutability in action!

## 🧠 Background Context

Now that we know everything in Python is an **object**, let's take time to understand what that really means.  
Before you write a single line of code, **read all the resources**, **think deeply**, and **try to reason through each scenario**. Use the interpreter _only at the end_ to verify your thoughts.

This is exactly the kind of logic you'll need to explain in interviews for Python roles.  
Take your time — it will pay off!

## 🎯 Learning Objectives

By the end of this project, you should be able to confidently answer (without Googling!):

- 🤔 What is an object?
- 🆚 Difference between a class and an instance?
- 🔄 What is the difference between mutable and immutable objects?
- 🎯 What is a reference?
- ➕ What is an assignment?
- 🧍 What is an alias?
- ✅ How to check if two variables are identical?
- 🔗 How to check if two variables point to the same object?
- 🧠 How to print a variable’s ID (memory address)?
- 🔁 What are mutable and immutable types?
- 📦 Built-in mutable types in Python?
- 🔐 Built-in immutable types in Python?
- 📤 How does Python pass variables to functions?

## 📚 Resources

Make sure you’ve read:

- [9.10. Objects and values](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [9.11. Aliasing](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python)
- Immutable vs mutable types
- [Mutation (Only this chapter)](https://docs.python.org/3/reference/datamodel.html#object.__setattr__)
- [9.12. Cloning lists](https://docs.python.org/3/faq/programming.html#how-do-i-copy-an-object-in-python)
- [Python tuples: immutable but potentially changing](https://stackoverflow.com/questions/4827393/python-tuples-immutable-but-their-contents-may-not-be)

## ✅ Requirements

### 🐍 Python Scripts

- ✅ Allowed editors: `vi`, `vim`, `emacs`
- ✅ Interpreted with **Python 3.8.5** on Ubuntu 20.04 LTS
- ✅ Each file must end with a new line
- ✅ First line must be: `#!/usr/bin/python3`
- ✅ Must pass `pycodestyle` (version `2.7.*`)
- ✅ All files must be executable
- ✅ File length will be tested using `wc`

### 📄 Answer Files (`.txt`)

- ✅ Only one line per file
- 🚫 No Shebang (`#!/usr/bin/python3`)
- ✅ Each file must end with a new line

🧠 **Tip:** This project is about understanding, not coding. Take your time, think hard, and explain each behavior clearly.  
💬 Don’t hesitate to discuss with peers, but make sure you can explain _why_ an answer is what it is.

Good luck! 🚀
