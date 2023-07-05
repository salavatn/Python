from app.library import Model, CharField, DateField

class Contacts(Model):
    first_name  = CharField(max_length=20,  null=False)
    last_name   = CharField(max_length=20,  null=False)
    city        = CharField(max_length=210, null=False)
    birthday    = DateField(null=False)
    
