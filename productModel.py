from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    # This defines the many-to-one relationship
    user = relationship("User", back_populates="products")
