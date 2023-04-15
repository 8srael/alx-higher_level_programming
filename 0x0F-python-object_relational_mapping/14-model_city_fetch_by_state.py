#!/usr/bin/python3

"""Cities"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).\
        filter(State.id == City.state_id).\
        order_by(City.id).\
        all()

    for state, city in results:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
