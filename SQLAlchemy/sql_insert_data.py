print("\nFILE START: SQL_INSERT_DATA")

from sql_connection import session
from sql_table_list import TableCustomers

table = TableCustomers
# # Sample Data
row_0 = table(name="Marry", age=26, grade="R")
session.add(row_0)


row_1 = table(name="Fredy", age=38, grade="C")
row_2 = table(name="Mark", age=42, grade="D")
row_3 = table(name="Jack", age=21, grade="A")
row_4 = table(name="Brain", age=38, grade="B")
row_5 = table(name="Alice", age=41, grade="E")


# INSERT MORE DATA
session.add_all([row_1, row_2, row_3, row_4, row_5])
session.commit()

print("\tFILE FINISH: SQL_INSERT_DATA\n")

