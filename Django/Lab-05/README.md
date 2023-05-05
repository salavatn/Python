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
    <summary>1.1. Подготовить виртуальное окружение </summary>
    <code>
        python -m venv venv             <br>    
        source venv/bin/activate        <br>
    </code>
</details>

<details markdown="1"> 
    <summary>1.2. Добавить библиотеки в requirements.txt и установить</summary>
    <code>
        echo django             >> requirements.txt  <br>    
        echo django-extensions  >> requirements.txt  <br>    
        echo psycopg2-binary    >> requirements.txt  <br>    
        echo python-dotenv      >> requirements.txt  <br>    
        pip install -r requirements.txt              <br>
    </code>
</details>

<details markdown="1"> 
    <summary>1.3. Создать проект "FranceCars"</summary>
<pre><code>django-admin startproject FranceCars</code></pre>
</details>

<details markdown="1"> 
    <summary>1.4. Сформируйте .env с параметрами подключения к PostgeSQL</summary>
<pre><code>POSTGRES_HOST=127.0.0.1    
POSTGRES_PORT=5432       
POSTGRES_DB=postgres       
POSTGRES_USER=postgres      
POSTGRES_PASSWORD=Pa$$word  
</code></pre>
</details>


<details markdown="1"> 
<summary>1.5. Настройте в settings.py подключение к PostgreSQL</summary>
<pre><code>from dotenv import load_dotenv     
import os                         
<br>
load_dotenv(dotenv_path='.env')            
pg_host  = os.getenv('POSTGRES_HOST')       
pg_port  = os.getenv('POSTGRES_PORT')       
pg_db    = os.getenv('POSTGRES_DB')        
pg_user  = os.getenv('POSTGRES_USER')       
pg_psswd = os.getenv('POSTGRES_PASSWORD')   
<br>
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
</code></pre>
</details>

