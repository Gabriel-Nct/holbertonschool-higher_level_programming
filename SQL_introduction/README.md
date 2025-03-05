# 📌 SQL - Introduction

## 📖 Description
This project is a hands-on introduction to SQL and relational databases. You will learn how to create databases, manage tables, and execute SQL queries using MySQL.

---

## 📚 Resources
Make sure to read or watch the following resources:
- [What is Database & SQL?](#)
- [Install MySQL (MySQL Server)](#)
- [A Basic MySQL Tutorial](#)
- [Basic SQL statements: DDL and DML](#) (no need to read the chapter "Privileges")
- [Basic queries: SQL and RA](#)
- [SQL technique: functions](#)
- [SQL technique: subqueries](#)
- [Difference between a backtick and an apostrophe](#)
- [MySQL Cheat Sheet](#)
- [MySQL 8.0 SQL Statement Syntax](#)

---

## 🎯 Learning Objectives
By the end of this project, you should be able to explain:
- 🗄️ What is a database
- 🔗 What is a relational database
- ❓ What SQL stands for
- 🏛️ What is MySQL
- 🛠️ How to create a database in MySQL
- 🔤 What DDL and DML stand for
- 🏗️ How to CREATE or ALTER a table
- 🔍 How to SELECT data from a table
- ✏️ How to INSERT, UPDATE, or DELETE data
- 🔄 What are subqueries
- ⚡ How to use MySQL functions

---

## ⚙️ Requirements
### 🖥️ General
- Allowed editors: `vi`, `vim`, `emacs`
- All scripts will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0**
- All SQL files should:
  - End with a new line
  - Have a comment describing the task at the beginning
  - Use uppercase for SQL keywords (`SELECT`, `WHERE`, etc.)
  - Be named accordingly (e.g., `0-list_databases.sql`)
  - Be tested using `wc` for length verification

---

## 🚀 Installation & Setup
### 🐧 Ubuntu 22.04 (Current Image)
1. **Update package list**
   ```bash
   apt update
   ```
2. **Install MySQL Server**
   ```bash
   apt install -y mysql-server
   ```
3. **Verify installation**
   ```bash
   mysql --version
   ```
4. **Start MySQL Service**
   ```bash
   service mysql start
   ```
5. **Connect to MySQL CLI**
   ```bash
   mysql -uroot
   ```

---

## 📝 Tasks
### 📌 Mandatory Tasks
1. **List databases** ➡️ `0-list_databases.sql`
2. **Create a database** ➡️ `1-create_database_if_missing.sql`
3. **Delete a database** ➡️ `2-remove_database.sql`
4. **List tables** ➡️ `3-list_tables.sql`
5. **Create first table** ➡️ `4-first_table.sql`
6. **Describe a table** ➡️ `5-full_table.sql`
7. **List all rows in a table** ➡️ `6-list_values.sql`
8. **Insert a row** ➡️ `7-insert_value.sql`
9. **Count occurrences of ID = 89** ➡️ `8-count_89.sql`
10. **Create and populate second table** ➡️ `9-full_creation.sql`
11. **List records sorted by score** ➡️ `10-top_score.sql`
12. **Select records with score >= 10** ➡️ `11-best_score.sql`
13. **Update Bob's score** ➡️ `12-no_cheating.sql`
14. **Delete records with score <= 5** ➡️ `13-change_class.sql`
15. **Compute average score** ➡️ `14-average.sql`
16. **Count records by score** ➡️ `15-groups.sql`
17. **List records where name is not empty** ➡️ `16-no_link.sql`

---

## 📂 Repository Structure
```
📂 holbertonschool-higher_level_programming
└── 📂 SQL_introduction
    ├── 0-list_databases.sql
    ├── 1-create_database_if_missing.sql
    ├── 2-remove_database.sql
    ├── 3-list_tables.sql
    ├── 4-first_table.sql
    ├── 5-full_table.sql
    ├── 6-list_values.sql
    ├── 7-insert_value.sql
    ├── 8-count_89.sql
    ├── 9-full_creation.sql
    ├── 10-top_score.sql
    ├── 11-best_score.sql
    ├── 12-no_cheating.sql
    ├── 13-change_class.sql
    ├── 14-average.sql
    ├── 15-groups.sql
    ├── 16-no_link.sql
    └── README.md
```

---

## 🤝 Contributing
- Fork the repository 📌
- Create a new branch (`git checkout -b feature-branch`) 🌿
- Commit your changes (`git commit -m 'Add new feature'`) ✍️
- Push to the branch (`git push origin feature-branch`) 🚀
- Open a Pull Request 🛠️

---
