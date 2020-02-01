from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, DateTime

from db.connect import Base, session
from sqlalchemy.orm import validates

from db.models.logs import Log


class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    price = Column(BigInteger)
    created_at = Column(DateTime)

    @validates('name')
    def update_state(self, key, value):
        log = Log(food="Create New Food, {}".format(datetime.now()))
        session.add(log)
        session.commit()
        return value

