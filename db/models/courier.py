from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from db.connect import Base


class Courier(Base):
    __tablename__ = 'courier'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    bill = relationship("Bill", back_populates="bill")