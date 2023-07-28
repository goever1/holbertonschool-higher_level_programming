#!/usr/bin/python3
'''
It lists all State objects from the database hbtn_0e_6_usa
'''

from sys import argv
from sqlalchemy import create_engine
import sqlalchemy as db
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    connection = engine.connect()
    states = db.select(State.id, State.name).order_by(State.id)
    result = connection.execute(states).fetchall()

    for state in result:
        print("{}: {}".format(state[0], state[1]))
