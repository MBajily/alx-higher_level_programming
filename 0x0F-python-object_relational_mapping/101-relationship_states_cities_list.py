#!/usr/bin/python3
""" State object with the name passed as argument
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    Base.metadata.create_all(eng)
    sess = sessionmaker(bind=eng)
    sess = sess()
    
    for inst in sess.query(State).order_by(State.id):
        print(inst.id, inst.name, sep=": ")
        
        for city in inst.cities:
            print("    ", end="")
            print(city.id, city.name, sep=": ")
