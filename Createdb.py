from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.Main import Base


engine = create_engine('sqlite:///sunset_liqour.db', echo=True)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

session.close()
