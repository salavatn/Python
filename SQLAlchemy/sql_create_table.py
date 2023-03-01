print("\nFILE START: SQL_CREATE_TABLE")
from sql_connection import base, engine
from sql_table_list import TableCustomers

table = TableCustomers
base.metadata.create_all(engine)
print("\tFILE FINISH: SQL_CREATE_TABLE\n")