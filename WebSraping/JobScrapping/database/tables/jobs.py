from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database.db_connection import Base, engine

# print('Creating table: JOB_on_HHru')

class TableJob(Base):
    __tablename__ = 'JOB_on_HHru'
    id              = Column(Integer, primary_key=True)
    job_id          = Column(String(50))
    job_title       = Column(String(200))
    salary_min      = Column(Integer)
    salary_max      = Column(Integer)
    id_salary_all   = Column(Integer, ForeignKey('JOB_Salary_Original.id'))
    job_link        = Column(String(250))
    id_city_name    = Column(Integer, ForeignKey('JOB_City.id'))
    id_company_name = Column(Integer, ForeignKey('JOB_Company.id'))
    id_website      = Column(Integer, ForeignKey('JOB_Website.id'))
    id_description  = Column(Integer, ForeignKey('JOB_Description.id'))


Base.metadata.create_all(bind=engine)
