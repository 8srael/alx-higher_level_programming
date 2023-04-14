#!/usr/bin/python3

"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    dbrows = cur.fetchall()

    for row in dbrows:
        print(row)

    cur.close()
    db.close()
