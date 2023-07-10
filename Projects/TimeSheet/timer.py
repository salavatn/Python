from rich.console import Console
from rich.table import Table
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import and_
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from datetime import date, datetime
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

user_args = sys.argv

table = TableTimeSheet
today = date.today()
time_now = int(time.time())


def upload_and_update(task_name):

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


def write_task_name():
    task_name_key = user_args.index(key_task) + 1
    task_name_value = user_args[task_name_key].upper()
    upload_and_update(task_name_value)


def convert_unix_time(unix_time):
    result = datetime.utcfromtimestamp(unix_time).strftime('%H:%M:%S')
    return result


def convert_second(t_sec):
    if t_sec >= 60:
        t_min = int(t_sec / 60)
        if t_min >= 60:
            t_hours = int(t_min / 60)
            minutes = t_min - t_hours * 60
            return f"{t_hours}:{minutes} H"
        else:
            second = t_sec - t_min * 60
            if second <= 9:
                return f"{t_min}:0{second} M"
            return f"{t_min}:{second} M"
    else:
        if t_sec <= 9:
            return f"0:0{t_sec} M"
        return f"0:{t_sec} M"


def get_result_table():
    result_table_name = Table(title="\nTask Tracker TimeSheet")
    result_table_column = ["ID", "Date", "Task Name", "Started", "Finished", "Duration"]
    result_table_rows = []

    table_data = session.query(table).order_by(table.ID)
    for data in table_data:
        task_id = str(data.ID)
        task_date = str(data.Date)
        task_name = data.Task_Name
        task_start = convert_unix_time(data.Task_Started)
        task_finish = convert_unix_time(data.Task_Finished)
        task_duration = convert_second(data.Task_Duration)
        table_row = []
        table_row += task_id, task_date, task_name, task_start, task_finish, task_duration
        result_table_rows.append(table_row)

    for column in result_table_column:
        result_table_name.add_column(column)

    for row in result_table_rows:
        result_table_name.add_row(*row, style='bright_green')

    console = Console()
    console.print(result_table_name)


key_task = '--task'
key_result = '--result'


if key_task in user_args:
    write_task_name()

if key_result in user_args:
    get_result_table()


'''SQL Query:

    SELECT 
      "Date", 
      "Task_Name" AS "Task Name", 
      SUM ("Task_Duration") AS "Duration"
    FROM "TimeSheet"
    GROUP BY "Task_Name", "Date"
    ORDER BY SUM ("Task_Duration") DESC;

'''