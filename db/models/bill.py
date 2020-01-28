from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.connect import Base


class Bill(Base):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    food_name = Column(String)
    food_price = Column(Integer)
    address = relationship("Address", back_populates="address")
    costumer_id = Column(Integer, ForeignKey('costumer.id'))
    store_id = Column(Integer, ForeignKey('store.id'))
