#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database starting with 'N'."""
import sys
import MySQLdb

def main():
    """
    Main function that fetches and prints states from the database
    starting with the letter 'N'.
    """
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM `states` ORDER BY `id`")
            for state in cursor.fetchall():
                if state[1][0] == 'N':
                    print(state)
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    main()
