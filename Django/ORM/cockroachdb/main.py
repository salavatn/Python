from config.settings import django_start
from database.models import Contacts


fname    = input('Your first name:  ')
lname    = input('Your second name: ')
city     = input('Your city:        ')
birthday = input('Your birthday:    ')


data = {
    'first_name': fname,
    'last_name':  lname,
    'city':       city,
    'birthday':   birthday
}

new_record = Contacts(**data)
new_record.save()

all_data = Contacts.objects.all()
for element in all_data:
    fname = element.first_name
    lname = element.last_name
    city  = element.city
    bday  = element.birthday
    print(f'{fname} {lname} from {city}. Birthday is {bday}')

