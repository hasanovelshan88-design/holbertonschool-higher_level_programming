#!/usr/bin/python3
"""Lists all State objects and corresponding City objects"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    [print("{}: {}\n{}".format(
        s.id, s.name,
        "\n".join("\t{}: {}".format(c.id, c.name)
                  for c in sorted(s.cities, key=lambda c: c.id)))
     for s in session.query(State).order_by(State.id)]
    session.close()
