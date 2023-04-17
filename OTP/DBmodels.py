from sqlalchemy     import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy     import create_engine
from dotenv         import load_dotenv
import os


# Load the .credentials file and get the variables:
load_dotenv(dotenv_path='.credentials')
host = os.getenv('DB_HOST_IP')
port = os.getenv('DB_HOST_PORT')
user = os.getenv('DB_USERNAME')
pswd = os.getenv('DB_PASSWORD')
db   = os.getenv('DB_NAME')


# SQLAlchemy engine, session and base
engine  = create_engine(f'postgresql://{user}:{pswd}@{host}:{port}/{db}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base    = declarative_base()


# Table Notes
class Notes(Base):
    __tablename__ = 'UsersSecrets'
    ID          = Column(Integer,  primary_key=True)
    UserName    = Column(String,   nullable=False, length=50)
    LastName    = Column(String,   nullable=False, length=50)
    Email       = Column(String,   nullable=False, length=50)
    SecretKey   = Column(String,   nullable=False, length=32, unique=True)
    Registration= Column(DateTime, nullable=False)
    Status      = Column(Boolean,  default=True)


# Create table
Base.metadata.create_all(engine)
