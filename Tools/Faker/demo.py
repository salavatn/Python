from faker import Faker

fake = Faker()


first_name  = fake.first_name()
last_name   = fake.last_name()
balance     = fake.random_int(11, 243589)
birthday  = fake.date_of_birth().strftime('%Y-%m-%d')
email       = fake.company_email()

data = {
    'firstname': first_name, 
    'lastname': last_name, 
    'balance': balance, 
    'birth_date': birthday, 
    'email': email}

print(data)

# Output:
# {'firstname': 'Michael', 'lastname': 'Hernandez', 'balance': 243589, 'birth_date': '1997-01-01', 'email': '
