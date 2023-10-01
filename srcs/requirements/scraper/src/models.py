from sqlalchemy import Boolean, Column, ForeignKey, Integer, BigInteger, String, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    category_id = Column(Integer)
    products = relationship("Product", back_populates="category")  # To establish a relationship with the Product model

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String)
    unit_size = Column(Integer)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)  # Foreign Key to Category

    category = relationship("Category", back_populates="products")  # Relationship to Category model
    prices = relationship("Price", back_populates="product")  # To establish a relationship with the Price model
    
class Price(Base):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    ts = Column(BigInteger)

    ts = Column(TIMESTAMP, nullable=False)  # TIMESTAMP is appropriate for a timestamp
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)  # Foreign Key to Product
    product = relationship("Product", back_populates="prices")  # Relationship to Product model