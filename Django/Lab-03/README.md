# Подключение PostgreSQL

**Оглавление:**
- [Подключение PostgreSQL](#подключение-postgresql)
  - [1. Самостоятельная подготовка:](#1-самостоятельная-подготовка)
  - [2.](#2)
  - [3.](#3)


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
 

## 2. 

## 3. 

