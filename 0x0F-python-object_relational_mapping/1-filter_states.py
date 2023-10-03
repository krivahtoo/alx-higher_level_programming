#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(
        host=host, user=user, passwd=password, db=name, port=port
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                   ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
