from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from fastapi import FastAPI

# Connection Parameters
host = 'db.zorvmuaqwcpbfqjpifmo.supabase.co'
port = '5432'
database = 'postgres'
username = 'postgres'
password = 'zorvmuaqwcpbfqjpifmo'

# SQL Alchemy connections to PostgreSQL
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=False)
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


query = session.query(Clients)

fake_users = []
count = 1
for data in query:
    count += 1
    if count <= 10:
        raw = {"ID": data.ID, "FirstName": data.FirstName, "LastName": data.LastName, "Balance": data.Balance}
        fake_users.append(raw)
    else:
        break

session.commit()


app = FastAPI(
    title="Trading App"
)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in fake_users:
        if user.get("ID") == user_id:
            return user





# data = get_user(1)
# print(data)
