from sqlalchemy import Column, Integer, String, Date, Float
from database.db_connection import Base, engine


class TableSalaryUSD(Base):
    __tablename__ = 'job_salary_usd'
    id       = Column(Integer, primary_key=True)
    currency = Column(String(5))
    usd      = Column(Float)
    date     = Column(Date)


# Base.metadata.create_all(bind=engine)
TableSalaryUSD.metadata.create_all(bind=engine)
