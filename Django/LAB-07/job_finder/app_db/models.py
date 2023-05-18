from django.db.models import Model, CharField, IntegerField, ForeignKey, AutoField, TextField, FloatField, DateField, CASCADE


class Vacancies(Model):
    id        = AutoField(primary_key=True)
    job_id    = IntegerField()
    job_title = CharField(max_length=200)
    job_link  = CharField(max_length=250)
    salary_min_usd = IntegerField(null=True)
    salary_max_usd = IntegerField(null=True)
    salary_min     = IntegerField(null=True)
    salary_max     = IntegerField(null=True)
    currency    = CharField(max_length=10, null=True) #ForeignKey('Currencies', on_delete=CASCADE, null=True)   
    city        = ForeignKey('Location', on_delete=CASCADE)
    company     = ForeignKey('Companies', on_delete=CASCADE)
    resource    = ForeignKey('Resource', on_delete=CASCADE)
    desc        = ForeignKey('Descriptions', on_delete=CASCADE)
    published   = DateField()


class Resource(Model):
    link = CharField(max_length=250)


class Location(Model):
    city    = CharField(max_length=100)
    country = CharField(max_length=100, default=None)


class Companies(Model):
    company = CharField()
    city    = ForeignKey('Location', on_delete=CASCADE)
    link    = CharField(max_length=250)


class Descriptions(Model):
    text = TextField()


class Currencies(Model):
    currency = CharField(max_length=10)
    usd      = FloatField()
    date     = DateField()
