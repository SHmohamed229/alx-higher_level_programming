#!/usr/bin/python3
"""
script for list from the
Database "hbtn_0e_0_usa".
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    this for access to database and get States
    from Database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
