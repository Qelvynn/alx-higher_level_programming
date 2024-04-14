#!/usr/bin/python3
"""Module that lists all states from a MySQL database."""

import sys
import MySQLdb

def list_states(username, password, database):
    """
    List all states from the database hbtn_0e_0_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()

        # Execute the SQL query to fetch all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the query result
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as err:
        print(f"Database error: {err}")
    except Exception as err:
        print(f"Error: {err}")
    finally:
        # Close the database connection
        if db is not None:
            db.close()

# Example usage
if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
    else:
        print("Usage: ./script.py <username> <password> <database>")
