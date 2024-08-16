#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    script that lists all cities from the database hbtn_0e_4_usa
    """

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], host="localhost",
                         port=3306, db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(argv[4]))
    rows = cur.fetchall()

    print(", ".join([state[1] for state in rows]))

    cur.close()
    db.close()
