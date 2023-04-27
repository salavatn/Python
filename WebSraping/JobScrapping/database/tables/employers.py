from sqlalchemy import Column, Integer, String, Text
from database.db_connection import Base, engine

# print('Creating table: JOB_Company')

class TableCompany(Base):
    __tablename__ = 'JOB_Company'
    id            = Column(Integer, primary_key=True)
    company       = Column(String(250))
    company_link  = Column(String(250))


Base.metadata.create_all(bind=engine)
