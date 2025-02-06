from sqlalchemy import Column, Integer, Text
from database.db_connection import Base, engine

# print('Creating table: JOB_Description')

class TableDescription(Base):
    __tablename__ = 'job_description'
    id   = Column(Integer, primary_key=True)
    text = Column(Text)


# Base.metadata.create_all(bind=engine)
TableDescription.metadata.create_all(bind=engine)
