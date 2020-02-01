from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates

from db.connect import Base, session
from db.models.logs import Log


class Store(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    bills = relationship("Bill")

    @validates('name')
    def update_state(self, key, value):
        log = Log(store="Create New Store, {}".format(datetime.now()))
        session.add(log)
        session.commit()
        return value
