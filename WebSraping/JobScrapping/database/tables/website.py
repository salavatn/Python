from sqlalchemy import Column, Integer, String, Text
from database.db_connection import Base, engine

# print('Creating table: JOB_Website')

class TableWebsite(Base):
    __tablename__ = 'job_website'
    id  = Column(Integer, primary_key=True)
    url = Column(String(250))


# Base.metadata.create_all(bind=engine)
TableWebsite.metadata.create_all(bind=engine)
