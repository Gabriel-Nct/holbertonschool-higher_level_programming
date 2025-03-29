#!/usr/bin/python3
"""
This script lists all City objects from the database
hbtn_0e_14_usa
from the state passed as an argument.
The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(City, State).join(State).order_by(City.id)

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
