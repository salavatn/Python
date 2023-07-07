from config.library import Model, CharField, DateField


class Clients(Model):
    username = CharField(max_length=20)
    email    = CharField(max_length=50)
    password = CharField(max_length=50)

