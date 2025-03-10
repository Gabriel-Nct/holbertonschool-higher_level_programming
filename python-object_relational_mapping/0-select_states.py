#!/usr/bin/python3
"""
Imorting Module MySQLdb and sys to lists all states from a database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Script that lists all states from the database hbtn_0e_0_usa.
    It takes 3 arguments: MySQL username, MySQL password,
    and the database name.
    """
    # Checks that 3 arguments (username, password, database) are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Assign command line arguments to variables for use
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish a connection to the MySQL server using the provided credentials
    db = MySQLdb.connect(
        host="localhost",  # Server location
        port=3306,         # Port number for MySQL
        user=username,     # MySQL username
        passwd=password,   # MySQL password
        db=database        # Database to connect to
    )

    # Create a cursor object to allow execution of SQL queries
    cursor = db.cursor()

    # Query to retrieve all states, ordered by state ID in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Retrieve all results from the query
    states = cursor.fetchall()

    # Print each state record returned by the query
    for state in states:
        print(state)

    # Close the cursor and the connection to the database
    cursor.close()
    db.close()
