import random 

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, ForeignKey
from sqlalchemy.types import INTEGER, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

# engine = create_engine('sqlite:///sqlite.db', echo=True)
engine = create_engine('postgresql://postgres:1@localhost:5432/alchemy')
Base = declarative_base()

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

#metadata = MetaData()

class PartItem(Base):
    __tablename__ = 'partitems'

    part_id = Column(INTEGER, primary_key=True,autoincrement=True)
    description = Column(String)
    series_num = Column(INTEGER)
    car_id = Column(INTEGER, ForeignKey("cars.car_id"))

class Car(Base):
    __tablename__ = 'cars'

    car_id = Column(INTEGER,primary_key=True,autoincrement=True)
    make = Column(String)
    model = Column(String)
    year = Column(String)
    parts = relationship(PartItem, uselist=True, primaryjoin=(car_id == PartItem.car_id))

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
#metadata.create_all(bind=engine)

session = Session()

# for i in range(0, 20):
#     car = Car(make='Toyota', model='Prius', year='2014')
#     part = PartItem(car_id=i+1,description='Engine',
#                 series_num=random.randint(0, 1000))
#     session.add(car)
#     session.add(part)

# session.commit() 

# class SessionMixin(object):
#     def __init__(self, *args, **kwargs):
#         self.session = Session()
#         super(SessionMixin, self).__init__(*args, **kwargs)