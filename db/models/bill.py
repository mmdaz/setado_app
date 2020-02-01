from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db.connect import Base


class Bill(Base):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    food_price = Column(String)
    created_at = Column(DateTime)
    address = relationship("Address", uselist=False)
    costumer_id = Column(Integer, ForeignKey('costumer.id'), )
    store_id = Column(Integer, ForeignKey('store.id'))
