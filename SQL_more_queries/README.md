# SQL - More Queries 📊

## Project Overview

This project is a deep dive into SQL queries using MySQL 8.0. It involves working with databases, users, privileges, constraints, and advanced SQL concepts like JOINs, UNIONs, and subqueries. The tasks range from creating and managing users to querying data across multiple tables.

## Learning Objectives 🎯

By the end of this project, you should be able to:

-   Create and manage MySQL users and their privileges.
    
-   Understand and implement **PRIMARY KEY** and **FOREIGN KEY** constraints.
    
-   Use **NOT NULL** and **UNIQUE** constraints.
    
-   Retrieve data from multiple tables using **JOINs**, **UNIONs**, and **subqueries**.
    
-   Work with advanced SQL techniques for database management and optimization.
    

## Technologies & Requirements 📜

-   **Operating System**: Ubuntu 20.04 LTS
    
-   **Database**: MySQL 8.0 (version 8.0.25)
    
-   **Editors**: vi, vim, emacs
    
-   **Mandatory File Naming**:
    
    -   Each SQL query must be saved as a `.sql` file.
        
    -   Each file must start with a comment describing the task.
        
    -   SQL keywords must be in **UPPERCASE**.
        
    -   Files must end with a new line.
        

## Installation & Setup ⚙️

To run this project locally, follow these steps:

1.  Install MySQL 8.0 on Ubuntu 20.04:
    
    ```
    sudo apt update
    sudo apt install mysql-server
    ```
    
2.  Secure the installation:
    
    ```
    sudo mysql_secure_installation
    ```
    
3.  Log in to MySQL:
    
    ```
    sudo mysql
    ```
    
4.  Execute the SQL scripts:
    
    ```
    mysql -u root -p < script.sql
    ```
    

## Tasks 🏁

### User & Privilege Management

1.  **My Privileges!** - List all privileges of specific users.
    
2.  **Read User** - Create a database and a user with SELECT privileges.
    

### Table Creation & Constraints

3.  **Always a Name** - Create a table with a `NOT NULL` column.
    
4.  **ID Can't Be Null** - Ensure `id` column has a default value.
    
5.  **Unique ID** - Enforce `UNIQUE` constraint on `id`.
    
6.  **States Table** - Create a `states` table with primary key constraints.
    
7.  **Cities Table** - Create a `cities` table with a foreign key reference.
    

### Data Retrieval

8.  **Cities of California** - List cities in California without using `JOIN`.
    
9.  **Cities by States** - List all cities and their corresponding states.
    
10.  **Genre ID by Show** - Retrieve shows with at least one genre.
    
11.  **Genre ID for All Shows** - Retrieve all shows, displaying `NULL` if no genre.
    
12.  **No Genre** - List all shows without a genre.
    
13.  **Number of Shows by Genre** - Count the number of shows per genre.
    
14.  **My Genres** - Retrieve genres linked to _Dexter_.
    
15.  **Only Comedy** - List all Comedy shows.
    
16.  **List Shows and Genres** - Retrieve all shows with their genres, displaying `NULL` if no genre.
    

## Usage 🛠️

To execute a script, run:

```
mysql -u root -p < script.sql
```

Replace `script.sql` with the actual filename.

## Resources 📚

-   [MySQL 8.0 Documentation](https://dev.mysql.com/doc/refman/8.0/en/)
    
-   SQL Joins Cheat Sheet
    
-   SQL Constraints