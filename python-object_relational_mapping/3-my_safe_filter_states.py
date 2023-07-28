#!/usr/bin/python3
'''
it write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. (SQL injection safe)
'''

  if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    st = sys.argv[4].split('\'')
    to = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(st[0])
    cur.execute(to)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
