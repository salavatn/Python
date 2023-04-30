# Django ORM

<!-- Оглавление: -->


## Подготовка проекта

* Создаем виртуальное окружение Python в текущем рабочем каталоге с именем "venv". 
* Активируем виртуальное окружение. 
* Обновляет установленную версию pip до последней версии. 
* Выводим список всех установленных пакетов Python в текущем виртуальном окружении.

```sh
python -m venv venv
source venv/bin/activate
pip install --upgrade pip 
pip list
```
```
Package    Version
---------- -------
pip        23.1.2
setuptools 65.5.0
```

---

* Добавляем строку `django` в файл "requirements.txt" 
* Добавляем строку `psycopg2-binary` в файл "requirements.txt", эта библиотека для работы с PostgreSQL.
* Устанавливаем все зависимости, перечисленные в файле "requirements.txt". 

```sh 
echo django          >> requirements.txt
echo psycopg2-binary >> requirements.txt

pip install -r requirements.txt
pip list
```

```
pip list
Package    Version
---------- -------
asgiref    3.6.0
Django     4.2
pip        23.1.2
setuptools 65.5.0
sqlparse   0.4.4
```

---

Cтруктура каталогов проекта **Django**. Краткое описание каждого элемента:

* **venv/** - Виртуальное окружение Python. Содержит все установленные зависимости, которые нужны для запуска проекта.
* **README.md** - Содержит описание проекта.
* **requirements.txt** - Файл, содержащий список всех зависимостей проекта. Можно создать командой `pip freeze > requirements.txt`.

```
DJANGO/
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
│
├── README.md
└── requirements.txt
```


## Знакомство с Django Admin

* Команда выводит версию Django:
```sh
django-admin --version
```
```
4.2
```

<br>

---
<br>

* Команда выводит список доступных команд и их описание для django-admin. django-admin - это утилита командной строки, предоставляемая Django, которая позволяет выполнять различные задачи, такие как создание приложений, миграция базы данных, управление пользователями и группами и многое другое:

```sh
django-admin --help
```
```
Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```

## Создание нового проекта

* Создаем новый Django-проект с именем **PrjContacts**. Django-проект - это набор настроек и приложений, необходимых для создания веб-приложения. Команда `startproject` создает структуру каталогов проекта и набор файлов конфигурации Django, таких как `settings.py`, `urls.py` и `wsgi.py`.

```sh
django-admin startproject PrjContacts
```

* В результате выполнения команды структура каталогов должна выглядеть примерно так:

```
DJANGO/
├── PrjContacts/            # New
│   ├── PrjContacts/        # New
│   │   ├── __init__.py     # New
│   │   ├── asgi.py         # New
│   │   ├── settings.py     # New
│   │   ├── urls.py         # New
│   │   └── wsgi.py         # New
│   │   
│   └── manage.py           # New
│
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
│
├── README.md
└── requirements.txt
```
* Файл `manage.py` - это файл управления **Django**, который используется для запуска различных команд, связанных с проектом. Например, с помощью `manage.py runserver` можно запустить локальный веб-сервер для разработки и отладки приложения.


## Создание нового приложения
* Создаем новое приложение Django с именем "**AppContacts**" внутри проекта "**PrjContacts**". Django-приложение - это компонент проекта, который выполняет определенную функцию, такую как управление контактами, обработка форм или отображение списка новостей. Команда `startapp` создает структуру каталогов для приложения и набор файлов, таких как `models.py`, `views.py` и `urls.py`:

```sh
cd PrjContacts
python manage.py startapp AppContacts
```

* В результате выполнения команды структура каталогов должна выглядеть примерно так:
```
DJANGO/
├── PrjContacts/
│   ├── AppContacts/                # New
│   │   ├── migrations/             # New
│   │   │   └── __init__.py         # New
│   │   ├── __init__.py             # New
│   │   ├── admin.py                # New
│   │   ├── apps.py                 # New
│   │   ├── models.py               # New
│   │   ├── tests.py                # New
│   │   └── views.py                # New
│   │
│   ├── PrjContacts/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │   
│   └── manage.py
│
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
│
├── README.md
└── requirements.txt
```
* После создания приложения `AppContacts`, его нужно будет зарегистрировать в файле `settings.py` проекта, добавив имя приложения в список `INSTALLED_APPS`. Кроме того, вам необходимо будет настроить маршрутизацию **URL** для приложения, определив соответствующие URL-адреса в файле `urls.py` приложения и добавив их в основной файл `urls.py` проекта.


## Добавление нового приложения

* Откройте файл `PrjContacts/PrjContacts/settings.py`
* Найдите список установленных приложений **INSTALLED_APPS**.
* Добавьте `'AppContacts'` в список установленных приложений:

```python
INSTALLED_APPS = [
    'AppContacts',              # Новое приложение
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
* Сохраните изменения в файле `settings.py`. 
* Теперь приложение **AppContacts** будет установлено в проект Django.


## Добавить подключение к БД PostgreSQL
* Откройте файл `PrjContacts/PrjContacts/settings.py` в текстовом редакторе.
* Найдите блок настроек базы данных `DATABASES`.
* Замените настройки базы данных в блоке **DATABASES** на следующий код:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     'имя_базы_данных',
        'USER':     'пользователь',
        'PASSWORD': 'пароль',
        'HOST':     'адрес_хоста',
        'PORT':     'порт',
    }
}
```
* Сохраните изменения в файле `settings.py`. 
* Теперь проект Django будет использовать базу данных `PostgreSQL` с указанными параметрами.


## Добавить модели для PostgreSQL

* Откройте файл `PrjContacts/AppContacts/models.py`
* Добавьте модели для базы данных, например:
  
```python
from django.db import models


class Contacts(models.Model):
    FirstName   = models.CharField(max_length=50)
    LastName    = models.CharField(max_length=50)
    City        = models.CharField(max_length=50)
    Email       = models.EmailField()
    Birthday    = models.DateField()

```

## Создать миграции
* Создаем новые файлы миграции на основе изменений, внесенных в модели приложения **AppContacts**. Она анализирует текущее состояние моделей и сравнивает их с последней примененной миграцией, а затем генерирует необходимые SQL-команды для создания или изменения таблиц базы данных на основе изменений:

```sh
python manage.py makemigrations AppContacts
```

* Вывод показывает, что создан новый файл миграции `0001_initial.py`, который будет содержать необходимые SQL-команды для начальной настройки модели **Contacts** в базе данных.
```
Migrations for 'AppContacts':
  AppContacts/migrations/0001_initial.py
    - Create model Contacts
```

```
DJANGO/
├── PrjContacts/
│   ├── AppContacts/
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py     # New
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   ├── PrjContacts/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │   
│   └── manage.py
│
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
│
├── README.md
└── requirements.txt
```

---

* Выполняем все необходимые миграции, создавая соответствующие таблицы в базе данных.
```sh
python manage.py migrate
```
```
Operations to perform:
  Apply all migrations: AppContacts, admin, auth, contenttypes, sessions
Running migrations:
  Applying AppContacts.0001_initial... OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

* Была создана таблица `AppContacts_contacts` для модели **Contacts** в приложении **AppContacts**, а также другие таблицы, которые необходимы для работы Django и его стандартных приложений, таких как auth, admin и т.д:
```
AppContacts_contacts
auth_group
auth_group_permissions
auth_permission
auth_user
auth_user_groups
auth_user_user_permissions
django_admin_log
django_content_type
django_migrations
django_sessions
```

* **ContactsApp_contacts** - это таблица, которую вы создали в вашем приложении ContactsApp для хранения контактов
* **auth_\*\*\*** - это таблицы, которые связаны с аутентификацией и авторизацией в Django.
* **django_admin_log** - это таблица, которая используется для журналирования действий администраторов в Django административной панели.
* **django_content_type** - это таблица, которая хранит информацию о моделях приложений Django.
* **django_migrations** - это таблица, которая используется для отслеживания миграций, которые были применены в вашем проекте.
* **django_sessions** - это таблица, которая используется для хранения информации о сессиях пользователей в Django.


## Добавить запись в базу данных

```sh
touch main.py
```
```python
from PrjContacts.AppContacts.models import Contacts

new_contact = Contacts(
    FirstName='Имя',
    LastName='Фамилия',
    City='Город',
    Email='email@example.com',
    Birthday='2000-01-01'
)
new_contact.save()
```

```sh
python main.py
```

```
DJANGO/
├── PrjContacts/
│   ├── AppContacts/
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py     # New
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   ├── PrjContacts/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │   
│   └── manage.py
│
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
│
├── README.md
└── requirements.txt
```


# Django Admin

```sh 
python manage.py runserver
```

Open URL:
http://127.0.0.1:8000/admin/

## Create new Super User
```sh 
python manage.py createsuperuser
```
```
Username (leave blank to use 'salavat'): admin
Email address: admin@demo.com
Password: ********
Password (again): ******** 
Superuser created successfully.
```

## Добавить Модель базы данных
Перейти в файл: `AppContacts/admin.py`

```python
from django.contrib import admin
from .models import Contacts

# Register your models here.
admin.site.register(Contacts)
```

будет возможность добавлять свои записи:
http://127.0.0.1:8000/admin/AppContacts/