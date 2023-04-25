from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database.db_connection import Base, engine

print("\tFILE 'database/tables/job.py' is running\n")

class TableJob(Base):
    __tablename__ = 'jobs_hhru'
    id          = Column(Integer, primary_key=True)
    job_id      = Column(String(50))
    title       = Column(String(200))
    salary      = Column(String(50))
    city_id     = Column(Integer)#, ForeignKey('jobs_cities.id'))
    company_id  = Column(Integer)#, ForeignKey('jobs_company.id'))
    description = Column(Text)


Base.metadata.create_all(bind=engine)

print("\tFILE 'database/tables/job.py' is finished\n")