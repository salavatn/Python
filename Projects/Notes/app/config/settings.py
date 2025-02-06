from dotenv import load_dotenv
from django import setup
import dj_database_url
from os import getenv


# Section 1: Load environment variables
load_dotenv(dotenv_path='.env')
db_user = getenv('DB_USER')
db_pswd = getenv('DB_PSWD')
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')
db_name = getenv('DB_NAME')




# Section 2: Django ORM settings
url_database   = f'postgresql://{db_user}:{db_pswd}@{db_host}:{db_port}/{db_name}'
DATABASES      = {'default': dj_database_url.config(default=url_database, engine='postgresql')}
INSTALLED_APPS = ['app.database', 'dj_database_url']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Section 3: Initialize Django
django_start   = setup()







# # Section 2: Django settings
# DATABASES = {
#     'default': {
#         'ENGINE':   'django.db.backends.postgresql',
#         'NAME':     db_name,
#         'USER':     db_user,
#         'PASSWORD': db_pswd,
#         'HOST':     db_host,
#         'PORT':     db_port,
#         }
#     }
# INSTALLED_APPS     = ['database',]
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# # Section 3: Django setup
# django_start = setup()