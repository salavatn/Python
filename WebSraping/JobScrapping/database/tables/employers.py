from sqlalchemy import Column, Integer, String, Text
from database.db_connection import Base, engine

print("file 'database/tables/employers.py' is running\n")

class TableCompany(Base):
    __tablename__ = 'jobs_company'
    id          = Column(Integer, primary_key=True)
    company     = Column(String(250))
    website     = Column(String(200))
    description = Column(Text)

# SQL for creating table
# CREATE TABLE jobs_company (
#     id          SERIAL,
#     company     VARCHAR(250),
#     website     VARCHAR(200),
#     description TEXT,
#     PRIMARY KEY (id)
# );


Base.metadata.create_all(bind=engine)

print("\tFILE 'database/tables/employers.py' is finished\n")