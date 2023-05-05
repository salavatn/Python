# Django ORM - Запросы

**Оглавление:**
- [Создание Django Проекта](#создание-django-проекта)
  - [1. Создание проекта](#1-создание-проекта)
    - [1.1. Подготовка виртуального окружения](#11-подготовка-виртуального-окружения)
    - [1.2. Знакомство с django-admin](#12-знакомство-с-django-admin)
    - [1.3. Создание нового проекта](#13-создание-нового-проекта)
  - [2. Тестовый запуск веб-приложения](#2-тестовый-запуск-веб-приложения)


## 1. Подготовка проекта 


<details markdown="1"> 
<summary>1.01. Подготовить виртуальное окружение </summary>
<br>
<code>LAB-05/</code>
<pre><code>python -m venv venv            
source venv/bin/activate      
</code></pre>
</details>

<details markdown="1"> 
<summary>1.02. Добавить библиотеки в requirements.txt и установить</summary>
<br>
<code>LAB-05/</code>
<pre><code>echo django             >> requirements.txt    
echo django-extensions  >> requirements.txt   
echo psycopg2-binary    >> requirements.txt      
echo python-dotenv      >> requirements.txt    
<br>
pip install -r requirements.txt            
</code></pre>
</details>

<details markdown="1"> 
<summary>1.03. Создать проект "FranceCars"</summary>
<br>
<code>LAB-05/</code>
<pre><code>django-admin startproject FranceCars</code></pre>
</details>

<details markdown="1"> 
<summary>1.04. Сформируйте .env с параметрами подключения к PostgeSQL</summary>
<br>
<code>LAB-05/FranceCars/.env:</code>
<pre><code>POSTGRES_HOST=127.0.0.1    
POSTGRES_PORT=5432       
POSTGRES_DB=postgres       
POSTGRES_USER=postgres      
POSTGRES_PASSWORD=Pa$$word  
</code></pre>
</details>

<details markdown="1"> 
<summary>1.05. Подгрузите переменные из .env в settings.py</summary>
<br>
<code>LAB-05/FranceCars/FranceCars/settings.py:</code>
<pre><code>from dotenv import load_dotenv     
import os                         
<br>
load_dotenv(dotenv_path='.env')            
pg_host  = os.getenv('POSTGRES_HOST')       
pg_port  = os.getenv('POSTGRES_PORT')       
pg_db    = os.getenv('POSTGRES_DB')        
pg_user  = os.getenv('POSTGRES_USER')       
pg_psswd = os.getenv('POSTGRES_PASSWORD')   
</code></pre>
</details>

<details markdown="1"> 
<summary>1.06. Настройте в settings.py подключение к PostgreSQL</summary>
<br>
<code>LAB-05/FranceCars/FranceCars/settings.py:</code>
<pre><code>DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     pg_db,
        'USER':     pg_user,
        'PASSWORD': pg_psswd,
        'HOST':     pg_host,
        'PORT':     pg_port,
    }
}
</code></pre>
</details>

<details markdown="1"> 
<summary>1.07. Запустите миграцию</summary>
<br>
<code>LAB-05/FranceCars/</code>
<pre><code>./manage.py migrate </code></pre>
</details>

<details markdown="1"> 
<summary>1.08. Зарегистрировать приложение django_extensions</summary>
<br>
<code>LAB-05/FranceCars/FranceCars/settings.py:</code>
<pre><code>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',            # New
]</code></pre>
</details>

<details markdown="1"> 
<summary>1.09. Создать новое приложение "Automobiles"</summary>
<br>
<code>LAB-05/FranceCars/</code>
<pre><code>./manage.py startapp Automobiles</code></pre>
</details>

<details markdown="1"> 
<summary>1.10. Зарегистрировать приложение "Automobiles"</summary>
<br>
<code>LAB-05/FranceCars/FranceCars/settings.py:</code>
<pre><code>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'Automobiles',                  # New
]</code></pre>
</details>

<details markdown="1"> 
<summary>1.11. Создайте модель для "Automobiles"</summary>
<br>
<code>LAB-05/FranceCars/Automobiles/models.py:</code>
<pre><code>from django.db import models
<br>
class TableAutomobiles(models.Model):
    id          = models.AutoField(primary_key=True)
    Model       = models.CharField(max_length=50)
    Year        = models.IntegerField()
    Color       = models.CharField(max_length=50)
    Price       = models.IntegerField()
    EngineSize  = models.IntegerField()
    VIN         = models.CharField(max_length=50)
</code></pre>
</details>

<details markdown="1"> 
<summary>1.12. Создайте файлы миграции и запустите миграцию</summary>
<br>
<code>LAB-05/FranceCars/</code>
<pre><code>./manage.py makemigrations Automobiles
./manage.py migrate </code></pre>
</details>

**К этому шагу вы должны иметь:**
Структура проекта:
```sh
LAB-05/
├── FranceCars/
│   ├── FranceCars/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── Automobiles/            
│   │   ├── migrations/      
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py
│   │   │
│   │   ├── __init__.py      
│   │   ├── admin.py         
│   │   ├── apps.py         
│   │   ├── models.py        
│   │   ├── tests.py        
│   │   └── views.py         
│   │   
│   ├── .env
│   └── manage.py  
│
├── venv/
├── README.md
└── requirements.txt
```

Таблицы в базе данных PostgreSQL:
| table_name                 |
| -------------------------- |
| Automobiles_automobiles    |
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
