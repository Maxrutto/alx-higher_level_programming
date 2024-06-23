#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM STATES")
    rows = cur.fetchall()

    for row in rows:
        print(row)
