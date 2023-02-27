from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Custom Environment Variables:
load_dotenv()
host = os.environ['SUPABASE_HOST']
database = os.environ['SUPABASE_DB']
port = os.environ['SUPABASE_PORT']
username = os.environ['SUPABASE_USER']
password = os.environ['SUPABASE_PASSWD']

ns_engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=True)
ns_session_maker = sessionmaker(bind=ns_engine)
ns_session = ns_session_maker()

ns_base = declarative_base()


class Students(ns_base):
    __tablename__ = 'USERS'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


ns_base.metadata.create_all(ns_engine)