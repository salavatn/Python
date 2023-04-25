from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database.db_connection import Base, engine


class TableSkill(Base):
    __tablename__ = 'HHskills'
    id      = Column(Integer, primary_key=True)
    skill   = Column(String(100))


class TableLink(Base):
    __tablename__ = 'HH_Links'
    ID       = Column(Integer, primary_key=True)
    Job_ID   = Column(Integer, ForeignKey('HH_Jobs.id'))
    Skill_ID = Column(Integer, ForeignKey('HH_Skills.id'))


Base.metadata.create_all(bind=engine)