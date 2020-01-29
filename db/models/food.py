from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, DateTime

from db.connect import Base


class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    price = Column(BigInteger)
    created_at = Column(DateTime)
