
```
JOBSCRAPPING/
├── converter/
│   ├── __init__.py
│   └── currancy.py
│
├── database/
│   ├── __init__.py
│   ├── db_connection.py
│   ├── db_handler.py
│   │
│   └── tables/
│       ├── __init__.py
│       ├── cities.py
│       ├── description.py
│       ├── employers.py
│       ├── jobs.py
│       ├── salary.py
│       ├── skill.py
│       └── website.py
│
├── headhunter/
│   ├── __init__.py
│   └── scrapper_hh.py
│   
├── tests/
│   ├── __init__.py
│   ├── test_converter.py
│   ├── test_db_connection.py
│   ├── test_db_handler.py
│   ├── test_skraper_hh.py
│   └── test_tables.py
│   
├── __init__.py
├── .env_api
├── .env_db
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

```

---

**How to us:**
```sh
python main.py --search Python --type title
```

**Example result:**
```sh
=============================================== Job #8
Job #79742922 is already in database

=============================================== Job #9
Job ID:         80074829
Job Title:      Junior Python разработчик
Job City ID:    Иркутск
Salary:         40000 - 50000 RUB
Company Name:   ООО БВК
Company Number: 6063299
Company Link:   https://hh.ru/employer/6063299
Job Link:       https://hh.ru/vacancy/80074829
Job Source:     https://hh.ru/
Currency RUB already in database. USD = 0.0124299999889373
Job Record ID:  2213

=============================================== Job #10
Job #80082407 is already in database
```

**SQL Query:**
```sql
SELECT
  job_vacancies.id      AS "ID",
  job_vacancies.title   AS "Title",
  job_city.name         AS "City",
  job_vacancies.usd_min AS "USD Min",
  job_vacancies.usd_max AS "USD Max",
  job_company.name      AS "Company",
  job_vacancies.link    AS "Job URL"

FROM job_vacancies

INNER JOIN job_city     
  ON job_vacancies.city_id = job_city.id       -- Join with City Table
INNER JOIN job_company  
  ON job_vacancies.company_id = job_company.id -- Join with Company Table

WHERE                                          
  job_vacancies.usd_min IS NOT NULL OR        -- Hide Null in min salary OR
  job_vacancies.usd_max IS NOT NULL           -- Hide Null in max salary

ORDER BY job_vacancies.id DESC
LIMIT 8;
```

**RESULT:**
| ID   | Title                                                                      | City         | USD Min | USD Max | Company                         | Job URL                        |
| ---- | -------------------------------------------------------------------------- | ------------ | ------- | ------- | ------------------------------- | ------------------------------ |
| 2214 | Программист Python                                                         | Владивосток  | 870     |         | DNS Технологии                  | https://hh.ru/vacancy/80127347 |
| 2213 | Junior Python разработчик                                                  | Иркутск      | 497     | 622     | ООО БВК                         | https://hh.ru/vacancy/80074829 |
| 2212 | Python-разработчик (Django, DRF)                                           | Москва       | 746     | 2735    | ООО Фабрика Решений             | https://hh.ru/vacancy/80082407 |
| 2207 | Ведущий Python разработчик / Senior python developer                       | Воронеж      | 1865    | 3108    | Актив Компьютерс                | https://hh.ru/vacancy/80091877 |
| 2203 | Ведущий программист Python                                                 | Новосибирск  | 2797    |         | Тензор                          | https://hh.ru/vacancy/80103251 |
| 2202 | Преподаватель разработки игр на Python в онлайн-школу для детей (удаленно) | Тюмень       | 311     | 746     | Компьютерная школа IT-Compot    | https://hh.ru/vacancy/79692172 |
| 2199 | Преподаватель кружка программирования Python                               | Новошахтинск | 311     |         | ИП Клименко Валерий Анатольевич | https://hh.ru/vacancy/80140915 |
| 2198 | Преподаватель кружка программирования Python                               | Новочеркасск | 311     |         | ИП Клименко Валерий Анатольевич | https://hh.ru/vacancy/80141171 |