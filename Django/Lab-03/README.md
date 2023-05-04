# Создание Django Приложение

**Оглавление:**
- [Создание Django Приложение](#создание-django-приложение)
  - [1. Самостоятельная подготовка:](#1-самостоятельная-подготовка)
  - [2. Создание Django-приложение](#2-создание-django-приложение)
  - [3. Регистрация созданного приложения](#3-регистрация-созданного-приложения)
  - [4. Добавить модели для PostgreSQL](#4-добавить-модели-для-postgresql)
  - [5. Создать миграции](#5-создать-миграции)
    - [5.1. Новые файлы миграции](#51-новые-файлы-миграции)
    - [5.2. Миграция](#52-миграция)


## 1. Самостоятельная подготовка:
1. Создайте виртуальное окружение (`venv`)
2. Установите библиотеки 
    - `django`
    - `psycopg2-binary`
    - `python-dotenv`
3. Создайте Django проект `University`
4. Создайте `.env` и добавьте переменные окружения для подключения к PostgreSQL
5. Настройте подключение к PostgreSQL в файле `University/settings.py` 
6. Запустите процедуру миграции
7. Проверьте, что в базе данных PostgreSQL создались системные таблицы:
    - auth_group 
    - auth_group_permissions    
    - auth_permission            
    - auth_user                  
    - auth_user_groups           
    - auth_user_user_permissions 
    - django_admin_log           
    - django_content_type        
    - django_migrations          
    - django_session             
8. У вас должна получиться следующая структура проекта:

```sh
LAB-03/
├── University/   
│   ├── University/        
│   │   ├── __init__.py 
│   │   ├── asgi.py       
│   │   ├── settings.py   
│   │   ├── urls.py       
│   │   └── wsgi.py     
│   │   
│   ├── .env
│   └── manage.py         
│
├── venv/
├── README.md
└── requirements.txt
```
---
```sh
pip list
```
```log
Package         Version
--------------- -------
asgiref         3.6.0
Django          4.2.1
pip             23.1.2
psycopg2-binary 2.9.6
python-dotenv   1.0.0
setuptools      65.5.0
sqlparse        0.4.4
```
 

## 2. Создание Django-приложение

```sh
cd University
./manage.py startapp Students
```

> Создаем новое приложение Django с именем "**Students**" внутри проекта "**University**". Команда `startapp` создает структуру каталогов для приложения и набор файлов, таких как `models.py`, `views.py` и `urls.py`:


* В результате выполнения команды структура каталогов должна выглядеть примерно так:
```sh
LAB-03/
├── University/
│   ├── University/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── Students/            # New
│   │   ├── migrations/      # New
│   │   │   └── __init__.py  # New
│   │   ├── __init__.py      # New
│   │   ├── admin.py         # New
│   │   ├── apps.py          # New
│   │   ├── models.py        # New
│   │   ├── tests.py         # New
│   │   └── views.py         # New
│   │   
│   ├── .env
│   └── manage.py  
│
├── venv/
├── README.md
└── requirements.txt
```

## 3. Регистрация созданного приложения
> После создания приложения `Students`, его нужно будет зарегистрировать в файле `settings.py` проекта, добавив имя приложения в список `INSTALLED_APPS`. 
<!-- > Кроме того, вам необходимо будет настроить маршрутизацию **URL** для приложения, определив соответствующие URL-адреса в файле `urls.py` приложения и добавив их в основной файл `urls.py` проекта. -->

* Откройте файл `University/University/settings.py`
* Найдите список установленных приложений **INSTALLED_APPS**.
* Добавьте `'Students'` в список установленных приложений:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Students',                     # Новое приложение
]
```
* Сохраните изменения в файле `settings.py`. 
* Теперь приложение **Students** будет установлено в проект Django.


## 4. Добавить модели для PostgreSQL

* Откройте файл `University/Students/models.py`
* Добавьте модели для базы данных, например:
  
```python
from django.db import models


class TableStudents(models.Model):
    FirstName   = models.CharField(max_length=50)
    LastName    = models.CharField(max_length=50)
    City        = models.CharField(max_length=50)
    Email       = models.EmailField()
    Birthday    = models.DateField()
```



## 5. Создать миграции
> Создаем новые файлы миграции на основе изменений, внесенных в модели приложения **Students**. Она анализирует текущее состояние моделей и сравнивает их с последней примененной миграцией, а затем генерирует необходимые SQL-команды для создания или изменения таблиц базы данных на основе изменений:

### 5.1. Новые файлы миграции
```sh
./manage.py makemigrations Students
```

```
Migrations for 'Students':
  Students/migrations/0001_initial.py
```
Вывод показывает, что создан новый файл миграции `0001_initial.py`, который будет содержать необходимые SQL-команды для начальной настройки модели **Students** в базе данных.

```sh
LAB-03/
├── University/
│   ├── University/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── Students/            
│   │   ├── migrations/      
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py  # New
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


### 5.2. Миграция
* Выполняем все необходимые миграции, создавая соответствующие таблицы в базе данных.
```sh
./manage.py migrate
```
```
Operations to perform:
  Apply all migrations: Students, admin, auth, contenttypes, sessions
Running migrations:
  Applying Students.0001_initial... OK
```

* Была создана таблица `Students_tablestudents` для модели **TableStudents** в приложении **Students**.
  

