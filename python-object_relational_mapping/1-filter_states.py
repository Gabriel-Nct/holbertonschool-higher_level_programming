#!/usr/bin/python3
"""
Script that lists all states with a name starting
with 'N' from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cursor = db.cursor()

    # Execute SQL query to fetch states starting with 'N'
    query = """
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC;
    """
    cursor.execute(query)

    # Fetch and print results
    for state in cursor.fetchall():
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
