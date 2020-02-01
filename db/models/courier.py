from datetime import datetime

from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import validates

from db.connect import Base, session
from db.models.logs import Log


class Courier(Base):
    __tablename__ = 'courier'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    @validates('age')
    def update_state(self, key, value):
        log = Log(costumer="Create New courier, {}".format(datetime.now()))
        session.add(log)
        session.commit()
        return value
