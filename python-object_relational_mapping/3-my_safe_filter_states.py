#!/usr/bin/python3
'''
it write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. (SQL injection safe)
'''

if __name__ == "__main__":
  import sys
  import MySQLdb
  
  db_cnctn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             charset="utf8")
  db_connect = db_cnctn.cursor()
  db_connect.execute("SELECT * FROM states")
  for row in db_connect.fetchall():
    if row[1] == sys.argv[4]:
      print(f"{row}")
