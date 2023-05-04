# Создание Django Проекта

**Оглавление:**
- [Создание Django Проекта](#создание-django-проекта)
  - [1. Создание проекта](#1-создание-проекта)
    - [1.1. Подготовка виртуального окружения](#11-подготовка-виртуального-окружения)
    - [1.2. Знакомство с django-admin](#12-знакомство-с-django-admin)
    - [1.3. Создание нового проекта](#13-создание-нового-проекта)
  - [2. Создать миграции](#2-создать-миграции)
    - [2.1. Миграция](#21-миграция)


## 1. Создание проекта 
 
### 1.1. Подготовка виртуального окружения

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
* **requirements.txt** - Файл, содержащий список всех зависимостей проекта.

```python
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


### 1.2. Знакомство с django-admin

* **django-admin** - это утилита командной строки, предоставляемая Django, которая позволяет выполнять различные задачи, такие как:
  - создание приложений,
  - миграция базы данных, 
  - управление пользователями и группами 
  - и многое другое.

```sh
django-admin --help
```
```
Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check            - Проверка проекта на ошибки.
    compilemessages  - Компиляция файлов перевода (.po) в двоичный формат (.mo).
    createcachetable - Создание таблицы для кэширования.
    dbshell          - Вход в интерактивный интерфейс CLI для работы с DB.
    diffsettings     - Вывод различий между настройками проекта и значениями по умолчанию.
    dumpdata         - Экспорт данных из базы данных в файл в формате JSON или XML.
    flush            - Очистка содержимого базы данных.
    inspectdb        - Создание моделей на основе существующей базы данных.
    loaddata         - Импорт данных из файла в формате JSON или XML в базу данных.
    makemessages     - Создание файлов перевода (.po) на основе строк в коде.
    makemigrations   - Создание файла миграции на основе изменений в моделях.
    migrate          - Применение миграций к базе данных.
    optimizemigration - Оптимизация файлов миграции.
    runserver        - Запуск веб-сервера.
    sendtestemail    - Отправка тестового письма на заданный адрес электронной почты.
    shell            - Запуск интерактивной оболочки Django.
    showmigrations   - Вывод списка миграций и их статусов.
    sqlflush         - Вывод SQL-запросов для очистки содержимого базы данных.
    sqlmigrate       - Вывод SQL-запросов для миграции базы данных на определенную миграцию.
    sqlsequencereset - Вывод SQL-запросов для сброса последовательностей базы данных.
    squashmigrations - Слияние нескольких миграций в одну.
    startapp         - Создание нового Django-приложения.
    startproject     - Создание нового Django-проекта.
    test             - Запуск тестов для проекта.
    testserver       - Запуск веб-сервера с тестовыми данными.
```

* Команда выводит версию Django:
```sh
django-admin --version
```
```
4.2
```


### 1.3. Создание нового проекта

* Создаем новый Django-проект с именем **PrjContacts** (*Проект Контакты*). Django-проект - это набор настроек и приложений, необходимых для создания веб-приложения. Команда `startproject` создает структуру каталогов проекта и набор файлов конфигурации Django, таких как `settings.py`, `urls.py` и `wsgi.py`.

```sh
django-admin startproject PrjContacts
```

* В результате выполнения команды структура каталогов должна выглядеть примерно так:

```python
DJANGO/
├── PrjContacts/          # New: Корневой каталог
│   ├── PrjContacts/      # New: Подкаталог содержит
│   │   ├── __init__.py   # New: Определяем каталог как Python пакет
│   │   ├── asgi.py       # New: Asynchronous Server Gateway Interface
│   │   ├── settings.py   # New: Файл настроек Django-проекта
│   │   ├── urls.py       # New: Файл маршрутизации URL-адресов
│   │   └── wsgi.py       # New: Web Server Gateway Interface
│   │   
│   └── manage.py         # New: файл управления проектом Django
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

---

**Notes:**
1. После создания проекта, мы вместо **django-admin <subcommands>** будем использовать **python manage.py <subcommands>**
   - `django-admin <subcommands>` 
   - `python manage.py <subcommands>`
2. Так как в файле **manage.py** присутствует строка `#!/usr/bin/env python` -- это позволяет запускать скрипт без указания **python**:
   - `python manage.py <subcommands>`
   - `./manage.py <subcommands>`

--- 

```sh
./manage.py --help
```
```
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]          # содержит подкоманды, связанные с аутентификацией, 
  ...           # такие как "changepassword" и "createsuperuser".

[contenttypes]  # содержит подкоманду "remove_stale_contenttypes", 
  ...           # которая удаляет старые типы содержимого.

[django]        # содержит множество подкоманд, связанных с управлением проектом Django, 
  ...           # таких как makemigrations, migrate, test и т.д.

[sessions]      # содержит подкоманду "clearsessions", 
  ...           # которая очищает сессии в базе данных.

[staticfiles]   # содержит подкоманды, связанные со статическими файлами, 
  ...           # такие как "collectstatic", "findstatic" и "runserver".

```



## 2. Создать миграции

### 2.1. Миграция
* Выполняем все необходимые миграции, создавая соответствующие таблицы в базе данных.
```sh
./manage.py migrate
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

> Была создана таблица `AppContacts_contacts` для модели **Contacts** в приложении **AppContacts**, а также другие таблицы, которые необходимы для работы Django и его стандартных приложений, таких как auth, admin и т.д:
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

* **ContactsApp_contacts** - это таблица, которую мы создали в нашем приложении **ContactsApp** для хранения контактов
* **auth_\*\*\*** - это таблицы, которые связаны с аутентификацией и авторизацией в Django.
* **django_admin_log** - это таблица, которая используется для журналирования действий администраторов в Django административной панели.
* **django_content_type** - это таблица, которая хранит информацию о моделях приложений Django.
* **django_migrations** - это таблица, которая используется для отслеживания миграций, которые были применены в вашем проекте.
* **django_sessions** - это таблица, которая используется для хранения информации о сессиях пользователей в Django.