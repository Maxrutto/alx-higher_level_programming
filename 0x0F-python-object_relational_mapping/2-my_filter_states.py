#!/usr/bin/python3
"""
Script that takes in an argument and displays
all values in the states table
where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Extracting values from database connection
    """

    db_connect = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                 passwd=argv[2], db=argv[3])
    cur = db_connect.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    unique_names = set()

    for row in rows:
        state_id, state_name = row
        if state_name not in unique_names:
            unique_names.add(state_name)
            print((state_id, state_name))

    cur.close()
    db_connect.close()
