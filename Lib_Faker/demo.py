from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from faker import Faker

from sqlalchemy import text

query = text()

# Connection Parameters
host = 'db.zfcwzrekfaadppegzqmw.supabase.co'
port = '5432'
database = 'postgres'
username = 'postgres'
password = 'zfcwzrekfaadppegzqmw'

# SQL Alchemy connections to PostgreSQL
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=True)
# base = declarative_base()
session_maker = sessionmaker(bind=engine)
session = session_maker()
meta = MetaData()

clients = Table(
    'clients', meta,
    Column('ID', Integer, primary_key=True),
    Column('FirstName', String),
    Column('LastName', String),
    Column('Balance', Integer),
    Column('Birthday', String),
    Column('Email', String)
)

meta.create_all(engine)

# count = 1
# while count <= 100:
#     count += 1

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
balance = fake.random_int(11, 243589)
birth_date = fake.date_of_birth()
email = fake.company_email()

insertData = clients.insert().values(FirstName=first_name,
                                     LastName=last_name,
                                     Balance=balance,
                                     Birthday=birth_date,
                                     Email=email)
insertData.compile().params
print(f"\n\n\n\n{insertData}")


c1 = clients(FirstName=first_name, LastName=last_name, Balance=balance, Birthday=birth_date, Email=email)
session.add(c1)

# VALUES (:ID, :FirstName, :LastName, :Balance, :Birthday, :Email)