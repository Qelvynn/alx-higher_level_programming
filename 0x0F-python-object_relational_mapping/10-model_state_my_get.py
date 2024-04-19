#!/usr/bin/python3
"""
Module that searches for a state in a MySQL database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def main():
    """
    Main function that creates an SQLAlchemy engine, session, and
    searches for a state with a specific name in the database.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        return

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}",
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Search for the specified state in the database
    state = session.query(State).filter(State.name == state_name).first()
    print(f"{state.id}" if state else "Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
