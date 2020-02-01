from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates

from db.connect import Base, session
from db.models.logs import Log


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    address = Column(String)
    phone = Column(String, unique=True)
    bill_id = Column(Integer, ForeignKey('bill.id'))
    bill = relationship("Bill")
    costumer_id = Column(Integer, ForeignKey('costumer.id'))
    
    @validates('name')
    def update_state(self, key, value):
        log = Log(address="Create New Food, {}".format(datetime.now()))
        session.add(log)
        session.commit()
        return value

