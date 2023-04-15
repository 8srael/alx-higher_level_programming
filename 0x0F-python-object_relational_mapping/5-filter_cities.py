#!/usr/bin/python3

"""Lists states and cities"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset='utf8')
    cur = db.cursor()

    cur.execute("""SELECT cities.name FROM cities
                    JOIN states ON cities.state_id = states.id
                        WHERE states.name = %s
                             ORDER BY cities.id ASC""", (argv[4], ))

    dbrows = cur.fetchall()

    for i in range(len(dbrows)):
        if i == len(dbrows) - 1:
            print(dbrows[i][0])
        print(dbrows[i][0], end=", ")

    cur.close()
    db.close()
