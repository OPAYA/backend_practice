from sqlalchemy import Column, BigInteger, DateTime, Text, func, Integer, ARRAY, Numeric, Float

from app.models.db.base import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text(100), nullable=False)
    description = Column(Text(255))
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)