# Web Scrapping

## Структура проекта:
```
WEBSCRAPPING/
│   
├── Ufanet/                 # папка с приложением.
│   │ 
│   ├── main.py             # файл, содержащий основную логику приложения.
│   │ 
│   ├── database.py         # файл, отвечающий за подключение к базе данных.
│   │ 
│   ├── requirements.txt    # файл, содержащий список зависимостей для проекта.
│   │ 
│   └── .env_db             # файл, описываются параметры для подключения к БД
│ 
└── README.md               # файл с описанием проекта и инструкциями по его использованию.
```

```python
import requests
from bs4 import BeautifulSoup

url     = 'https://salavatn.github.io/Python/Directions/webscrapping/'
response = requests.get(url)  # <class 'requests.models.Response'>

html    = response.content 

website = BeautifulSoup(html, 'html.parser')    # <class 'bs4.BeautifulSoup'>
print(website)
```

Метод `response.content`, который возвращает содержимое страницы в бинарном виде, а во втором - метод `response.text`, который возвращает содержимое страницы в виде текста.

В большинстве случаев лучше использовать вариант с `response.text`, так как он возвращает текстовую строку, которую может легко обработать BeautifulSoup. Однако, если содержимое страницы содержит бинарные данные, например, изображения, то лучше использовать `response.content`.

Таким образом, в данном случае лучше использовать второй вариант с response.text, так как мы получаем текстовую страницу, которую нужно распарсить с помощью `BeautifulSoup`.

## Find
* **find**(tag, attributes, recursive, text, **kwargs) - метод для поиска первого вхождения тега в HTML-документе. Возвращает результат в виде объекта Tag или None, если ничего не найдено.
* **findChild**(tag, attributes, recursive, text, **kwargs) - метод для поиска первого вхождения тега в дочерних элементах данного тега. Возвращает результат в виде объекта Tag или None, если ничего не найдено.
* **findChildren**(tag, attributes, recursive, text, limit, **kwargs) - метод для поиска всех дочерних элементов данного тега с заданным именем тега и атрибутами. Возвращает результат в виде списка Tag или пустого списка, если ничего не найдено.
* **find_all**(name, attrs, recursive, text, limit, **kwargs) - метод для поиска всех вхождений тега в HTML-документе. Возвращает результат в виде списка Tag или пустого списка, если ничего не найдено.
* **find_all_next**(name, attrs, text, limit, **kwargs) - метод для поиска всех следующих элементов с заданным именем тега и атрибутами. Возвращает результат в виде списка Tag или пустого списка, если ничего не найдено.
* **find_all_previous**(name, attrs, text, limit, **kwargs) - метод для поиска всех предыдущих элементов с заданным именем тега и атрибутами. Возвращает результат в виде списка Tag или пустого списка, если ничего не найдено.
* **find_next**(name, attrs, text, **kwargs) - метод для поиска следующего элемента с заданным именем тега и атрибутами. Возвращает результат в виде объекта Tag или None, если ничего не найдено.
* **find_next_sibling**(name, attrs, text, **kwargs) - метод для поиска следующего соседнего элемента с заданным именем тега и атрибутами. Возвращает результат в виде объекта Tag или None, если ничего не найдено.
* **find_next_siblings**(name, attrs, text, **kwargs) - метод для поиска всех следующих соседних элементов с заданным именем тега и атрибутами. Возвращает результат в виде списка Tag или пустого списка, если ничего не найдено.
* **find_parent**(name, attrs, **kwargs) - метод для поиска родительского элемента с заданным именем тега и атрибутами. Возвращает результат в виде объекта Tag или None, если ничего не найдено.
* **find_parents**(name, attrs, **kwargs) - метод для поиска всех родительских элементов с заданным именем тега и атрибутами. Возвращает результат в виде списка Tag или пустого списка, если ничего не найдено.
* **find_previous**(name, attrs, text, **kwargs


Список для разработчика Python:
- Фреймворк
- Библиотеки анализа данных
- Библиотеки для ML AI
- ORM
- Библиотеки для сетевых протоколов
- Инструменты для тестирования
- Инструмент для управления зависимостями
- Системы контроля версий
- IDE
- Очереди сообщений
- Автоматизации задач (например, Fabric и Ansible)




MySQL
PostgreSQL
ClickHouse
Redis
PostgreSQL
MongoDB
FastAPI
Django
Flask
Pyramid
Tornado
CherryPy
Bottle
Falcon
web2py
Hug
Sanic
aiohttp
TurboGears
Django Rest
Vue.js
React
Angular
Svelte
Ember.js
Backbone.js
Polymer
Docker
Kubernetes
Docker Compose
Podman
Mesos
Nomad
OpenShift
NumPy
Pandas
Matplotlib
SciPy
Scikit-learn
aiohttp
asyncpg
NLTK
SpaCy
Gensim
TensorFlow
PyTorch
Keras
OpenCV
SQLAlchemy
Django ORM
PyMongo
Requests
urllib
Twisted
asyncio
Pytest
unittest
nose
doctest
Ansible
Terraform
Fabric
pip
virtualenv
conda
poetry
Git
Mercurial
SVN
PyCharm
Visual Studio Code
Sublime Text
RabbitMQ
Kafka
Redis