from sqlalchemy import Column, Integer, Text
from database.db_connection import Base, engine

# print('Creating table: JOB_Description')

class TableDescription(Base):
    __tablename__ = 'JOB_Description'
    id       = Column(Integer, primary_key=True)
    job_desc = Column(Text)


Base.metadata.create_all(bind=engine)
