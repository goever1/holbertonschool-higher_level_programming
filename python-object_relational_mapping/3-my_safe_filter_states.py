#!/usr/bin/python3
'''
it write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. (SQL injection safe)
'''

if __name__ == "__main__":
  import sys
  import MySQLdb
  
  db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
  
  cur = db.cursor()
  cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC")
  
  for row in cur.fetchall():
    if row[1] == sys.argv[4]:
      print(f"{row}")
cur.close()
