from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DECIMAL
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    email = Column(String(100))
    address = Column(String(255))
    loyalty_points = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship("Brand", backref="customers")  


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location = Column(String(100))
    established_year = Column(Integer)
    revenue = Column(DECIMAL(15, 2))

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    text = Column(String(255))
    brand = relationship("Brand", backref="comments")

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    score = Column(Integer)
    brand = relationship("Brand", backref="ratings")


class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    category = Column(String(50))
    price = Column(DECIMAL(10, 2)) 
    company = relationship("Company", backref="brands")
   


engine = create_engine('sqlite:///sunset_liqour.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()