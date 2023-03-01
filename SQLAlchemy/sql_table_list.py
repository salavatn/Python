print("\nFILE START: SQL_TABLE_LIST")
from sql_connection import base
from sqlalchemy import Column, Integer, String


class TableCustomers(base):
    __tablename__ = 'Customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


print("\tFILE FINISH: SQL_TABLE_LIST\n")
