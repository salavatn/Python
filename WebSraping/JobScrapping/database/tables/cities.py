from sqlalchemy import Column, Integer, String
from database.db_connection import Base, engine

# print('Creating table: JOB_City')

class TableCity(Base):
    __tablename__ = 'JOB_City'
    id   = Column(Integer, primary_key=True)
    city = Column(String(250))


Base.metadata.create_all(bind=engine)
