from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv(dotenv_path='.env_db')
user = os.getenv('DB_USER')
pswd = os.getenv('DB_PSWD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db   = os.getenv('DB_NAME')


# Create engine to PostgreSQL database
engine  = create_engine(f'postgresql://{user}:{pswd}@{host}:{port}/{db}')
Session = sessionmaker(bind=engine)
session = Session()
Base    = declarative_base()
