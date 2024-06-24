#!/usr/bin/python3
"""
Script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
Safe from SQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Script that takes in arguments and displays all
    values in the states table of hbtn_0e_0_usa
    """

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], host="localhost",
                         db=argv[3], port=3306)

    cur = db.cursor()
    state_name = argv[4]
    cur.execute("SELECT * FROM `states` WHERE `name` = %s", (state_name,))

    for state in cur.fetchall():
        if state[1] == state_name:
            print(state)
    cur.close()
    db.close()
