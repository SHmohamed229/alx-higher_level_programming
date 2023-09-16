#!/usr/bin/python3
"""
Script for post in an argu and
display all values in the states
where (name) argu
from the Database `hbtn_0e_0_usa`.

This for Time  is Safe from
MySQL Injections.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    this method for access to the Database and get States
    from the Database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
