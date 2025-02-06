from sqlalchemy import Column, Integer, String
from database.db_connection import Base, engine

# print('Creating table: JOB_Company')

class TableCompany(Base):
    __tablename__ = 'job_company'
    id          = Column(Integer, primary_key=True)
    name        = Column(String(250))
    link        = Column(String(250))
    company_id  = Column(Integer)

# Base.metadata.create_all(bind=engine)
TableCompany.metadata.create_all(bind=engine)
