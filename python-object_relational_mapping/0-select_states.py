#!/usr/bin/python3
'''
It list all states from database hbtn_0e_0_usa
'''

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host='localhost',
        port=3306
        user=username, 
        passwd=password, 
        db=database_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
