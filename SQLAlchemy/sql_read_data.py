print("\nFILE START: SQL_READ_DATA")
from sql_connection import session
from sql_table_list import TableCustomers

table = TableCustomers
query = session.query(table).order_by(table.name).filter(table.age <= 30)

for get in query:
    print(f"\tget.name: {get.name}, \tget.age: {get.age}, \tget.grade: {get.grade}")



print("\tFILE FINISH: SQL_READ_DATA\n")
