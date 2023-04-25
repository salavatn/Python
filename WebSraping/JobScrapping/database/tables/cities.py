from sqlalchemy import Column, Integer, String
from database.db_connection import Base, engine

print("\tFILE 'database/tables/cities.py' is running\n")

class TableCities(Base):
    __tablename__ = 'jobs_cities'
    id   = Column(Integer, primary_key=True)
    city = Column(String(250))


Base.metadata.create_all(bind=engine)

print("\tFILE 'database/tables/cities.py' is finished\n")

# SQL for creating table
# CREATE TABLE jobs_cities (
#     id   SERIAL,
#     city VARCHAR(250),
#     PRIMARY KEY (id)
# );
