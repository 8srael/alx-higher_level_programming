#!/usr/bin/python3

"""Lists all states with a name starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset='utf8')
    cur = db.cursor()

    query = """SELECT * FROM states
                WHERE states.name LIKE 'N%'
                    ORDER BY states.id ASC"""

    cur.execute(query)
    dbrows = cur.fetchall()

    for row in dbrows:
        print(row)

    cur.close()
    db.close()
