#!/usr/bin/python3
"""Module that lists all cities from a specified state in the hbtn_0e_0_usa database."""

import sys
import MySQLdb

def main():
    """
    Main function that fetches and prints cities from the database
    that are in a specified state provided as a command-line argument.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        return

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        with db.cursor() as cursor:
            query = """
            SELECT c.name
            FROM cities AS c
            JOIN states AS s ON c.state_id = s.id
            WHERE s.name = %s
            ORDER BY c.id
            """
            cursor.execute(query, (state_name,))
            cities = [city[0] for city in cursor.fetchall()]
            print(", ".join(cities))
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    main()
