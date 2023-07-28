#!/usr/bin/python3
'''
It list all states from database hbtn_0e_0_usa
'''
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host= 'localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()    
    db.close()
