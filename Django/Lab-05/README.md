# Django ORM - Запросы

**Оглавление:**
- [Django ORM - Запросы](#django-orm---запросы)
  - [1. Подготовка проекта](#1-подготовка-проекта)
  - [2. Использование ORM запросов](#2-использование-orm-запросов)
    - [2.1. Подготовка скрипта для запросов](#21-подготовка-скрипта-для-запросов)
    - [2.2. Insert](#22-insert)
    - [2.3. Get 5 records](#23-get-5-records)
    - [2.4. Get 5 records - Brand, Model, Engine](#24-get-5-records---brand-model-engine)
    - [2.5. Get records with Brown or Blue colors](#25-get-records-with-brown-or-blue-colors)
    - [2.6. Get records with Year and Color](#26-get-records-with-year-and-color)
    - [2.7. Get records with (2019 OR 2020) AND Color](#27-get-records-with-2019-or-2020-and-color)
    - [2.8. Get records where Value Contain](#28-get-records-where-value-contain)
    - [2.9. Get records where Value StartsWith](#29-get-records-where-value-startswith)
    - [2.10. Get records Combining](#210-get-records-combining)
  - [3. Q Objects:](#3-q-objects)
    - [3.1 Text, Case Sensitive](#31-text-case-sensitive)
    - [3.2. Text, Case-Insensitive](#32-text-case-insensitive)
    - [3.3. Numbers](#33-numbers)
    - [3.4. Combining queries](#34-combining-queries)
    - [3.5. Full code example](#35-full-code-example)


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
    id      = models.IntegerField(primary_key=True)
    Brand   = models.CharField(max_length=50)
    Model   = models.CharField(max_length=50)
    Year    = models.IntegerField()
    Color   = models.CharField(max_length=50)
    Price   = models.IntegerField()
    Engine  = models.CharField(max_length=50)
    VIN     = models.CharField(max_length=50)
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
* Структура проекта:
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

* Таблицы в базе данных PostgreSQL:
```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
```

| table_name                   |
| ---------------------------- |
| Automobiles_tableautomobiles |
| Students_tablestudents       |
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

The table:
| id | Brand         | Model    | Year | Color  | Price   | Engine              | VIN               | Status    |
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
| 13 | Chevrolet     | Optima   | 2021 | Silver | 1700000 | 1.6L Turbo          | 3GNKBKRSXJG123456 | Available |
| 14 | Hyundai       | Elantra  | 2022 | White  | 1600000 | 2.0L MPI            | 5NPD84LF7LH123456 | Available |
| 15 | Subaru        | Legacy   | 2021 | Blue   | 2000000 | 2.5L BOXER          | 4S3BWAN65M3000000 | Available |
| 16 | Kia           | Forte    | 2020 | Red    | 1500000 | 2.0L MPI            | 3KPF24AD0LE123456 | Available |

### 2.1. Подготовка скрипта для запросов
```sh
cd FranceCars 
cd Automobiles 
mkdir scripts
cd scripts 
touch main.py
```

### 2.2. Insert

```python
car_list = [
    {'Brand': 'Peugeot', 'Model': '3008', 'Year': 2019, 'Color': 'White', 'Price': 2000000, 'Engine': '1.6 PureTech', 'VIN': 'VF3RFE00V5E000000'},
    {'Brand': 'Dodge', 'Model': 'Ram', 'Year': 2019, 'Color': 'White', 'Price': 2000000, 'Engine': '1.6 PureTech', 'VIN': 'VF3RFE00V5E000000'},
    {'Brand': 'Peugeot', 'Model': '3008', 'Year': 2019, 'Color': 'White', 'Price': 2000000, 'Engine': '1.6 PureTech', 'VIN': 'VF3RFE00V5E000000'},
    {'Brand': 'Renault', 'Model': 'Arkana', 'Year': 2019, 'Color': 'Brown', 'Price': 1350000, 'Engine': '1.3 TCe', 'VIN': 'VF1RFE00V5E000000'},
    {'Brand': 'Audi', 'Model': 'Q5', 'Year': 2020, 'Color': 'Black', 'Price': 2500000, 'Engine': '2.0 TFSI', 'VIN': 'WAUZZZFYXJ1234567'},
    {'Brand': 'BMW', 'Model': '3 Series', 'Year': 2021, 'Color': 'Blue', 'Price': 2800000, 'Engine': '2.0 TwinPower Turbo', 'VIN': 'WBA5R1C50M7C12345'},
    {'Brand': 'Mercedes-Benz', 'Model': 'GLE', 'Year': 2022, 'Color': 'Silver', 'Price': 3500000, 'Engine': '3.0L Inline-6 Turbo', 'VIN': 'W1N0G8EB2LX123456'},
    {'Brand': 'Toyota', 'Model': 'Camry', 'Year': 2021, 'Color': 'Red', 'Price': 1800000, 'Engine': '2.5L Dynamic Force', 'VIN': '4T1C11BKXLU123456'},
    {'Brand': 'Honda', 'Model': 'Civic', 'Year': 2020, 'Color': 'White', 'Price': 1500000, 'Engine': '1.5L Turbocharged', 'VIN': '2HGFC1F31LH123456'},
    {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 2022, 'Color': 'Yellow', 'Price': 3200000, 'Engine': '5.0L V8', 'VIN': '1FA6P8CF6L1234567'},
    {'Brand': 'Volkswagen', 'Model': 'Passat', 'Year': 2021, 'Color': 'Gray', 'Price': 1900000, 'Engine': '2.0 TSI', 'VIN': '1VWAA7A31LC123456'},
    {'Brand': 'Nissan', 'Model': 'Sentra', 'Year': 2020, 'Color': 'Black', 'Price': 1400000, 'Engine': '1.8L DOHC', 'VIN': '3N1AB8CV5LY123456'},
    {'Brand': 'Chevrolet', 'Model': 'Optima', 'Year': 2021, 'Color': 'Silver', 'Price': 1700000, 'Engine': '1.6L Turbo', 'VIN': '3GNKBKRSXJG123456'},
    {'Brand': 'Hyundai', 'Model': 'Elantra', 'Year': 2022, 'Color': 'White', 'Price': 1600000, 'Engine': '2.0L MPI', 'VIN': '5NPD84LF7LH123456'},
    {'Brand': 'Subaru', 'Model': 'Legacy', 'Year': 2021, 'Color': 'Blue', 'Price': 2000000, 'Engine': '2.5L BOXER', 'VIN': '4S3BWAN65M3000000'},
    {'Brand': 'Kia', 'Model': 'Forte', 'Year': 2020, 'Color': 'Red', 'Price': 1500000, 'Engine': '2.0L MPI', 'VIN': '3KPF24AD0LE123456'}
]

car = t_automobiles(**car_list)
car.save()
```

### 2.3. Get 5 records
```python
table   = TableAutomobiles.objects
records = table.filter()[:5].values()

for item in records:
    print(item)
```

Result:
```log
{'id': 1, 'Brand': 'Dodge', 'Model': 'Ram', 'Year': 2019, 'Color': 'White', 'Price': 2000000, 'Engine': '1.6 PureTech', 'VIN': 'VF3RFE00V5E000000', 'Status': 'Available'}
{'id': 2, 'Brand': 'Peugeot', 'Model': '3008', 'Year': 2019, 'Color': 'White', 'Price': 2000000, 'Engine': '1.6 PureTech', 'VIN': 'VF3RFE00V5E000000', 'Status': 'Available'}
{'id': 3, 'Brand': 'Renault', 'Model': 'Arkana', 'Year': 2019, 'Color': 'Brown', 'Price': 1350000, 'Engine': '1.3 TCe', 'VIN': 'VF1RFE00V5E000000', 'Status': 'Available'}
{'id': 4, 'Brand': 'Audi', 'Model': 'Q5', 'Year': 2020, 'Color': 'Black', 'Price': 2500000, 'Engine': '2.0 TFSI', 'VIN': 'WAUZZZFYXJ1234567', 'Status': 'Available'}
{'id': 5, 'Brand': 'BMW', 'Model': '3 Series', 'Year': 2021, 'Color': 'Blue', 'Price': 2800000, 'Engine': '2.0 TwinPower Turbo', 'VIN': 'WBA5R1C50M7C12345', 'Status': 'Available'}
```

### 2.4. Get 5 records - Brand, Model, Engine
```python
table   = TableAutomobiles.objects
records = table.filter()[:5].values('Brand', 'Model', 'Engine')

for item in records:
    print(item)
```

Result:
```log
{'Brand': 'Dodge', 'Model': 'Ram', 'Engine': '1.6 PureTech'}
{'Brand': 'Peugeot', 'Model': '3008', 'Engine': '1.6 PureTech'}
{'Brand': 'Renault', 'Model': 'Arkana', 'Engine': '1.3 TCe'}
{'Brand': 'Audi', 'Model': 'Q5', 'Engine': '2.0 TFSI'}
{'Brand': 'BMW', 'Model': '3 Series', 'Engine': '2.0 TwinPower Turbo'}
```

### 2.5. Get records with Brown or Blue colors

```python
from Automobiles.models import TableAutomobiles
from django.db.models import Q

table   = TableAutomobiles.objects
q_blue  = Q(Color='Blue')
q_brown = Q(Color='Brown')
query   = table.filter(q_blue | q_brown)
result  = query.values('Brand', 'Model', 'Color', 'Engine')

for item in result:
    print(item)
```

Result:
```
{'Brand': 'Renault', 'Model': 'Arkana', 'Color': 'Brown', 'Engine': '1.3 TCe'}
{'Brand': 'BMW', 'Model': '3 Series', 'Color': 'Blue', 'Engine': '2.0 TwinPower Turbo'}
{'Brand': 'Subaru', 'Model': 'Legacy', 'Color': 'Blue', 'Engine': '2.5L BOXER'}
```

```sql
SELECT 
    "Automobiles_tableautomobiles"."Brand", 
    "Automobiles_tableautomobiles"."Model", 
    "Automobiles_tableautomobiles"."Color", 
    "Automobiles_tableautomobiles"."Engine" 
FROM "Automobiles_tableautomobiles"
WHERE (
    "Automobiles_tableautomobiles"."Color" = Blue OR 
    "Automobiles_tableautomobiles"."Color" = Brown)
```


### 2.6. Get records with Year and Color

```python
from Automobiles.models import TableAutomobiles
from django.db.models import Q

table   = TableAutomobiles.objects
q_year  = Q(Year=2019)
q_color = Q(Color='Brown')
query   = table.filter(q_year & q_color)
result  = query.values('Brand', 'Model', 'Color', 'Engine')

for item in result:
    print(item)
```

Result:
```
{'Brand': 'Renault', 'Model': 'Arkana', 'Color': 'Brown', 'Engine': '1.3 TCe'}
```

```sql
SELECT 
    "Automobiles_tableautomobiles"."Brand", 
    "Automobiles_tableautomobiles"."Model", 
    "Automobiles_tableautomobiles"."Color", 
    "Automobiles_tableautomobiles"."Engine" 
FROM "Automobiles_tableautomobiles" 
WHERE (
    "Automobiles_tableautomobiles"."Year" = 2019 AND 
    "Automobiles_tableautomobiles"."Color" = Brown)
```


### 2.7. Get records with (2019 OR 2020) AND Color

```python
from Automobiles.models import TableAutomobiles
from django.db.models import Q

table   = TableAutomobiles.objects

q_2019  = Q(Year=2019)
q_2020  = Q(Year=2020)
q_white = Q(Color='White')

query   = table.filter((q_2019 | q_2020) & q_white) 
result  = query.values('Brand', 'Model', 'Color', 'Engine')

for item in result:
    print(item)
```

Result:
```
{'Brand': 'Dodge', 'Model': 'Ram', 'Color': 'White', 'Engine': '1.6 PureTech'}
{'Brand': 'Peugeot', 'Model': '3008', 'Color': 'White', 'Engine': '1.6 PureTech'}
{'Brand': 'Honda', 'Model': 'Civic', 'Color': 'White', 'Engine': '1.5L Turbocharged'}
```

```sql
SELECT 
    "Automobiles_tableautomobiles"."Brand", 
    "Automobiles_tableautomobiles"."Model", 
    "Automobiles_tableautomobiles"."Color", 
    "Automobiles_tableautomobiles"."Engine" 
FROM "Automobiles_tableautomobiles" 
WHERE (
    ("Automobiles_tableautomobiles"."Year" = 2019 OR "Automobiles_tableautomobiles"."Year" = 2020) 
    AND "Automobiles_tableautomobiles"."Color" = White)
```



### 2.8. Get records where Value Contain

```python
from Automobiles.models import TableAutomobiles
from django.db.models import Q

table    = TableAutomobiles.objects
q_engine = Q(Engine__contains='2.0')
query    = table.filter(q_engine) 
result   = query.values('Brand', 'Model', 'Color', 'Engine')

for item in result:
    print(item)
```

Result:
```
{'Brand': 'Audi', 'Model': 'Q5', 'Color': 'Black', 'Engine': '2.0 TFSI'}
{'Brand': 'BMW', 'Model': '3 Series', 'Color': 'Blue', 'Engine': '2.0 TwinPower Turbo'}
{'Brand': 'Volkswagen', 'Model': 'Passat', 'Color': 'Gray', 'Engine': '2.0 TSI'}
{'Brand': 'Hyundai', 'Model': 'Elantra', 'Color': 'White', 'Engine': '2.0L MPI'}
{'Brand': 'Kia', 'Model': 'Forte', 'Color': 'Red', 'Engine': '2.0L MPI'}
```

```sql
SELECT 
    "Automobiles_tableautomobiles"."Brand", 
    "Automobiles_tableautomobiles"."Model", 
    "Automobiles_tableautomobiles"."Color", 
    "Automobiles_tableautomobiles"."Engine" 
FROM "Automobiles_tableautomobiles" 
WHERE "Automobiles_tableautomobiles"."Engine"::text LIKE %2.0%
```


### 2.9. Get records where Value StartsWith 

```python
from Automobiles.models import TableAutomobiles
from django.db.models import Q

table    = TableAutomobiles.objects
q_vin    = Q(VIN__startswith='3')
query    = table.filter(q_vin) 
result   = query.values('Brand', 'Model', 'Color', 'VIN')


for item in result:
    print(item)
```

Result:
```
{'Brand': 'Nissan', 'Model': 'Sentra', 'Color': 'Black', 'VIN': '3N1AB8CV5LY123456'}
{'Brand': 'Chevrolet', 'Model': 'Optima', 'Color': 'Silver', 'VIN': '3GNKBKRSXJG123456'}
{'Brand': 'Chevrolet', 'Model': 'Optima', 'Color': 'Silver', 'VIN': '3GNKBKRSXJG123456'}
{'Brand': 'Kia', 'Model': 'Forte', 'Color': 'Red', 'VIN': '3KPF24AD0LE123456'}
```

```sql
SELECT 
    "Automobiles_tableautomobiles"."Brand", 
    "Automobiles_tableautomobiles"."Model", 
    "Automobiles_tableautomobiles"."Color", 
    "Automobiles_tableautomobiles"."VIN" 
FROM "Automobiles_tableautomobiles" 
WHERE "Automobiles_tableautomobiles"."VIN"::text LIKE 3%
```


### 2.10. Get records Combining

```python
from Automobiles.models import TableAutomobiles
from django.db.models import Q

table    = TableAutomobiles.objects
q_price    = Q(Price__gt=1300000) | Q(Price__lt=2000000)
q_year     = Q(Year=2021)
query    = table.filter(q_price & q_year) 
result   = query.values('Brand', 'Model', 'Color', 'Price')


for item in result:
    print(item)
```

Result:
```
{'Brand': 'BMW', 'Model': '3 Series', 'Color': 'Blue', 'Price': 2800000}
{'Brand': 'Toyota', 'Model': 'Camry', 'Color': 'Red', 'Price': 1800000}
{'Brand': 'Volkswagen', 'Model': 'Passat', 'Color': 'Gray', 'Price': 1900000}
{'Brand': 'Chevrolet', 'Model': 'Optima', 'Color': 'Silver', 'Price': 1700000}
{'Brand': 'Chevrolet', 'Model': 'Optima', 'Color': 'Silver', 'Price': 1700000}
{'Brand': 'Subaru', 'Model': 'Legacy', 'Color': 'Blue', 'Price': 2000000}
```

```sql
SELECT
    "Automobiles_tableautomobiles"."Brand", 
    "Automobiles_tableautomobiles"."Model", 
    "Automobiles_tableautomobiles"."Color", 
    "Automobiles_tableautomobiles"."Price" 
FROM "Automobiles_tableautomobiles" 
WHERE (
    ("Automobiles_tableautomobiles"."Price" > 1300000 OR "Automobiles_tableautomobiles"."Price" < 2000000) 
    AND "Automobiles_tableautomobiles"."Year" = 2021)
```


## 3. Q Objects:

| Brand         | Model    | Year | Color  |
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
q_color = Q(Color='Black')              # Case Sensitive & Exact:       Black
q_color = Q(Color__exact='Black')       # Case Sensitive & Exact:       Black
q_color = Q(Color__contains='W')        # Case Sensitive:               White
q_color = Q(Color__startswith='Bl')     # Case Sensitive & Starts With: Black, Blue 
q_color = Q(Color__endswith='e')        # Case Sensitive & Ends With:   White, Blue 
q_color = Q(Color__regex=r'^(Wh|Bl)')   # Case Sensitive & Regex:       White, Blue, Black
```

### 3.2. Text, Case-Insensitive

```python
q_color = Q(Color__iexact='white')      # Case Insensitive & Exact:         white, White, WHITE
q_color = Q(Color__icontains='w')       # Case Insensitive:                 aws, AWS, brown, BROWN, white, White 
q_color = Q(Color__istartswith='w')     # Case Insensitive & Starts With:   white, White
q_color = Q(Color__iendswith='e')       # Case Insensitive & Ends With:     white, WHITE, e, E
q_color = Q(Color__iregex=r'^(Wh|Bl)')  # Case Insensitive & Regex:         white, WHTIE, Blue, BLUE, Black, BLACK
```

### 3.3. Numbers

```python
q_year  = Q(Year=2019)                  # Exact:                    Matches years exactly equal to 2019
q_year  = Q(Year__exact=2019)           # Exact:                    Matches years exactly equal to 2019

q_year  = Q(Year__gt=2019)              # Greater Than:             Matches years greater than 2019
q_year  = Q(Year__gte=2019)             # Greater Than or Equal:    Matches years greater than or equal to 2019

q_year  = Q(Year__lt=2020)              # Less Than:                Matches years less than 2020
q_year  = Q(Year__lte=2020)             # Less Than or Equal:       Matches years less than or equal to 2020

q_year  = Q(Year__range=(2019, 2021))   # Range:                    Matches years within the range 2019-2021
q_year  = Q(Year__in=[2019, 2020, 2021])# In:                       Matches years that are in the list [2019, 2020, 2021]

q_year  = Q(Year__isnull=True)          # Is Null:                  Matches records where the Year is null
q_year  = Q(Year__isnull=False)         # Is Not Null:              Matches records where the Year is not null
```

### 3.4. Combining queries

```python
q_year  = Q(Year=2019) | Q(Year=2020)           # OR:   Matches years that are either 2019 or 2020
q_color = Q(Color='White') | Q(Color='Black')   # OR:   Matches colors that are either 'White' or 'Black'

q_query = Q(Color='White') & Q(Year=2019)       # AND:  Matches records where the Color is 'White' and the Year is 2019

q_query = ~Q(Color='White')                     # NOT:  Matches records where the Color is not 'White'
q_query = ~Q(Color='White') & Q(Year=2019)      # NOT AND: Matches records where
```

### 3.5. Full code example

```sh
./manage.py runscript main
```

```python
from Automobiles.models import TableAutomobiles
from django.db.models import Q

def run():
    pass

table    = TableAutomobiles.objects
q_color  = Q(Color='Brown') | Q(Color='Yellow')
query    = table.filter(q_color)
result   = query.values('Brand', 'Model', 'Color', 'Year')

for item in result:
    print(item)
```

**Result:**
```
{'Brand': 'Renault', 'Model': 'Arkana', 'Color': 'Brown', 'Year': 2019}
{'Brand': 'Ford', 'Model': 'Mustang', 'Color': 'Yellow', 'Year': 2022}
```

```sql
SELECT 
    "Automobiles_tableautomobiles"."Brand", 
    "Automobiles_tableautomobiles"."Model", 
    "Automobiles_tableautomobiles"."Color", 
    "Automobiles_tableautomobiles"."Year" 
FROM "Automobiles_tableautomobiles" 
WHERE (
    "Automobiles_tableautomobiles"."Color" = Brown OR 
    "Automobiles_tableautomobiles"."Color" = Yellow)
```

