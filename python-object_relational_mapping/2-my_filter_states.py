#!/usr/bin/python3
'''
it takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
'''

if __name__ = __main__:
  import sys
  import MySQLdb

  db = MySQL.connect( host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sus.argv[3])
  cur = db.cursor()
  to = "SELECT * FROM states WHERE BINARY name='{}'\ ORDER BY id ASC".format(sys.argv[4])
  cur.execute(to)
  states = cur.fetchall()
  for state in states:
    if (state[1] == sys.argv[4]):
      print(state)
  cur.close()
