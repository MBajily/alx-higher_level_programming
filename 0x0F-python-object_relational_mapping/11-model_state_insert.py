#!/usr/bin/python3
""" prints the State object with the name passed as argument from the databasei
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(eng)
    sess = sessionmaker(bind=eng)
    sess = sess()

    new_state = State(name='Louisiana')
    sess.add(new_state)

    newInstance = sess.query(State).filter_by(name='Louisiana').first()
    print(newInstance.id)
    sess.commit()
