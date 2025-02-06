from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy     import Column, Integer, String, Text
from sqlalchemy     import create_engine
from dotenv         import load_dotenv
import os


# load environment variables
load_dotenv(dotenv_path='.env_db')
host = os.getenv('DB_HOST_IP')
port = os.getenv('DB_HOST_PORT')
user = os.getenv('DB_USERNAME')
psswd = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')


# create engine to connect to Postgres
engine = create_engine(f'postgresql://{user}:{psswd}@{host}:{port}/{db}', echo=False)
try:
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
except Exception as e:
    print(f"Error connecting to Postgres {e}")


class Vacancy(Base):
    __tablename__ = 'Ufanet_Jobs'
    id      = Column(Integer, primary_key=True)
    title   = Column(String(255))
    salary  = Column(String)
    tasks   = Column(Text)
    expect  = Column(Text)
    offer   = Column(Text)
    link    = Column(String(255))


Base.metadata.create_all(engine)
