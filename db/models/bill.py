from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, validates

from db.connect import Base, session
from db.models.logs import Log


class Bill(Base):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    food_price = Column(String)
    created_at = Column(DateTime)
    address = relationship("Address", uselist=False)
    costumer_id = Column(Integer, ForeignKey('costumer.id'), )
    store_id = Column(Integer, ForeignKey('store.id'))

    @validates('food_name')
    def update_state(self, key, value):
        log = Log(bill="Create New Bill, {}".format(datetime.now()))
        session.add(log)
        session.commit()
        return value

