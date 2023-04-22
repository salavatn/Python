from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base, engine


class TableJob(Base):
    __tablename__ = 'HHjobs'
    id      = Column(Integer, primary_key=True)
    keyword = Column(String(250))
    title   = Column(String(250))
    salary  = Column(String(150))
    employer= Column(String(250))
    address = Column(String(200))
    link    = Column(String(100))
    desc    = Column(Text)


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