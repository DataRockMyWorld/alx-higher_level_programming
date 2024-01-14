#!/usr/bin/python3
""" 
This script takes an argument and displays states
that match the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    with db.cursor() as cur:
        cur.execute(
            "SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id \
                    = states.id ORDER BY cities.id ASC"
        )

        query_rows = cur.fetchall()

    if query_rows is not None:
        for row in query_rows:
            print(row)

    cur.close()
    db.close()
