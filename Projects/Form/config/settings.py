from config.library import django, dj_database_url
from config.library import load_dotenv, os


# Section 1: Environment variables
load_dotenv(dotenv_path='.env')
db_user = os.getenv('POSTGRESQL_USER')
db_pswd = os.getenv('POSTGRESQL_PSWD')
db_host = os.getenv('POSTGRESQL_HOST')
db_port = os.getenv('POSTGRESQL_PORT')
db_name = os.getenv('POSTGRESQL_NAME')


# Section 2: Django ORM settings
url_database    = f'postgresql://{db_user}:{db_pswd}@{db_host}:{db_port}/{db_name}?sslmode=verify-full'
DATABASES       = {'default': dj_database_url.config(default=url_database, engine='django_cockroachdb')}
INSTALLED_APPS  = ['database', 'dj_database_url', 'django_cockroachdb']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Section 3: Initialize Django
django_start = django.setup()