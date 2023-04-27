from sqlalchemy import Column, Integer, String, Date, Float
from database.db_connection import Base, engine

# print('Creating table: JOB_Salary_Original')

class TableSalaryAll(Base):
    __tablename__ = 'JOB_Salary_Original'
    id           = Column(Integer, primary_key=True)
    min_original = Column(Integer)
    max_original = Column(Integer)
    currency     = Column(String(10))


class TableSalaryUSD(Base):
    __tablename__ = 'JOB_Salary_USD'
    id                = Column(Integer, primary_key=True)
    currency_from     = Column(String(5))
    currency_USD      = Column(Float)
    convertation_date = Column(Date)


Base.metadata.create_all(bind=engine)
