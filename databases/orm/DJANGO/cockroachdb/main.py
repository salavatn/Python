from config.settings import django_start
from database.models import Contacts


# Section 1: Get data from user
fname    = input('Your first name:  ')
lname    = input('Your second name: ')
city     = input('Your city:        ')
birthday = input('Your birthday:    ')


# Section 2: Prepare data for database
data = {
    'first_name': fname,
    'last_name':  lname,
    'city':       city,
    'birthday':   birthday
}


# Section 3: Save data to database
new_record = Contacts(**data)
new_record.save()


# Section 4: Print all data from database
all_data = Contacts.objects.all()
for element in all_data:
    fname = element.first_name
    lname = element.last_name
    city  = element.city
    bday  = element.birthday
    print(f'{fname} {lname} from {city}. Birthday is {bday}')

