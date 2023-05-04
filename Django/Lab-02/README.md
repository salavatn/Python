# Подключение PostgreSQL

**Оглавление:**
- [Подключение PostgreSQL](#подключение-postgresql)
  - [1. Самостоятельная подготовка:](#1-самостоятельная-подготовка)
  - [2. Библиотека psycopg](#2-библиотека-psycopg)
  - [2. Настройки подключения к PostgreSQL](#2-настройки-подключения-к-postgresql)
  - [3. Переменные окружения](#3-переменные-окружения)
    - [3.1. Сформировать .env](#31-сформировать-env)
    - [3.2. Библиотека dotenv](#32-библиотека-dotenv)
  - [4. Настройка подключения к PostgreSQL](#4-настройка-подключения-к-postgresql)
    - [4.1. Параметры из .env](#41-параметры-из-env)
    - [4.2. Настройки подключения](#42-настройки-подключения)
  - [5. Запуск миграции](#5-запуск-миграции)


## 1. Самостоятельная подготовка:
1. Создайте виртуальное окружение (`venv`)
2. Установите библиотеку `django`
3. Создайте Django проект `CarDealer`
4. У вас должна получиться следующая структура проекта:

```sh
LAB-02/
├── CarDealer/            # New: Корневой каталог
│   ├── CarDealer/        # New: Подкаталог содержит
│   │   ├── __init__.py   # New: Определяем каталог как Python пакет
│   │   ├── asgi.py       # 
│   │   ├── settings.py   # Файл настроек Django-проекта
│   │   ├── urls.py       #
│   │   └── wsgi.py       #
│   │   
│   └── manage.py         # Файл управления проектом Django
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
```sh
pip list
```
```log
Package    Version
---------- -------
asgiref    3.6.0
Django     4.2.1
pip        23.1.2
setuptools 65.5.0
sqlparse   0.4.4
```
 

## 2. Библиотека psycopg

* Добавляем строку `psycopg2-binary` в файл "requirements.txt", эта библиотека для работы с PostgreSQL.
* Устанавливаем все зависимости, перечисленные в файле "requirements.txt". 

```sh 
echo psycopg2-binary >> requirements.txt

pip install -r requirements.txt
pip list
```
```
Package         Version
--------------- -------
asgiref         3.6.0
Django          4.2.1
pip             23.1.2
psycopg2-binary 2.9.6
setuptools      65.5.0
sqlparse        0.4.4
```


## 2. Настройки подключения к PostgreSQL



Для подключения к базе данных -- в проекте необходимо выполнить следующие шаги:

## 3. Переменные окружения

### 3.1. Сформировать .env

> *Файл `.env` является файлом конфигурации и содержит переменные окружения. Будет использоваться для хранения конфиденциальных данных и параметров конфигурации, которые не должны храниться в открытом доступе в коде приложения, например, пароли, ключи API, `настройки базы данных` и т.д.*

* Создать и отредактировать файл `Lab-02/CarDealer/.env`, указав параметры подключения к базе данных:
```js
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=Pa$$word
```
> Нет под рукой базы данных **PostgreSQL**? <br>
> Используй облачный сервис на [Supabase](https://supabase.com/).


* Здесь указаны следующие параметры подключения к базе данных:
  * **POSTGRES_HOST** - IP-адрес хоста, на котором находится база данных;
  * **POSTGRES_PORT** - порт, на котором запущен сервер базы данных;
  * **POSTGRES_DB** - имя базы данных;
  * **POSTGRES_USER** - имя пользователя базы данных;
  * **POSTGRES_PASSWORD** - пароль пользователя базы данных.


```sh
LAB-02/
├── CarDealer/
│   ├── CarDealer/
│   ├── .env        #<----│ New: Файл конфигурации переменных окружения
│   └── manage.py
│
├── venv/
├── README.md
└── requirements.txt
```

### 3.2. Библиотека dotenv

> *Библиотека `python-dotenv` позволяет загрузить переменные окружения из файла `.env` и использовать их в настройках приложения.*

* Добавить библиотеку `python-dotenv` в файл `LAB-02/requirements.txt`

```sh
pip install -r requirements.txt
pip list
```
```
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




## 4. Настройка подключения к PostgreSQL

### 4.1. Параметры из .env
1. Открыть файл `CarDealer/CarDealer/settings.py` и добавить следующий код в начало файла:

```python
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')
pg_host  = os.getenv('POSTGRES_HOST')
pg_port  = os.getenv('POSTGRES_PORT')
pg_db    = os.getenv('POSTGRES_DB')
pg_user  = os.getenv('POSTGRES_USER')
pg_psswd = os.getenv('POSTGRES_PASSWORD')
```

> Этот код загрузит переменные окружения из файла **.env** и присвоит их значения соответствующим переменным:
> - `pg_host`
> - `pg_port`
> - `pg_db`
> - `pg_user`
> - `pg_psswd`


### 4.2. Настройки подключения
Добавить настройки подключения к базе данных в файл `CarDealer/CarDealer/settings.py`:
   * Найдите блок настроек базы данных `DATABASES`.
   * Замените настройки базы данных в блоке **DATABASES** на следующий код:

```python
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

```
   * Сохраните изменения в файле `settings.py`. 
   * Теперь проект Django будет использовать базу данных `PostgreSQL` с указанными параметрами.


## 5. Запуск миграции
```sh
./manage.py migrate 
```

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
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

> Команда `./manage.py migrate` используется для применения миграций, созданных для приложения. Когда эта команда выполняется, **Django** применяет все еще не примененные миграции для указанных приложений и обновляет базу данных в соответствии с новой структурой данных, которая описывается в миграциях. Кроме того, команда migrate также создает таблицу django_migrations, которая хранит информацию о том, какие миграции были применены в базу данных.

* Сформированная таблица:

| table_name                 |
| -------------------------- |
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
