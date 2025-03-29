#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all
states with a name matching a given string.
Usage:
    ./2-my_filter_states.py <username> <password> <database> <state_name>
The script uses the MySQLdb library to connect to the database
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

    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC".format(state_name)
    )

    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
