#!/usr/bin/python3
'''
It takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
'''

if __name__ == "__main__":
  import sys
  import MySQLdb

  db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], 
                       passwd=sys.argv[2], db=sys.argv[3])
  cur = db.cursor()
  cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
  
  print(", ".join([row[2] for row in
                     db_connect.fetchall() if row[4] == sys.argv[4]]))
