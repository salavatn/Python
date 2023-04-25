JOBSCRAPPING/
├── database
│   ├── __init__.py
│   ├── db_connection.py
│   ├── .env_db
│   └── tables/
│       ├── __init__.py
│       ├── job.py
│       └── skill.py
└── headhunter
    ├── __init__.py
    └── scrapper.py


Файл headhunter/__init__.py:
from database.db_connection import Base, engine, session
from database.tables.skill  import TableSkill
from database.tables.job    import TableJob

Файл headhunter/scrapper.py:
from database.db_connection import Base, engine, session
from database.tables.job    import TableJob

table = TableJob



При запуске scrapper.py:
    from database.tables.job    import TableJob
ModuleNotFoundError: No module named 'database'