from sqlalchemy import Column, Integer, String, Text
from database.db_connection import Base, engine

# print('Creating table: JOB_Website')

class TableWebsite(Base):
    __tablename__ = 'JOB_Website'
    id      = Column(Integer, primary_key=True)
    website = Column(String(250))


Base.metadata.create_all(bind=engine)
