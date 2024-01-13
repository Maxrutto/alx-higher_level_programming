#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connection to the database and retrieving the
    states
    """
    db_connect = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=                                 argv[2], db=argv[3])
    cur = db_connect.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db_connect.close()

