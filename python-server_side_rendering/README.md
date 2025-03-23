# 🐍 Python - Server-Side Rendering

## 📖 Description

Server-side rendering (SSR) is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering, where the browser builds the web page using JavaScript and dynamic data.

In this project, you will learn how to implement SSR using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.

### 🎯 Learning Objectives

-   🧐 Understand the concepts of server-side rendering and its differences from client-side rendering.
-   🚀 Learn the benefits of using SSR in web development.
-   🛠 Implement SSR in Python using the Flask framework.
-   🏗 Utilize Jinja templating engine to dynamically generate HTML pages.
-   📊 Read and display data from JSON, CSV, and SQLite databases.
-   ✨ Handle dynamic content and user inputs in web applications.

----------

## 📌 What to Expect

You will build a Flask application that serves web pages using server-side rendering techniques. Starting with basic templates, you will progressively integrate dynamic content from multiple data sources. By the end of the project, you will have a solid grasp of SSR, templating, and how to build scalable web applications.

----------

## 📚 Resources

-   [MDN Web Docs on Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn/Server-side)
-   [Client-side vs. Server-side vs. Pre-rendering](https://www.cloudflare.com/learning/serverless/server-side-rendering/)
-   [Flask Official Documentation](https://flask.palletsprojects.com/en/2.3.x/)
-   [Python JSON Documentation](https://docs.python.org/3/library/json.html)
-   [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
-   [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
-   [Jinja2 Documentation](https://jinja.palletsprojects.com/en/3.0.x/)

----------

## ✅ Tasks Breakdown

### 📜 Task 0: Creating a Simple Templating Program

📌 **Objective:** Learn string templating in Python and generate personalized invitation files from a template.  
📂 **File:** `task_00_intro.py`

🔹 **Key Steps:**

-   Create a template file with placeholders.
-   Define a list of attendees.
-   Implement a function `generate_invitations()`.
-   Handle edge cases (empty inputs, missing data, invalid types).
-   Write output files for each attendee.

### 🖥 Task 1: Creating a Basic HTML Template in Flask

📌 **Objective:** Build a simple Flask application that serves a web page using a Jinja template.  
📂 **File:** `task_01_jinja.py`

🔹 **Key Steps:**

-   Set up a Flask environment and install Flask (`pip install Flask`).
-   Create an HTML template with headings, paragraphs, and lists.
-   Render the template in Flask.
-   Design reusable header and footer templates.
-   Implement multiple routes (`/`, `/about`, `/contact`).

### 🔄 Task 2: Creating a Dynamic Template with Loops and Conditions

📌 **Objective:** Enhance the Flask app by integrating dynamic content using Jinja’s loops and conditions.  
📂 **File:** `task_02_logic.py`

🔹 **Key Steps:**

-   Create a `items.json` file containing a list of items.
-   Design a template that loops through the items.
-   Display an error message if the list is empty.
-   Implement a `/items` route that loads data dynamically.

### 📊 Task 3: Displaying Data from JSON or CSV Files in Flask

📌 **Objective:** Read and display product data from JSON and CSV files, and filter by an optional `id` parameter.  
📂 **File:** `task_03_files.py`

🔹 **Key Steps:**

-   Create `products.json` and `products.csv` files.
-   Design a template `product_display.html` to display products in a table.
-   Modify Flask routes to accept `source=json` or `source=csv` as query parameters.
-   Implement filtering by product ID.
-   Handle errors (invalid source, missing data, etc.).

### 🗄 Task 4: Extending Dynamic Data Display to Include SQLite

📌 **Objective:** Extend the Flask application to fetch and display data from an SQLite database.  
📂 **File:** `task_04_db.py`

🔹 **Key Steps:**

-   Create an SQLite database (`products.db`).
-   Define a `Products` table and populate it with sample data.
-   Modify the Flask app to handle `source=sql` query parameters.
-   Ensure error handling for database-related issues.

----------

## 🛠 Setup Instructions

1️⃣ **Clone the Repository:**

```sh
 git clone https://github.com/holbertonschool-higher_level_programming.git
 cd python-server_side_rendering

```

2️⃣ **Install Dependencies:**

```sh
pip install Flask

```

3️⃣ **Run the Flask Application:**

```sh
python task_01_jinja.py

```

4️⃣ **Access the Application:** Open `http://localhost:5000` in your web browser.

----------

## 🎯 Testing & Debugging

-   Run each script individually to verify its output.
-   Use `print()` statements or Flask's debugging mode for troubleshooting.
-   Test different input scenarios to ensure proper error handling.
-   Validate outputs with sample JSON and CSV data.

----------

## 🤝 Contribution Guidelines

💡 **Want to contribute?**

-   Fork the repository 🍴
-   Create a new branch 🌿
-   Commit your changes ✅
-   Push to your branch 🚀
-   Submit a Pull Request 📬

----------

**🚀 Happy Coding!**