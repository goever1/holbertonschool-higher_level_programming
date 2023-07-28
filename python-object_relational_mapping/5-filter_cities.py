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
  db.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id\
              WHERE states.name='{}'\
              ORDER BY cities.id ASC".format(sys.argv[4]))
  cities = cur.fetchall()
  for i in range(0, len(cities)):
    if i < (len(cities) -1):
      print(cities[i][0], end=", ")
    else
      print(cities[i][0], end="")
    print()
  cur.close()
  
