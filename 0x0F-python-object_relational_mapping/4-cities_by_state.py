#!/usr/bin/python3
"""Module that lists all cities and their corresponding states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

def main():
    """
    Main function that fetches and prints all cities and their corresponding states
    from the database.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        with db.cursor() as cursor:
            query = """
            SELECT c.id, c.name, s.name
            FROM cities AS c
            INNER JOIN states AS s ON c.state_id = s.id
            ORDER BY c.id
            """
            cursor.execute(query)
            for city in cursor.fetchall():
                print(city)
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    main()
