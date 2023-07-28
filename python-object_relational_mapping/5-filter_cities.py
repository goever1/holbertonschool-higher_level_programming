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
  db.execute("SELECT cities.name\
              FROM state INNER JOIN cities ON states.id = cities.state_id\
              WHERE states.name='{}'\
              ORDER BY cities.id ASC".format(sys.argv[4]))
  cities = cur.fetchall()
  for cities in states:
    print(cities)
  db.close()
  
