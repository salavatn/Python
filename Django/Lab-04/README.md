#  Расширенный инструмент для Django

**Оглавление:**
- [Расширенный инструмент для Django](#расширенный-инструмент-для-django)
  - [1. Самостоятельная подготовка:](#1-самостоятельная-подготовка)
  - [2. Django Extentions](#2-django-extentions)
    - [2.1. Библиотека django-extensions](#21-библиотека-django-extensions)
    - [2.2. Зарегистрировать django-extensions](#22-зарегистрировать-django-extensions)
  - [3. Использование runscript](#3-использование-runscript)
    - [3.1. Каталог scripts](#31-каталог-scripts)
    - [3.2. Запуск скрипта:](#32-запуск-скрипта)
    - [3.3. Запуск с аргументами:](#33-запуск-с-аргументами)


## 1. Самостоятельная подготовка:
1. Создайте Django проект `Books`
         
2. У вас должна получиться следующая структура проекта:

```sh
LAB-04/
├── Books/   
│   ├── Books/        
│   │   ├── __init__.py 
│   │   ├── asgi.py       
│   │   ├── settings.py   
│   │   ├── urls.py       
│   │   └── wsgi.py     
│   │   
│   └── manage.py         
│
├── venv/
├── README.md
└── requirements.txt
```
 

## 2. Django Extentions

> `Django-extensions` - это сторонний пакет для Django, который содержит набор полезных инструментов для разработчиков, таких как команды для отладки и тестирования, утилиты для генерации кода и многое другое.

### 2.1. Библиотека django-extensions

* Установите библиотеку `django-extensions`

```sh
echo django-extensions >> requirements.txt 
pip install -r requirements.txt
pip list
```
```
Package    Version
---------- -------
asgiref    3.6.0
Django     4.2.1
pip        23.1.2
setuptools 65.5.0
sqlparse   0.4.4
```

### 2.2. Зарегистрировать django-extensions
* Добавить `django-extensions` в список установленных приложений в файле `Lab-04/Books/Books/settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'django_extensions',
]
```
```sh
./manage.py help 
```

```sh
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    ...
    testserver

[django_extensions]
    admin_generator # генерирует шаблоны админки Django на основе моделей
    clean_pyc # удаляет скомпилированные файлы Python (.pyc)
    clear_cache # очищает кэш Django
    compile_pyc # компилирует все файлы Python в байт-код (.pyc)
    create_command # создает новую Django-команду
    create_jobs # создает одну или несколько работ из очереди задач Celery
    create_template_tags # создает файл тегов шаблонов Django
    delete_squashed_migrations # удаляет слитые миграции Django
    describe_form # выводит описание формы Django
    drop_test_database # удаляет тестовую базу данных
    dumpscript # выводит содержимое базы данных в виде скрипта SQL
    export_emails # экспортирует адреса электронной почты из пользовательской модели Django в CSV-файл
    find_template # ищет и выводит информацию о шаблоне Django
    generate_password # генерирует случайный пароль
    generate_secret_key # генерирует новый секретный ключ Django
    graph_models # создает изображение графа моделей Django
    list_model_info # выводит информацию о моделях Django
    list_signals # выводит информацию о сигналах Django
    mail_debug # запускает SMTP-сервер для отладки электронной почты
    merge_model_instances # объединяет экземпляры модели Django
    notes # выводит заметки для моделей Django
    pipchecker # проверяет доступность обновлений Python-пакетов, используемых в Django-проекте
    print_settings # выводит настройки Django-проекта
    print_user_for_session # выводит пользователя для указанной сессии Django
    raise_test_exception # вызывает исключение для тестирования механизма обработки ошибок
    reset_db # сбрасывает базу данных Django
    reset_schema # сбрасывает схему базы данных Django
    runjob # запускает отдельную работу в Celery
    runjobs # запускает все работы в Celery
    runprofileserver # запускает сервер Django с профилированием

    runscript # запускает пользовательский скрипт Django
    
    runserver_plus # запускает сервер разработки Django с дополнительными функциями
    set_default_site # устанавливает сайт по умолчанию Django
    set_fake_passwords # устанавливает фейковые пароли для тестирования.
    shell_plus # запускает интерактивную оболочку Django с загрузкой моделей и других утилит.
    show_template_tags # выводит список всех тегов шаблонов, доступных в проекте.
    show_urls # выводит список всех URL-адресов, доступных в проекте.
    sqlcreate # создает файл SQL, который создает все таблицы в базе данных, используемой в проекте.
    sqldiff # создает файл SQL, который содержит изменения в базе данных, которые должны быть применены.
    sqldsn # создает строку подключения к базе данных на основе настроек проекта.
    sync_s3 # копирует статические файлы на Amazon S3.
    syncdata # копирует данные между базами данных, используемыми в проекте.
    unreferenced_files # находит файлы в проекте, которые больше не используются.
    update_permissions # обновляет права доступа на все модели в проекте.
    validate_templates # проверяет шаблоны проекта на ошибки.



[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```


## 3. Использование runscript

### 3.1. Каталог scripts
* Создать каталог `Lab-04/Books/scripts` в корневой директории проекта.
```sh
mkdir scripts
ls -la
```
```log
total 8
drwxr-xr-x@ 5 salavat  staff  160 May  4 22:35 .
drwxr-xr-x@ 7 salavat  staff  224 May  4 22:26 ..
drwxr-xr-x@ 8 salavat  staff  256 May  4 22:29 Books
-rwxr-xr-x@ 1 salavat  staff  661 May  4 22:26 manage.py
drwxr-xr-x@ 2 salavat  staff   64 May  4 22:35 scripts
```

* Создайте файл `Lab-04/Books/scripts/main.py` со скриптом и функцией `run()` внутри каталога scripts:

```python
def run():
  print('Hello, World! From Django Project')
``` 

### 3.2. Запуск скрипта:

1. Обычный запуск:
```sh
./manage.py runscript main
```
```
Hello, World! From Django Project
```

2. Запуск с отладкой:
```sh
./manage.py runscript main -v2
```
```
Check for django.contrib.admin.scripts.main
Check for django.contrib.auth.scripts.main
Check for django.contrib.contenttypes.scripts.main
Check for django.contrib.sessions.scripts.main
Check for django.contrib.messages.scripts.main
Check for django.contrib.staticfiles.scripts.main
Check for django_extensions.scripts.main
Check for scripts.main
Found script 'scripts.main' ...
Running script 'scripts.main' ...
Hello, World! From Django Project
```

### 3.3. Запуск с аргументами:
1. Скорректировать main.py
```python
def run(*arguments):
    data = arguments
    for item in data:
        print(item)
```

2. Запуск с аргументами:
```sh
./manage.py runscript main --script-args One Two IPaddress Mark Port
```
```
One
Two
IPaddress
Mark
Port
```
