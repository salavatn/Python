from pathlib import Path
from dotenv import load_dotenv     
import os                         


load_dotenv(dotenv_path='.env')            

pg_host  = os.getenv('POSTGRES_HOST')       
pg_port  = os.getenv('POSTGRES_PORT')       
pg_db    = os.getenv('POSTGRES_DB')        
pg_user  = os.getenv('POSTGRES_USER')       
pg_psswd = os.getenv('POSTGRES_PASSWORD')  
secret_k = os.getenv('DJANGO_KEY')

BASE_DIR    = Path(__file__).resolve().parent.parent
SECRET_KEY  = secret_k
DEBUG       = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'app_webscrapping',
    'app_db',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'job_finder.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'job_finder.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     pg_db,
        'USER':     pg_user,
        'PASSWORD': pg_psswd,
        'HOST':     pg_host,
        'PORT':     pg_port,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE   = 'UTC'
USE_I18N    = True
USE_TZ      = True
STATIC_URL  = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
