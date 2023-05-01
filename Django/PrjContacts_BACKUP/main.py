import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PrjContacts.PrjContacts.settings')

import django

django.setup()

from AppContacts.models import Contacts


new_contact = Contacts(
    FirstName='Имя',
    LastName='Фамилия',
    City='Город',
    Email='email@example.com',
    Birthday='2000-01-01'
)

new_contact.save()
