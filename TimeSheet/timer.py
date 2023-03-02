from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import and_
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from datetime import date
import sys
import os
import time


def connect_to_database():
    load_dotenv()
    host = os.environ['SQL_TM_HOST']
    database = os.environ['SQL_TM_DB']
    port = os.environ['SQL_TM_PORT']
    username = os.environ['SQL_TM_USER']
    password = os.environ['SQL_TM_PASSWD']

    tm_engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}', echo=False)
    tm_base = declarative_base()
    tm_session_maker = sessionmaker(bind=tm_engine)
    tm_session = tm_session_maker()
    return [tm_base, tm_session, tm_engine]


base = connect_to_database()[0]
session = connect_to_database()[1]
engine = connect_to_database()[2]


class TableTimeSheet(base):
    __tablename__ = 'TimeSheet'
    ID = Column(Integer, primary_key=True)
    Date = Column(Date)
    Task_Name = Column(String)
    Task_Started = Column(Integer)
    Task_Finished = Column(Integer)
    Task_Duration = Column(Integer)


# Create Table
base.metadata.create_all(engine)


# Parameters for query:
table = TableTimeSheet
today = date.today()
task_name = sys.argv[1]
time_now = int(time.time())


# Upload data to PostgreSQL
def upload_data():
    row = table(Date=today,
                Task_Name=task_name,
                Task_Started=time_now,
                Task_Finished=time_now,
                Task_Duration=0)
    session.add(row)
    session.commit()


exist_record = session.query(table).filter_by(Date=today).first() is not None     # True or False

if exist_record is True:
    upload_data()
    print("Uploaded the next record")
    current_row = session.query(table).filter_by(Task_Started=time_now)

    for get_current in current_row:
        prev_row_id = get_current.ID - 1
        prev_row = session.query(table).filter(table.ID == prev_row_id)

        for get_prev in prev_row:
            get_prev.Task_Finished = time_now
            time_prev = get_prev.Task_Started
            get_prev.Task_Duration = time_now - time_prev
            session.commit()
            print("Previous record is updated")
else:
    upload_data()
    print("Uploaded new record")

