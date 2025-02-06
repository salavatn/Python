from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database.db_connection import Base, engine


class TableJob(Base):
    __tablename__ = 'job_vacancies'
    id              = Column(Integer, primary_key=True)
    job_id          = Column(Integer)
    title           = Column(String(200))
    link            = Column(String(250))
    usd_min         = Column(Integer)
    usd_max         = Column(Integer)
    current_min     = Column(Integer)
    current_max     = Column(Integer)
    currency        = Column(Integer, ForeignKey('job_salary_usd.id'))
    city_id         = Column(Integer, ForeignKey('job_city.id'))
    company_id      = Column(Integer, ForeignKey('job_company.id'))
    job_website_id  = Column(Integer, ForeignKey('job_website.id'))
    job_desc_id     = Column(Integer, ForeignKey('job_description.id'))


# Base.metadata.create_all(bind=engine)

TableJob.metadata.create_all(bind=engine)