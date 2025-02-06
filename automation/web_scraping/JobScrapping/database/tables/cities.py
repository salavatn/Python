from sqlalchemy import Column, Integer, String
from database.db_connection import Base, engine


class TableCity(Base):
    __tablename__ = 'job_city'
    id   = Column(Integer, primary_key=True)
    name = Column(String(250))


# Base.metadata.create_all(bind=engine)
TableCity.metadata.create_all(bind=engine)
