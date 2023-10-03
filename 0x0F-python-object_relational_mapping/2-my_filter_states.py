#!/usr/bin/python3
"""2. Filter states by user input
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    port = 3306
    state_name = sys.argv[4]

    query = f"SELECT * FROM states WHERE name LIKE BINARY '{state_name}'\
        ORDER BY id ASC"
    db = MySQLdb.connect(
        host=host, user=user, passwd=password, db=name, port=port
    )
    cursor = db.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
