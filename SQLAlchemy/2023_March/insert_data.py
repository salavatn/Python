from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from faker import Faker

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


fake = Faker()
count = 1

while count <= 100:

    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_balance = fake.random_int(11, 243589)
    fake_birth_date = fake.date_of_birth()
    fake_email = fake.company_email()

    row = Clients(FirstName=fake_first_name,
                  LastName=fake_last_name,
                  Balance=fake_balance,
                  Birthday=fake_birth_date,
                  Email=fake_email)
    session.add(row)

    print(f"Read the row-{count}")
    count += 1

session.commit()
