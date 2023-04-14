#!/usr/bin/python3

""" take name in argument and displays all values in the states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset='utf8')
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    dbrows = cur.fetchall()

    for row in dbrows:
        if row[1] == argv[4]:
            print(row)

    cur.close()
    db.close()
