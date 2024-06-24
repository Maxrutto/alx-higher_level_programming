#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT DISTINCT cities.id, cities.name, states.name \
                 AS state_name \
                 FROM cities \
                 INNER JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id ASC \
                 LIMIT 15")
    rows = cur.fetchall()
    for city_id, city_name, state_name in rows:
        print("({}, '{}', '{}')".format(city_id, city_name, state_name))
    
    cur.close()
    db.close()
