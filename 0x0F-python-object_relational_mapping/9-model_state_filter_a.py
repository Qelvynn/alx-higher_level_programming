#!/usr/bin/python3
"""
Module that retrieves and prints the first state from a MySQL database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def main():
    """
    Main function that creates an SQLAlchemy engine, session, and
    retrieves the first state from the database, printing its ID and name.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}",
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Retrieve the first state from the database and print its ID and name
    state = session.query(State).order_by(State.id).first()
    print(f"{state.id}: {state.name}" if state else "Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
