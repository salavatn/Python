from sqlalchemy import Column, Integer, String
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
    id      = Column(Integer, primary_key=True)
    min_usd = Column(Integer)
    max_usd = Column(Integer)


Base.metadata.create_all(bind=engine)
