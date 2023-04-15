#!/usr/bin/python3

"""Start link class to table in database"""

from sys import argv
from model_state import Base, State
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

    firstState = session.query(State).order_by(State.id).first()

    if firstState:
        print("{}: {}".format(firstObj.id, firstObj.name))
    else:
        print('Nothing')

    session.close()
