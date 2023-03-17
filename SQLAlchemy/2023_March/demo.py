from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# Connection Parameters
host = 'db.zfcwzrekfaadppegzqmw.supabase.co'
port = '5432'
database = 'postgres'
username = 'postgres'
password = 'zfcwzrekfaadppegzqmw'

# SQL Alchemy connections to PostgreSQL
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=True)
base = declarative_base()
session_maker = sessionmaker(bind=engine)
session = session_maker()


class Customers(base):
    __tablename__ = 'Customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)


base.metadata.create_all(engine)

# count = 1
# while count <= 5:
row = Customers(first_name='Brian2', last_name="Griffin",
                email='BrianPumkin@example.com')
# session.add(row)
    # print(f"read the row-{count}")
    # count += 1


# session.begin(nested=True)
# session.add(instance=row)   # _warn=True
result = session.query(Customers)

for data in result:
    print(data.first_name)


session.commit()



# Jinja2, Pug