#!/usr/bin/python3
'''
It list all states from database hbtn_0e_0_usa
'''

if __name__ == "__main__":}
  import sys
  import MySQLbd
  
  db = MuSQLdb.connector(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
  cur = db.cursor()
  cur.execute("SELECT * FROM states ORDER BY id ASC")
  query_rows = cur.fetchall()
  for eow in query_rows:
    print(row)
  cur.clase()
