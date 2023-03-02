print("FILE START: SQL_READ_DATA")
from sql_connection import session
from sql_table_list import TableCustomers


# Test
table = TableCustomers
# query = session.query(table).order_by(table.name).filter(table.age <= 30)

query = session.query(table).filter(table.id == 1)

for get in query:
    # print(f"\n\tget.name: {get.name}, \tget.age: {get.age}, \tget.grade: {get.grade}")
    print(get.name)
    get.name = "Antonio"
    session.commit()
    print(get.name)








# print("\tFILE FINISH: SQL_READ_DATA\n")
