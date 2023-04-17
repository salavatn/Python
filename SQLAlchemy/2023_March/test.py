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

import sqlalchemy

a = sqlalchemy.__version__
print(a)
