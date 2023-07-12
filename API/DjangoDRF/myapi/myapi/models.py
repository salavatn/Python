from django.db.models import Model, CharField, EmailField


class Contacts(Model):
    username = CharField(max_length=100)
    city     = CharField(max_length=100)
    email    = EmailField()

