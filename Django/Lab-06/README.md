# Django ORM - Запросы

**Оглавление:**
- [Django ORM - Запросы](#django-orm---запросы)
  - [1. Подготовка проекта](#1-подготовка-проекта)
  - [2. Использование ORM запросов](#2-использование-orm-запросов)
    - [2.1. Подготовка скрипта для запросов](#21-подготовка-скрипта-для-запросов)
    - [2.2. Insert](#22-insert)
    - [2.3. Get 5 records](#23-get-5-records)
    - [2.4. Get 5 records - brand, model, engine](#24-get-5-records---brand-model-engine)
    - [2.5. Get records with Brown or Blue colors](#25-get-records-with-brown-or-blue-colors)
    - [2.6. Get records with year and color](#26-get-records-with-year-and-color)
    - [2.7. Get records with (2019 OR 2020) AND color](#27-get-records-with-2019-or-2020-and-color)
    - [2.8. Get records where Value Contain](#28-get-records-where-value-contain)
    - [2.9. Get records where Value StartsWith](#29-get-records-where-value-startswith)
    - [2.10. Get records Combining](#210-get-records-combining)
  - [3. Q Objects:](#3-q-objects)
    - [3.1 Text, Case Sensitive](#31-text-case-sensitive)
    - [3.2. Text, Case-Insensitive](#32-text-case-insensitive)
    - [3.3. Numbers](#33-numbers)
    - [3.4. Combining queries](#34-combining-queries)
    - [3.5. Full code example](#35-full-code-example)
  - [4. F expressions](#4-f-expressions)
    - [4.1. Update Price](#41-update-price)
    - [4.2. Update Status](#42-update-status)
    - [4.3. Update Price for old cars](#43-update-price-for-old-cars)
  - [5. Method List](#5-method-list)


## 1. Подготовка проекта 


<details markdown="1"> 
<summary>1.01. Подготовить виртуальное окружение </summary>
<br>
<code>LAB-06/</code>
<pre><code>python -m venv venv            
source venv/bin/activate      
</code></pre>
</details>

<details markdown="1"> 
<summary>1.02. Добавить библиотеки в requirements.txt и установить</summary>
<br>
<code>LAB-06/</code>
<pre><code>echo django             >> requirements.txt    
echo django-extensions  >> requirements.txt   
echo psycopg2-binary    >> requirements.txt      
echo python-dotenv      >> requirements.txt    
<br>
pip install -r requirements.txt            
</code></pre>
</details>

<details markdown="1"> 
<summary>1.03. Создать проект "transport"</summary>
<br>
<code>LAB-06/</code>
<pre><code>django-admin startproject transport</code></pre>
</details>

<details markdown="1"> 
<summary>1.04. Сформируйте .env с параметрами подключения к PostgeSQL</summary>
<br>
<code>LAB-06/transport/.env:</code>
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
<code>LAB-06/transport/transport/settings.py:</code>
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
<code>LAB-06/transport/transport/settings.py:</code>
<pre><code>DATABASES = {
    'default'     - {
        'engine'     -   'django.db.backends.postgresql',
        'NAME'     -     pg_db,
        'USER'     -     pg_user,
        'PASSWORD'     - pg_psswd,
        'HOST'     -     pg_host,
        'PORT'     -     pg_port,
    }
}
</code></pre>
</details>

<details markdown="1"> 
<summary>1.07. Запустите миграцию</summary>
<br>
<code>LAB-06/transport/</code>
<pre><code>./manage.py migrate </code></pre>
</details>

<details markdown="1"> 
<summary>1.08. Зарегистрировать приложение django_extensions</summary>
<br>
<code>LAB-06/transport/transport/settings.py:</code>
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
<summary>1.09. Создать новое приложение "cars"</summary>
<br>
<code>LAB-06/transport/</code>
<pre><code>./manage.py startapp cars</code></pre>
</details>

<details markdown="1"> 
<summary>1.10. Зарегистрировать приложение "cars"</summary>
<br>
<code>LAB-06/transport/transport/settings.py:</code>
<pre><code>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'cars',                  # New
]</code></pre>
</details>

<details markdown="1"> 
<summary>1.11. Создайте модель для "cars"</summary>
<br>
<code>LAB-06/transport/cars/models.py:</code>
<pre><code>from django.db import models
<br>
class t_auto(models.model):
    id      = models.IntegerField(primary_key=True)
    brand   = models.CharField(max_length=50)
    model   = models.CharField(max_length=50)
    year    = models.IntegerField()
    color   = models.CharField(max_length=50)
    price   = models.IntegerField()
    engine  = models.CharField(max_length=50)
    vin     = models.CharField(max_length=50)
    status  = models.CharField(max_length=50, default='Available')
</code></pre>
</details>

<details markdown="1"> 
<summary>1.12. Создайте файлы миграции и запустите миграцию</summary>
<br>
<code>LAB-06/transport/</code>
<pre><code>./manage.py makemigrations cars
./manage.py migrate </code></pre>
</details>

**К этому шагу вы должны иметь:**
* Структура проекта:
```sh
LAB-06/
├── transport/
│   ├── transport/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── cars/            
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

* Таблицы в базе данных PostgreSQL:
```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
```

| table_name                   |
| ---------------------------- |
| cars_t_auto                  |
| auth_group                   |
| auth_group_permissions       |
| auth_permission              |
| auth_user                    |
| auth_user_groups             |
| auth_user_user_permissions   |
| django_admin_log             |
| django_content_type          |
| django_migrations            |
| django_session               |



## 2. Использование ORM запросов

### 2.1. Подготовка скрипта для запросов
```sh
cd transport 
cd cars 
mkdir scripts
cd scripts 
touch main.py
```

### 2.2. Insert

```python
from ..models import t_auto

def run():
    pass


car_list = [
    {'brand'     - 'Peugeot', 'model'     - '3008', 'year'     - 2019, 'color'     - 'White', 'price'     - 2000000, 'engine'     - '1.6 PureTech', 'vin'     - 'VF3RFE00V5E000000'},
    {'brand'     - 'Dodge', 'model'     - 'Ram', 'year'     - 2019, 'color'     - 'White', 'price'     - 2000000, 'engine'     - '1.6 PureTech', 'vin'     - 'VF3RFE00V5E000000'},
    {'brand'     - 'Peugeot', 'model'     - '3008', 'year'     - 2019, 'color'     - 'White', 'price'     - 2000000, 'engine'     - '1.6 PureTech', 'vin'     - 'VF3RFE00V5E000000'},
    {'brand'     - 'Renault', 'model'     - 'Arkana', 'year'     - 2019, 'color'     - 'Brown', 'price'     - 1350000, 'engine'     - '1.3 TCe', 'vin'     - 'VF1RFE00V5E000000'},
    {'brand'     - 'Audi', 'model'     - 'Q5', 'year'     - 2020, 'color'     - 'Black', 'price'     - 2500000, 'engine'     - '2.0 TFSI', 'vin'     - 'WAUZZZFYXJ1234567'},
    {'brand'     - 'BMW', 'model'     - '3 Series', 'year'     - 2021, 'color'     - 'Blue', 'price'     - 2800000, 'engine'     - '2.0 TwinPower Turbo', 'vin'     - 'WBA5R1C50M7C12345'},
    {'brand'     - 'Mercedes-Benz', 'model'     - 'GLE', 'year'     - 2022, 'color'     - 'Silver', 'price'     - 3500000, 'engine'     - '3.0L Inline-6 Turbo', 'vin'     - 'W1N0G8EB2LX123456'},
    {'brand'     - 'Toyota', 'model'     - 'Camry', 'year'     - 2021, 'color'     - 'Red', 'price'     - 1800000, 'engine'     - '2.5L Dynamic Force', 'vin'     - '4T1C11BKXLU123456'},
    {'brand'     - 'Honda', 'model'     - 'Civic', 'year'     - 2020, 'color'     - 'White', 'price'     - 1500000, 'engine'     - '1.5L Turbocharged', 'vin'     - '2HGFC1F31LH123456'},
    {'brand'     - 'Ford', 'model'     - 'Mustang', 'year'     - 2022, 'color'     - 'Yellow', 'price'     - 3200000, 'engine'     - '5.0L V8', 'vin'     - '1FA6P8CF6L1234567'},
    {'brand'     - 'Volkswagen', 'model'     - 'Passat', 'year'     - 2021, 'color'     - 'Gray', 'price'     - 1900000, 'engine'     - '2.0 TSI', 'vin'     - '1VWAA7A31LC123456'},
    {'brand'     - 'Nissan', 'model'     - 'Sentra', 'year'     - 2020, 'color'     - 'Black', 'price'     - 1400000, 'engine'     - '1.8L DOHC', 'vin'     - '3N1AB8CV5LY123456'},
    {'brand'     - 'Chevrolet', 'model'     - 'Optima', 'year'     - 2021, 'color'     - 'Silver', 'price'     - 1700000, 'engine'     - '1.6L Turbo', 'vin'     - '3GNKBKRSXJG123456'},
    {'brand'     - 'Hyundai', 'model'     - 'Elantra', 'year'     - 2022, 'color'     - 'White', 'price'     - 1600000, 'engine'     - '2.0L MPI', 'vin'     - '5NPD84LF7LH123456'},
    {'brand'     - 'Subaru', 'model'     - 'Legacy', 'year'     - 2021, 'color'     - 'Blue', 'price'     - 2000000, 'engine'     - '2.5L BOXER', 'vin'     - '4S3BWAN65M3000000'},
    {'brand'     - 'Kia', 'model'     - 'Forte', 'year'     - 2020, 'color'     - 'Red', 'price'     - 1500000, 'engine'     - '2.0L MPI', 'vin'     - '3KPF24AD0LE123456'}
]

for item in car_list:
    table = t_auto(**item)
    table.save()
```


The table:
| id | brand         | model    | year | color  | price   | engine              | vin               | status    |
| -- | ------------- | -------- | ---- | ------ | ------- | ------------------- | ----------------- | --------- |
| 1  | Dodge         | Ram      | 2019 | White  | 2000000 | 1.6 PureTech        | VF3RFE00V5E000000 | Available |
| 2  | Peugeot       | 3008     | 2019 | White  | 2000000 | 1.6 PureTech        | VF3RFE00V5E000000 | Available |
| 3  | Renault       | Arkana   | 2019 | Brown  | 1350000 | 1.3 TCe             | VF1RFE00V5E000000 | Available |
| 4  | Audi          | Q5       | 2020 | Black  | 2500000 | 2.0 TFSI            | WAUZZZFYXJ1234567 | Available |
| 5  | BMW           | 3 Series | 2021 | Blue   | 2800000 | 2.0 TwinPower Turbo | WBA5R1C50M7C12345 | Available |
| 6  | Mercedes-Benz | GLE      | 2022 | Silver | 3500000 | 3.0L Inline-6 Turbo | W1N0G8EB2LX123456 | Available |
| 7  | Toyota        | Camry    | 2021 | Red    | 1800000 | 2.5L Dynamic Force  | 4T1C11BKXLU123456 | Available |
| 8  | Honda         | Civic    | 2020 | White  | 1500000 | 1.5L Turbocharged   | 2HGFC1F31LH123456 | Available |
| 9  | Ford          | Mustang  | 2022 | Yellow | 3200000 | 5.0L V8             | 1FA6P8CF6L1234567 | Available |
| 10 | Volkswagen    | Passat   | 2021 | Gray   | 1900000 | 2.0 TSI             | 1VWAA7A31LC123456 | Available |
| 11 | Nissan        | Sentra   | 2020 | Black  | 1400000 | 1.8L DOHC           | 3N1AB8CV5LY123456 | Available |
| 12 | Chevrolet     | Optima   | 2021 | Silver | 1700000 | 1.6L Turbo          | 3GNKBKRSXJG123456 | Available |
| 13 | Hyundai       | Elantra  | 2022 | White  | 1600000 | 2.0L MPI            | 5NPD84LF7LH123456 | Available |
| 15 | Subaru        | Legacy   | 2021 | Blue   | 2000000 | 2.5L BOXER          | 4S3BWAN65M3000000 | Available |
| 16 | Kia           | Forte    | 2020 | Red    | 1500000 | 2.0L MPI            | 3KPF24AD0LE123456 | Available |


### 2.3. Get 5 records
```python
table   = t_auto.objects
records = table.filter()[:5].values()

for item in records:
    print(item)
```

Result:
```log
{'id'     - 1, 'brand'     - 'Dodge', 'model'     - 'Ram', 'year'     - 2019, 'color'     - 'White', 'price'     - 2000000, 'engine'     - '1.6 PureTech', 'vin'     - 'VF3RFE00V5E000000', 'status'     - 'Available'}
{'id'     - 2, 'brand'     - 'Peugeot', 'model'     - '3008', 'year'     - 2019, 'color'     - 'White', 'price'     - 2000000, 'engine'     - '1.6 PureTech', 'vin'     - 'VF3RFE00V5E000000', 'status'     - 'Available'}
{'id'     - 3, 'brand'     - 'Renault', 'model'     - 'Arkana', 'year'     - 2019, 'color'     - 'Brown', 'price'     - 1350000, 'engine'     - '1.3 TCe', 'vin'     - 'VF1RFE00V5E000000', 'status'     - 'Available'}
{'id'     - 4, 'brand'     - 'Audi', 'model'     - 'Q5', 'year'     - 2020, 'color'     - 'Black', 'price'     - 2500000, 'engine'     - '2.0 TFSI', 'vin'     - 'WAUZZZFYXJ1234567', 'status'     - 'Available'}
{'id'     - 5, 'brand'     - 'BMW', 'model'     - '3 Series', 'year'     - 2021, 'color'     - 'Blue', 'price'     - 2800000, 'engine'     - '2.0 TwinPower Turbo', 'vin'     - 'WBA5R1C50M7C12345', 'status'     - 'Available'}
```

### 2.4. Get 5 records - brand, model, engine
```python
table   = t_auto.objects
records = table.filter()[:5].values('brand', 'model', 'engine')

for item in records:
    print(item)
```

**Result:**
```log
{'brand'     - 'Dodge', 'model'     - 'Ram', 'engine'     - '1.6 PureTech'}
{'brand'     - 'Peugeot', 'model'     - '3008', 'engine'     - '1.6 PureTech'}
{'brand'     - 'Renault', 'model'     - 'Arkana', 'engine'     - '1.3 TCe'}
{'brand'     - 'Audi', 'model'     - 'Q5', 'engine'     - '2.0 TFSI'}
{'brand'     - 'BMW', 'model'     - '3 Series', 'engine'     - '2.0 TwinPower Turbo'}
```

### 2.5. Get records with Brown or Blue colors

```python
from cars.models import t_auto
from django.db.models import Q

table   = t_auto.objects
q_blue  = Q(color='Blue')
q_brown = Q(color='Brown')
query   = table.filter(q_blue | q_brown)
result  = query.values('brand', 'model', 'color', 'engine')

for item in result:
    print(item)
```

**Result:**
```
{'brand'     - 'Renault', 'model'     - 'Arkana', 'color'     - 'Brown', 'engine'     - '1.3 TCe'}
{'brand'     - 'BMW', 'model'     - '3 Series', 'color'     - 'Blue', 'engine'     - '2.0 TwinPower Turbo'}
{'brand'     - 'Subaru', 'model'     - 'Legacy', 'color'     - 'Blue', 'engine'     - '2.5L BOXER'}
```

```sql
SELECT 
    "cars_t_auto"."brand", 
    "cars_t_auto"."model", 
    "cars_t_auto"."color", 
    "cars_t_auto"."engine" 
FROM "cars_t_auto"
WHERE (
    "cars_t_auto"."color" = Blue OR 
    "cars_t_auto"."color" = Brown)
```


### 2.6. Get records with year and color

```python
from cars.models import t_auto
from django.db.models import Q

table   = t_auto.objects
q_year  = Q(year=2019)
q_color = Q(color='Brown')
query   = table.filter(q_year & q_color)
result  = query.values('brand', 'model', 'color', 'engine')

for item in result:
    print(item)
```

**Result:**
```
{'brand'     - 'Renault', 'model'     - 'Arkana', 'color'     - 'Brown', 'engine'     - '1.3 TCe'}
```

```sql
SELECT 
    "cars_t_auto"."brand", 
    "cars_t_auto"."model", 
    "cars_t_auto"."color", 
    "cars_t_auto"."engine" 
FROM "cars_t_auto" 
WHERE (
    "cars_t_auto"."year" = 2019 AND 
    "cars_t_auto"."color" = Brown)
```


### 2.7. Get records with (2019 OR 2020) AND color

```python
from cars.models import t_auto
from django.db.models import Q

table   = t_auto.objects

q_2019  = Q(year=2019)
q_2020  = Q(year=2020)
q_white = Q(color='White')

query   = table.filter((q_2019 | q_2020) & q_white) 
result  = query.values('brand', 'model', 'color', 'engine')

for item in result:
    print(item)
```

**Result:**
```
{'brand'     - 'Dodge', 'model'     - 'Ram', 'color'     - 'White', 'engine'     - '1.6 PureTech'}
{'brand'     - 'Peugeot', 'model'     - '3008', 'color'     - 'White', 'engine'     - '1.6 PureTech'}
{'brand'     - 'Honda', 'model'     - 'Civic', 'color'     - 'White', 'engine'     - '1.5L Turbocharged'}
```

```sql
SELECT 
    "cars_t_auto"."brand", 
    "cars_t_auto"."model", 
    "cars_t_auto"."color", 
    "cars_t_auto"."engine" 
FROM "cars_t_auto" 
WHERE (
    ("cars_t_auto"."year" = 2019 OR "cars_t_auto"."year" = 2020) 
    AND "cars_t_auto"."color" = White)
```



### 2.8. Get records where Value Contain

```python
from cars.models import t_auto
from django.db.models import Q

table    = t_auto.objects
q_engine = Q(engine__contains='2.0')
query    = table.filter(q_engine) 
result   = query.values('brand', 'model', 'color', 'engine')

for item in result:
    print(item)
```

**Result:**
```
{'brand'     - 'Audi', 'model'     - 'Q5', 'color'     - 'Black', 'engine'     - '2.0 TFSI'}
{'brand'     - 'BMW', 'model'     - '3 Series', 'color'     - 'Blue', 'engine'     - '2.0 TwinPower Turbo'}
{'brand'     - 'Volkswagen', 'model'     - 'Passat', 'color'     - 'Gray', 'engine'     - '2.0 TSI'}
{'brand'     - 'Hyundai', 'model'     - 'Elantra', 'color'     - 'White', 'engine'     - '2.0L MPI'}
{'brand'     - 'Kia', 'model'     - 'Forte', 'color'     - 'Red', 'engine'     - '2.0L MPI'}
```

```sql
SELECT 
    "cars_t_auto"."brand", 
    "cars_t_auto"."model", 
    "cars_t_auto"."color", 
    "cars_t_auto"."engine" 
FROM "cars_t_auto" 
WHERE "cars_t_auto"."engine"::text LIKE %2.0%
```


### 2.9. Get records where Value StartsWith 

```python
from cars.models import t_auto
from django.db.models import Q

table    = t_auto.objects
q_vin    = Q(vin__startswith='3')
query    = table.filter(q_vin) 
result   = query.values('brand', 'model', 'color', 'vin')


for item in result:
    print(item)
```

**Result:**
```
{'brand'     - 'Nissan', 'model'     - 'Sentra', 'color'     - 'Black', 'vin'     - '3N1AB8CV5LY123456'}
{'brand'     - 'Chevrolet', 'model'     - 'Optima', 'color'     - 'Silver', 'vin'     - '3GNKBKRSXJG123456'}
{'brand'     - 'Chevrolet', 'model'     - 'Optima', 'color'     - 'Silver', 'vin'     - '3GNKBKRSXJG123456'}
{'brand'     - 'Kia', 'model'     - 'Forte', 'color'     - 'Red', 'vin'     - '3KPF24AD0LE123456'}
```

```sql
SELECT 
    "cars_t_auto"."brand", 
    "cars_t_auto"."model", 
    "cars_t_auto"."color", 
    "cars_t_auto"."vin" 
FROM "cars_t_auto" 
WHERE "cars_t_auto"."vin"::text LIKE 3%
```


### 2.10. Get records Combining

```python
from cars.models import t_auto
from django.db.models import Q

table    = t_auto.objects
q_price    = Q(price__gt=1300000) | Q(price__lt=2000000)
q_year     = Q(year=2021)
query    = table.filter(q_price & q_year) 
result   = query.values('brand', 'model', 'color', 'price')


for item in result:
    print(item)
```

**Result:**
```
{'brand'     - 'BMW', 'model'     - '3 Series', 'color'     - 'Blue', 'price'     - 2800000}
{'brand'     - 'Toyota', 'model'     - 'Camry', 'color'     - 'Red', 'price'     - 1800000}
{'brand'     - 'Volkswagen', 'model'     - 'Passat', 'color'     - 'Gray', 'price'     - 1900000}
{'brand'     - 'Chevrolet', 'model'     - 'Optima', 'color'     - 'Silver', 'price'     - 1700000}
{'brand'     - 'Chevrolet', 'model'     - 'Optima', 'color'     - 'Silver', 'price'     - 1700000}
{'brand'     - 'Subaru', 'model'     - 'Legacy', 'color'     - 'Blue', 'price'     - 2000000}
```

```sql
SELECT
    "cars_t_auto"."brand", 
    "cars_t_auto"."model", 
    "cars_t_auto"."color", 
    "cars_t_auto"."price" 
FROM "cars_t_auto" 
WHERE (
    ("cars_t_auto"."price" > 1300000 OR "cars_t_auto"."price" < 2000000) 
    AND "cars_t_auto"."year" = 2021)
```


## 3. Q Objects:

| brand         | model    | year | color  |
| ------------- | -------- | ---- | ------ |
| Dodge         | Ram      | 2019 | White  |
| Peugeot       | 3008     | 2019 | White  |
| Renault       | Arkana   | 2019 | Brown  |
| Audi          | Q5       | 2020 | Black  |
| BMW           | 3 Series | 2021 | Blue   |
| Mercedes-Benz | GLE      | 2022 | Silver |
| Toyota        | Camry    | 2021 | Red    |
| Honda         | Civic    | 2020 | White  |
| Ford          | Mustang  | 2022 | Yellow |
| Volkswagen    | Passat   | 2021 | Gray   |
| Nissan        | Sentra   | 2020 | Black  |
| Chevrolet     | Optima   | 2021 | Silver |
| Hyundai       | Elantra  | 2022 | White  |
| Subaru        | Legacy   | 2021 | Blue   |
| Kia           | Forte    | 2020 | Red    |

### 3.1 Text, Case Sensitive 

```python
q_color = Q(color='Black')              # Case Sensitive & Exact     -       Black
q_color = Q(color__exact='Black')       # Case Sensitive & Exact     -       Black
q_color = Q(color__contains='W')        # Case Sensitive     -               White
q_color = Q(color__startswith='Bl')     # Case Sensitive & Starts With     - Black, Blue 
q_color = Q(color__endswith='e')        # Case Sensitive & Ends With     -   White, Blue 
q_color = Q(color__regex=r'^(Wh|Bl)')   # Case Sensitive & Regex     -       White, Blue, Black
```

### 3.2. Text, Case-Insensitive

```python
q_color = Q(color__iexact='white')      # Case Insensitive & Exact     -         white, White, WHITE
q_color = Q(color__icontains='w')       # Case Insensitive     -                 aws, AWS, brown, BROWN, white, White 
q_color = Q(color__istartswith='w')     # Case Insensitive & Starts With     -   white, White
q_color = Q(color__iendswith='e')       # Case Insensitive & Ends With     -     white, WHITE, e, E
q_color = Q(color__iregex=r'^(Wh|Bl)')  # Case Insensitive & Regex     -         white, WHTIE, Blue, BLUE, Black, BLACK
```

### 3.3. Numbers

```python
q_year  = Q(year=2019)                  # Exact     -                    Matches years exactly equal to 2019
q_year  = Q(year__exact=2019)           # Exact     -                    Matches years exactly equal to 2019

q_year  = Q(year__gt=2019)              # Greater Than     -             Matches years greater than 2019
q_year  = Q(year__gte=2019)             # Greater Than or Equal     -    Matches years greater than or equal to 2019

q_year  = Q(year__lt=2020)              # Less Than     -                Matches years less than 2020
q_year  = Q(year__lte=2020)             # Less Than or Equal     -       Matches years less than or equal to 2020

q_year  = Q(year__range=(2019, 2021))   # Range     -                    Matches years within the range 2019-2021
q_year  = Q(year__in=[2019, 2020, 2021])# In     -                       Matches years that are in the list [2019, 2020, 2021]

q_year  = Q(year__isnull=True)          # Is Null     -                  Matches records where the year is null
q_year  = Q(year__isnull=False)         # Is Not Null     -              Matches records where the year is not null
```

### 3.4. Combining queries

```python
q_year  = Q(year=2019) | Q(year=2020)           # OR     -   Matches years that are either 2019 or 2020
q_color = Q(color='White') | Q(color='Black')   # OR     -   Matches colors that are either 'White' or 'Black'

q_query = Q(color='White') & Q(year=2019)       # AND     -  Matches records where the color is 'White' and the year is 2019

q_query = ~Q(color='White')                     # NOT     -  Matches records where the color is not 'White'
q_query = ~Q(color='White') & Q(year=2019)      # NOT AND     - Matches records where
```

### 3.5. Full code example

```sh
./manage.py runscript main
```

```python
from cars.models import t_auto
from django.db.models import Q

def run():
    pass

table    = t_auto.objects
q_color  = Q(color='Brown') | Q(color='Yellow')
query    = table.filter(q_color)
result   = query.values('brand', 'model', 'color', 'year')

for item in result:
    print(item)
```

**Result:**
```
{'brand'     - 'Renault', 'model'     - 'Arkana', 'color'     - 'Brown', 'year'     - 2019}
{'brand'     - 'Ford', 'model'     - 'Mustang', 'color'     - 'Yellow', 'year'     - 2022}
```

```sql
SELECT 
    "cars_t_auto"."brand", 
    "cars_t_auto"."model", 
    "cars_t_auto"."color", 
    "cars_t_auto"."year" 
FROM "cars_t_auto" 
WHERE (
    "cars_t_auto"."color" = Brown OR 
    "cars_t_auto"."color" = Yellow)
```


## 4. F expressions
| brand         | model    | year | color  | price   | engine              | status    |
| ------------- | -------- | ---- | ------ | ------- | ------------------- | --------- |
| Peugeot       | 3008     | 2019 | White  | 2000000 | 1.6 PureTech        | Available |
| Dodge         | Ram      | 2019 | White  | 2000000 | 1.6 PureTech        | Available |
| Peugeot       | 3008     | 2019 | White  | 2000000 | 1.6 PureTech        | Available |
| Renault       | Arkana   | 2019 | Brown  | 1350000 | 1.3 TCe             | Available |
| Audi          | Q5       | 2020 | Black  | 2500000 | 2.0 TFSI            | Available |
| BMW           | 3 Series | 2021 | Blue   | 2800000 | 2.0 TwinPower Turbo | Available |
| Mercedes-Benz | GLE      | 2022 | Silver | 3500000 | 3.0L Inline-6 Turbo | Available |
| Toyota        | Camry    | 2021 | Red    | 1800000 | 2.5L Dynamic Force  | Available |
| Honda         | Civic    | 2020 | White  | 1500000 | 1.5L Turbocharged   | Available |
| Ford          | Mustang  | 2022 | Yellow | 3200000 | 5.0L V8             | Available |
| Volkswagen    | Passat   | 2021 | Gray   | 1900000 | 2.0 TSI             | Available |
| Nissan        | Sentra   | 2020 | Black  | 1400000 | 1.8L DOHC           | Available |
| Chevrolet     | Optima   | 2021 | Silver | 1700000 | 1.6L Turbo          | Available |
| Hyundai       | Elantra  | 2022 | White  | 1600000 | 2.0L MPI            | Available |
| Subaru        | Legacy   | 2021 | Blue   | 2000000 | 2.5L BOXER          | Available |
| Kia           | Forte    | 2020 | Red    | 1500000 | 2.0L MPI            | Available |


### 4.1. Update Price
```python
from ..models import t_auto
from django.db.models import F

def run():
    pass

table   = t_auto.objects
f_price = F('price')*0.95             # 5% discount  
table.filter(brand='Toyota').update(price=f_price)
```

| brand  | model | year | color | price   | engine             | status |
| ------ | ----- | ---- | ----- | ------- | ------------------ | ------ |
| Toyota | Camry | 2021 | Red   | 1710000 | 2.5L Dynamic Force | False  |



### 4.2. Update Status
```python
from ..models import t_auto
from django.db.models import F

def run():
    pass


table = t_auto.objects
table.filter(price__gt=2000000).update(status='Expensive')
```

| brand         | model    | year | color  | price   | engine              | status    |
| ------------- | -------- | ---- | ------ | ------- | ------------------- | --------- |
| Audi          | Q5       | 2020 | Black  | 2500000 | 2.0 TFSI            | Expensive |
| BMW           | 3 Series | 2021 | Blue   | 2800000 | 2.0 TwinPower Turbo | Expensive |
| Mercedes-Benz | GLE      | 2022 | Silver | 3500000 | 3.0L Inline-6 Turbo | Expensive |
| Ford          | Mustang  | 2022 | Yellow | 3200000 | 5.0L V8             | Expensive |

### 4.3. Update Price for old cars

```python
from ..models import t_auto
from django.db.models import F, Q

def run():
    pass

table   = t_auto.objects
q_year  = Q(year=2019)
f_price = F('price')*0.85
update  = table.filter(q_year).update(price=f_price)

# t_auto.objects.filter(Q(year=2019)).update(price=F('price')*0.85)
```

| brand   | model  | year | color | price   | engine       | status    |
| ------- | ------ | ---- | ----- | ------- | ------------ | --------- |
| Peugeot | 3008   | 2019 | White | 1700000 | 1.6 PureTech | Available |
| Dodge   | Ram    | 2019 | White | 1700000 | 1.6 PureTech | Available |
| Peugeot | 3008   | 2019 | White | 1700000 | 1.6 PureTech | Available |
| Renault | Arkana | 2019 | Brown | 1147500 | 1.3 TCe      | Available |

## 5. Method List

```python
from ..models import t_auto     

def run():
    pass

table   = t_auto.objects
table.<methods>
```
```
aggregate   - Performs an aggregation query on the queryset, computing aggregate values.
bulk_create - Creates multiple model instances in the database with fewer queries.
bulk_update - Updates multiple model instances in the database with fewer queries.
contains    - Filters the queryset to match objects that contain a specified value.
count       - Returns the number of objects in the queryset.
create      - Creates a new model instance and saves it to the database.
earliest    - Returns the earliest object according to a specified field.
exists      - Returns True if any object exists in the queryset.
explain     - Displays the SQL explanation of the queryset's query.
first       - Returns the first object in the queryset, according to the default ordering.
get         - Retrieves a single object that matches the given criteria, or raises an exception if not found.
get_or_create   - Retrieves an object that matches the given criteria, or creates a new one if not found.
in_bulk     - Retrieves a dictionary mapping primary keys to objects for a given list of primary keys.
iterator    - Returns an iterator that fetches objects from the database in chunks, rather than all at once.
last        - Returns the last object in the queryset, according to the default ordering.
latest      - Returns the latest object according to a specified field.
all         - Returns a new queryset that is a copy of the current queryset.
annotate    - Adds annotations to the queryset by performing database-level operations.
update      - Updates one or more fields of the objects in the queryset in the database.
update_or_create    - Updates an object if it exists in the database, or creates a new one if not.
values      - Returns a QuerySet that returns dictionaries instead of model instances.
values_list - Returns a QuerySet that returns tuples instead of model instances.
```
