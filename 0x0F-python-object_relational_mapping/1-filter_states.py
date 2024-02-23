#!/usr/bin/python3
"""
Script that all states with a name
starting with upper N from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    us = sys.argv[1]
    ps = sys.argv[2]
    dbs = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost", port=3306, user=us, passwd=ps, db=dbs
        )
        cursor = db.cursor()
        cursor.execute(
            "SELECT all FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
