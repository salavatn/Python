from database.models import Clients
from config.connection import session
from config.libs import Faker

faker = Faker()
count = 0
data  = []

while count < 10:
    first_name  = faker.first_name()
    last_name   = faker.last_name()
    balance     = faker.random_int(11, 243589)
    birthday    = faker.date_of_birth()
    email       = faker.company_email()

    row = {
        "FirstName": first_name,
        "LastName":  last_name,
        "Balance":   balance,
        "Birthday":  birthday,
        "Email":     email,
    }
    data.append(row)
    count += 1


for row in data:
    record = Clients(**row)
    session.add(record)

session.commit()

