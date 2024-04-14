#!/usr/bin/python3
"""
Module that deletes states containing the letter 'a' from a MySQL database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

def main():
    """
    Main function that creates an SQLAlchemy engine, session, and
    deletes states containing the letter 'a' from the database.
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

    # Use a single query to delete all states containing the letter 'a'
    session.query(State).filter(State.name.like('%a%')).delete(synchronize_session='fetch')

    # Commit the session to persist the changes
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
