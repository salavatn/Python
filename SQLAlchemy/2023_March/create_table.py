from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


# Connection Parameters
host = 'db.zorvmuaqwcpbfqjpifmo.supabase.co'
port = '5432'
database = 'postgres'
username = 'postgres'
password = 'zorvmuaqwcpbfqjpifmo'


# SQL Alchemy connections to PostgreSQL
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=True)
session_maker = sessionmaker(bind=engine)
base = declarative_base()
session = session_maker()


class Clients(base):
    __tablename__ = 'Clients'
    ID = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Balance = Column(Integer)
    Birthday = Column(String)
    Email = Column(String)


base.metadata.create_all(engine)
