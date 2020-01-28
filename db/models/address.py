from sqlalchemy import Column, Integer, String, ForeignKey

from db.connect import Base


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    address = Column(String)
    phone = Column(String, unique=True)
    bill_id = Column(Integer, ForeignKey('bill.id'))

