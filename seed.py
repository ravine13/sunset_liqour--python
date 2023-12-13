from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.Main import Base, Customer, Company, Brand, Comment, Rating


engine = create_engine('sqlite:///sunset_liqour.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



data = [{
  "id": 1,
  "name": "Matty Ducarel",
  "age": 25,
  "email": "mducarel0@webmd.com",
  "loyalty_points": 19560,
  "address": "Apt 236"
}, {
  "id": 2,
  "name": "Sonnie Edgworth",
  "age": 40,
  "email": "sedgworth1@lulu.com",
  "loyalty_points": 6853,
  "address": "Suite 64"
}, {
  "id": 3,
  "name": "Ashby Boig",
  "age": 28,
  "email": "aboig2@ocn.ne.jp",
  "loyalty_points": 10099,
  "address": "Suite 96"
}, {
  "id": 4,
  "name": "Robyn Lorence",
  "age": 96,
  "email": "rlorence3@si.edu",
  "loyalty_points": 18580,
  "address": "Suite 54"
}, {
  "id": 5,
  "name": "Claudell Bruton",
  "age": 16,
  "email": "cbruton4@ihg.com",
  "loyalty_points": 15805,
  "address": "1st Floor"
}]

customers = [Customer(**datum) for datum in data]

session.add_all(customers)
session.commit()

print("Done seeding Data!!!")
