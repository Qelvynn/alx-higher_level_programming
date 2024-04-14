#!/usr/bin/python3
"""
Module that retrieves and prints a list of cities with their
associated states from a MySQL database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

def main():
    """
    Main function that creates an SQLAlchemy engine, session, and
    retrieves cities with their associated states from the database.
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

    # Retrieve cities and their associated states from the database
    cities_states = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
