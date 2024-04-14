#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database with a specific name."""

import sys
import MySQLdb

def main():
    """
    Main function that fetches and prints states from the database
    with a specific name provided as a command-line argument.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        return

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        with db.cursor() as cursor:
            query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
            cursor.execute(query, (state_name,))
            for state in cursor.fetchall():
                print(state)
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    main()
