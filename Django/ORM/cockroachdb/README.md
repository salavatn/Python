# Django ORM connections to CockroachDB (PostgreSQL)

From Django we are use only **ORM** to connect to CockroachDB database. 

## What is CockroachDB?

> [CockroachDB](https://www.cockroachlabs.com/docs/stable/) is a distributed SQL database built on a transactional and strongly-consistent key-value store. It scales horizontally; survives disk, machine, rack, and even datacenter failures with minimal latency disruption and no manual intervention; supports strongly-consistent ACID transactions; and provides a familiar SQL API for structuring, manipulating, and querying data.

## Project Architecture
```
COCKROACHDB/
├── config/
│   ├── __init__.py
│   ├── library.py
│   └── settings.py
│
├── database/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── __init__.py
│   └── models.py
│
├── mgmt/
│   ├── __init__.py
│   ├── client_db.py
│   └── django_admin.py
│
├── __init__.py
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## How to run the project?
1. First, you need to install the dependencies:
    ```bash
    $ pip install -r requirements.txt
    ```
2. Then, you need rename `.env_BACKUP` to `.env` and set the environment variables:
    ```bash
    $ mv .env_BACKUP .env
    ```
3. Finally, you can run the project:
    ```bash
    $ python -m main
    ```
    ```bash
    Your first name:  Will
    Your second name: Smith
    Your city:        Philadelphia
    Your birthday:    1968-09-25

    Victor Balabanov from Moscow. Birthday is 1992-02-19
    Jack London from San Francisco. Birthday is 1986-01-12
    Will Smith from Philadelphia. Birthday is 1968-09-25
    ```
