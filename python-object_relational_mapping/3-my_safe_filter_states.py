#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all
states with a specific name from the states table.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (state_name,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
