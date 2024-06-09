from sqlalchemy import Column, BigInteger, DateTime, Text, func, Integer, ARRAY, Numeric, Float

from app.models.db.base import Base


# CREATE TABLE public.items (
#     item_id SERIAL PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     description TEXT,
#     price NUMERIC(10, 2) NOT NULL,
#     quantity INTEGER NOT NULL
# );

# INSERT INTO public.items (name, description, price, quantity)
# VALUES 
# ('Item 1', 'Description for item 1', 9.99, 5),
# ('Item 2', 'Description for item 2', 15.49, 3),
# ('Item 3', 'Description for item 3', 7.99, 20);


class ItemModel(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text(100), nullable=False)
    description = Column(Text(255))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)