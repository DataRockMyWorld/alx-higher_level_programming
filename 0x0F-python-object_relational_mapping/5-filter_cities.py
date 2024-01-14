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
            "SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                    WHERE states.name LIKE BINARY %(name)s ORDER BY cities.name ASC",
            {'name': argv[4]},
        )

        query_rows = cur.fetchall()
    
    if query_rows is not None:
       print(", ".join([row[0] for row in query_rows]))

    cur.close()
    db.close()
