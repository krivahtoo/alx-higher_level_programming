#!/usr/bin/python3
"""3. SQL Injection...
takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
import sys


if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    port = 3306
    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    params = (state_name,)
    db = MySQLdb.connect(
        host=host, user=user, passwd=password, db=name, port=port
    )
    cursor = db.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
