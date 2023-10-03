#!/usr/bin/python3
"""4. Cities by states
lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(
        host=host, user=user, passwd=password, db=db, port=port
    )
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON states.id = cities.state_id \
        ORDER BY cities.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
