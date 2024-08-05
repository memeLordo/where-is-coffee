from typing import Annotated

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///./database/sql_catalog.db")

session_factory = sessionmaker(engine)

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):

    def __repr__(self):
        pass
