#!/usr/bin/python3
"""
This script updates the name of a State object in a MySQL database
with id = 2 to "New Mexico".
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

    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
