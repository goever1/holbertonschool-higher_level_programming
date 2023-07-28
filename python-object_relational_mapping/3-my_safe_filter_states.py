#!/usr/bin/python3
'''
it write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. (SQL injection safe)
'''

if __name__ == "__main__":
  import sys
  import MySQLdb
  
  db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
  cur = db.cursor()
  to = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
  cur.execute(to, (sys.argv[4],))
  states = cur.fetchall()
  
  for state in states:
    print(state)
cur.close()
db.close()
