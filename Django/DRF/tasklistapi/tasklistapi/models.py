from django.db.models import Model, CharField, TextField, BooleanField

class TaskList(Model):
    title       = CharField(max_length=50)
    description = TextField
    completed   = BooleanField(default=False)

