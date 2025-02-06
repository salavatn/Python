from app.config.settings import django_start
from django.db.models import Model, ForeignKey, CASCADE
from django.db.models import CharField, DateField, EmailField, BooleanField
from datetime import datetime


# Table 1: app_users
class Users(Model):
    firstname   = CharField(max_length=20)
    lastname    = CharField(max_length=20)
    password    = CharField(max_length=40)
    emailaddr   = EmailField(max_length=35)
    created_at  = DateField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    status      = BooleanField(default=True)

    class Meta:
         db_table = 'app_users'


# Table 2: app_notes
class Notes(Model):
    user_id     = ForeignKey(Users, on_delete=CASCADE)
    title       = CharField(max_length=100)
    content     = CharField(max_length=255)
    created     = DateField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    updated     = DateField(null=True)

    class Meta:
        db_table = 'app_notes'
