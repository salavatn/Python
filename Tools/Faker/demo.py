from faker import Faker


# Section 1: create instance of Faker()
fake = Faker('en_EN')


# Section 2: generate fake data
first_name  = fake.first_name()
last_name   = fake.last_name()
balance     = fake.random_int(11, 243589)
birthday    = fake.date_of_birth().strftime('%Y-%m-%d')
email       = fake.company_email()


# Section 3: create dictionary data
data = {
    'firstname': first_name, 
    'lastname': last_name, 
    'balance': balance, 
    'birth_date': birthday, 
    'email': email}


# Section 4: print data
print(data)


# Example output:
# {'firstname': 'Kaitlyn', 'lastname': 'Murphy', 'balance': 107777, 'birth_date': '1938-06-27', 'email': 'qwalker@duncan-clark.com'}
# {'firstname': 'David', 'lastname': 'Bowman', 'balance': 112100, 'birth_date': '1955-05-28', 'email': 'kthompson@graham.com'}
# {'firstname': 'Diane', 'lastname': 'Scott', 'balance': 63465, 'birth_date': '2022-07-11', 'email': 'xhancock@blankenship.com'}
