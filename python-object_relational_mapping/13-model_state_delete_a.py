#!/usr/bin/python3
"""
This script deletes all State objects with a name
containing the letter 'a' from the database
hbn_0e_0_usa.
"""

import sys
from model_state import Base, State
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

    states_to_delete = session.query(State) \
                              .filter(State.name.like('%a%')) \
                              .all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
