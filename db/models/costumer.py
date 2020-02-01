from datetime import datetime

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship, validates

from db.connect import Base, session
from db.models.logs import Log


class Costumer(Base):
    __tablename__ = 'costumer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    addresses = relationship("Address")
    bills = relationship("Bill")

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @validates('age')
    def update_state(self, key, value):
        log = Log(costumer="Create New Costumer, {}".format(datetime.now()))
        session.add(log)
        session.commit()
        return value


