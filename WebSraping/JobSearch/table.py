from sqlalchemy import Column, Integer, String
from database import Base, engine


class TableVacancies(Base):
    __tablename__ = 'ListVacancies'
    id      = Column(Integer, primary_key=True)
    keyword = Column(String(50))
    title   = Column(String(100))
    salary  = Column(String(50))
    employer= Column(String(200))
    address = Column(String(50))
    link    = Column(String(100))



class TableFullVacancyDesc(Base):
    __tablename__ = 'DescriptionVacancies'
    id      = Column(Integer, primary_key=True)
    title   = Column(String(100))
    salary  = Column(String(50))
    employer= Column(String(200))
    address = Column(String(50))
    link    = Column(String(100))


Base.metadata.create_all(bind=engine)