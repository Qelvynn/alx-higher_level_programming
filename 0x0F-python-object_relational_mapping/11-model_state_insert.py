#!/usr/bin/python3
"""
Module that adds a new state to a MySQL database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def main():
    """
    Main function that creates an SQLAlchemy engine, session, and
    adds a new state to the database.
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

    # Create a new State object for Louisiana
    louisiana = State(name="Louisiana")

    # Add the new state to the session and commit the changes
    session.add(louisiana)
    session.commit()

    # Print the ID of the newly added state
    print(louisiana.id)

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
