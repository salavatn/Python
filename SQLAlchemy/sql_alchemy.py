from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

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


# Table parameters:
class TableCustomers(ns_base):
    __tablename__ = 'Customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# CREATE TABLE:
ns_base.metadata.create_all(ns_engine)


#
#
# # Sample Data
# ns_data = CLASS_Students(name="Airas", age=38, grade="A")
#
# # INSERT DATA
# ns_session.add(ns_data)

'''# More Sample Data:
ns_data_1 = CLASS_Students(name="Yuliya", age=32, grade="B")
ns_data_2 = CLASS_Students(name="Alsu", age=40, grade="C")'''

# # INSERT MORE DATA
# ns_session.add_all([ns_data_1, ns_data_2])

# ns_session.commit()


'''# GET DATA
data = ns_session.query(CLASS_Students)
print(f"SQL Query:\n{data}")

for i in data:
    print(f"Name:\t{i.name}")
'''