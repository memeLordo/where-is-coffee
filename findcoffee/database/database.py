from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(url="sqlite:///sql_catalog.db")

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):

    def __repr__(self):
        pass
