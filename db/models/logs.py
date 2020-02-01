from sqlalchemy import Column, String, Integer

from db.connect import Base


class Log(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    bill = Column(String)
    costumer = Column(String)
    courier = Column(String)
    food = Column(String)
    store = Column(String)
