print("\nFILE START: SQL_CONNECTION")

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# Custom Environment Variables:
load_dotenv()
host = os.environ['SUPABASE_HOST']
database = os.environ['SUPABASE_DB']
port = os.environ['SUPABASE_PORT']
username = os.environ['SUPABASE_USER']
password = os.environ['SUPABASE_PASSWD']


engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=True)
base = declarative_base()
session_maker = sessionmaker(bind=engine)
session = session_maker()

print("\tFILE FINISH: SQL_CONNECTION\n")
