from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

# Declare table
DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """

    # ** => Unpacks values in DATABASE
    # URL() => Maps keys & values to URL that the db understands
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    # Create table
    DeclarativeBase.metadata.create_all(engine)


# Pass table into Deals()
class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""

    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    original_price = Column('original_price', Integer, nullable=True)
    price = Column('price', Integer, nullable=True)
    end_date = Column('end_date', DateTime, nullable=True)
