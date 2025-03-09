# Python Object-Relational Mapping (ORM)

## 🚀 Project Overview

Welcome to the **Python ORM** project! In this project, we will bridge the gap between **Databases** and **Python** by utilizing **MySQLdb** and **SQLAlchemy**.

### 🎯 Key Objectives:

-   Learn how to connect to a MySQL database using Python
    
-   Perform SQL queries using both raw SQL and ORM techniques
    
-   Understand how to map Python classes to MySQL tables
    
-   Ensure code reusability and abstraction by avoiding direct SQL queries
    

----------

## 🛠 Prerequisites

Before starting, ensure your MySQL server is version **8.0**.

-   **How to install MySQL 8.0 on Ubuntu 20.04:**
    
    ```
    $ sudo apt update
    $ sudo apt install mysql-server
    $ mysql --version
    ```
    
-   **Connect to MySQL server:**
    
    ```
    $ sudo mysql
    mysql> quit
    ```
    
-   **Install MySQLdb module (v2.0.x):**
    
    ```
    $ sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
    $ sudo pip3 install mysqlclient
    ```
    
    ```
    >>> import MySQLdb
    >>> MySQLdb.version_info  
    (2, 0, 3, 'final', 0)
    ```
    
-   **Install SQLAlchemy module (v1.4.x):**
    
    ```
    $ sudo pip3 install SQLAlchemy
    ```
    
    ```
    >>> import sqlalchemy
    >>> sqlalchemy.__version__  
    '1.4.22'
    ```
    

----------

## 📌 Learning Objectives

At the end of this project, you will be able to: ✅ Connect to a MySQL database from a Python script ✅ Perform **SELECT** and **INSERT** operations ✅ Understand **ORM** and its advantages ✅ Map Python classes to MySQL tables

----------

## 🔥 ORM vs Raw SQL

Without ORM:

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With ORM:

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

🌟 **Key Difference**: ORM eliminates the need for writing raw SQL queries, making the code cleaner and database-independent.

----------

## 📋 Project Tasks

### 🏆 Mandatory Tasks:

1.  **Get all states** - List all states from `hbtn_0e_0_usa` database.
    
2.  **Filter states** - List states starting with `N`.
    
3.  **Filter states by user input** - Display all states where `name` matches the argument.
    
4.  **SQL Injection Protection** - Ensure safe queries.
    
5.  **Cities by states** - List all cities from `hbtn_0e_4_usa`.
    
6.  **All cities by state** - Display cities of a given state.
    
7.  **First state model** - Define `State` class using SQLAlchemy.
    
8.  **All states via SQLAlchemy** - List all `State` objects.
    
9.  **First state** - Print the first `State` object.
    
10.  **Contains 'a'** - List all `State` objects containing the letter `a`.
    
11.  **Get a state** - Print the `State` object matching a given name.
    
12.  **Add a new state** - Insert a new `State` ("Louisiana").
    
13.  **Update a state** - Change `id=2` state to "New Mexico".
    
14.  **Delete states** - Remove all states with letter `a`.
    
15.  **Cities in state** - Define `City` class and fetch city objects.
    

----------

## 📜 Requirements

-   Allowed editors: `vi`, `vim`, `emacs`
    
-   Run on **Ubuntu 20.04 LTS** using **Python 3.8.5**
    
-   Use **MySQLdb (v2.0.x)** and **SQLAlchemy (v1.4.x)**
    
-   Follow **pycodestyle (v2.7.x)**
    
-   Scripts must be executable and well-documented
    
-   Avoid using `execute` with SQLAlchemy
    

----------

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  **Fork** this repository.
    
2.  **Create** a new branch.
    
3.  **Commit** your changes.
    
4.  **Submit** a pull request.
