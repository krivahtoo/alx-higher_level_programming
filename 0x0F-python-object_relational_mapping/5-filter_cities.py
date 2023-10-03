#!/usr/bin/python3
"""5. All cities by state
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    port = 3306
    state_name = sys.argv[4]
    query = "SELECT name FROM cities WHERE state_id = \
        (SELECT id FROM states WHERE name LIKE BINARY %s)\
        ORDER BY cities.id ASC"
    params = (state_name,)
    db = MySQLdb.connect(
        host=host, user=user, passwd=password, db=name, port=port
    )
    cursor = db.cursor()

    cursor.execute(query, params)
    rows = cursor.fetchall()
    tuples = ()
    for row in rows:
        tuples += row
    print(*tuples, sep=", ")

    cursor.close()
    db.close()
