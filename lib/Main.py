from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    email = Column(String(100))
    address = Column(String(255))
    loyalty_points = Column(Integer)
    ratings = relationship("Rating", backref="rating_customer")
    comments = relationship("Comment", backref="comment_customer")
    brands = relationship("Brand", back_populates="customer")

    


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location = Column(String(100))
    established_year = Column(Integer)
    revenue = Column(DECIMAL(15, 2))
    brands = relationship("Brand", backref="company")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    text = Column(String(255))
    brand_id = Column(Integer, ForeignKey('brands.id'))  

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    score = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brands.id'))  


class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    category = Column(String(50))
    price = Column(DECIMAL(10, 2))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="brands")
    comments = relationship("Comment", backref="brand")
    ratings = relationship("Rating", backref="brand")

engine = create_engine('sqlite:///sunset_liqours.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
