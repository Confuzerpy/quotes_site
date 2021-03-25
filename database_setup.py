import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Coins(Base):
    __tablename__ = 'coins'

    id = Column(Integer, primary_key=True)
    symbol = Column(String(100))
    name = Column(String(100))
    price = Column(String(100))
    market_cap = Column(String(100))
    volume_24h = Column(String(100))
    delta_24h = Column(String(100))


engine = create_engine('sqlite:///coins.db')
Base.metadata.create_all(engine)
