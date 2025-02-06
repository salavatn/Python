# from app.config.settings import django_start
from app.config.settings import db_host, db_port, db_name, db_user, db_pswd
from django.core.management import execute_from_command_line
import dj_database_url
from django import setup
from sys import argv




# Section 2: Django ORM settings
url_database   = f'postgresql://{db_user}:{db_pswd}@{db_host}:{db_port}/{db_name}'
DATABASES      = {'default': dj_database_url.config(default=url_database, engine='postgresql')}
INSTALLED_APPS = ['app.database', 'dj_database_url']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Section 3: Initialize Django
django_start   = setup()



# Section 1: Django CLI
execute_from_command_line(argv)
