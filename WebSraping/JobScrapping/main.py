from database.db_connection import session
from headhunter import ScrapperHeadHunter
from database.tables.salary import TableSalaryAll
from database.tables.cities import TableCity
from database.tables.employers import TableCompany
from database.tables.website import TableWebsite
from database.tables.description import TableDescription
from database.tables.jobs import TableJob
import argparse
import time
from database.db_handler import HandlerDB

db = HandlerDB()


parser = argparse.ArgumentParser(description='Search vacancies on Job sites')
parser.add_argument('--search', type=str, help='Search term', required=True)
parser.add_argument('--page',   type=int, help='Page of search results', default=0)
args = parser.parse_args()

search_job = args.search.replace(' ', '+')
pages_job = args.page


table_city      = TableCity
table_company   = TableCompany
table_website   = TableWebsite
table_salary    = TableSalaryAll
# table_salary_usd = TableSalaryUSD()
table_desc      = TableDescription
table_job       = TableJob
# RUB_USD         = Converter(from_currency='RUB', to_currency='USD')
# KZT_USD         = Converter(from_currency='KZT', to_currency='USD')



# hh = ScrapperHeadHunter(hh_query=search_job, hh_page=pages__job) # Default


# all_cards = hh.get_job_cards()
count = 0

# while all_cards is not None and len(all_cards) > 0:
while True:
    
    
    hh = ScrapperHeadHunter(hh_query=search_job, hh_page=pages_job)
    job_cards = hh.get_job_cards()
    if job_cards is None or len(job_cards) == 0:   
        print("\nScrapping is Finished!\n")
        break

    pages_job += 1

    

    for card in job_cards:

        count += 1

        job_link    = hh.get_job_link(card)
        if "adsrv.hh.ru" in job_link:
            continue
        
        print(f"\n\n\n=============================================== Job #{count}")
       
        job_id      = hh.get_job_id(card)
        check_job   = db.check_job(job_id=job_id)
        if check_job:
            print(f"Job #{job_id} is already in database")
            continue

        job_title   = hh.get_job_title(card)
        
        job_city    = hh.get_job_city(card)
        job_source  = hh.get_job_source(card)
        job_desc    = hh.get_job_desc(job_link)
        company_id  = hh.get_company_id(card)
        company_name= hh.get_company_name(card)
        company_link = f'https://hh.ru/employer/{company_id}'
        salary_min, salary_max, currency = hh.get_job_salary(card)

        
        print(f"Job ID:         {job_id}")
        print(f"Job Title:      {job_title}")
        print(f"Job City ID:    {job_city}")
        print(f"Salary:         {salary_min} - {salary_max} {currency}")
        print(f"Company Name:   {company_name}")
        print(f"Company ID:     {company_id}")
        print(f"Company Link:   {company_link}")
        print(f"Job Link:       {job_link}")
        print(f"Job Source:     {job_source}")


        time.sleep(1)

        # Save to PostgreSQL

        id_city     = db.get_city_id(city_name=job_city)
        id_company  = db.get_company_id(
                            company_id=company_id,
                            company_name=company_name,
                            company_link=company_link)
        id_desc     = db.get_description_id(job_description=job_desc)
        min_usd, max_usd = db.get_salary_usd(
                            currency=currency,
                            salary_min=salary_min,
                            salary_max=salary_max)
        id_salary   = db.get_original_salary_id(
                            currency    = currency,
                            salary_min  = salary_min,
                            salary_max  = salary_max)
        id_website  = db.get_website_id(website_url=job_source)

        # Add Job
        job_record_id = db.add_job(
            set_job_id          = job_id,
            set_job_title       = job_title,
            set_salary_min      = min_usd,
            set_salary_max      = max_usd,
            set_salary_original_id = id_salary,
            set_job_link        = job_link,
            set_city_id         = id_city,
            set_company_id      = id_company,
            set_description_id  = id_desc,
            set_website_id      = id_website
        )

        print(f"Job Record ID:  {job_record_id}")
        


        time.sleep(1)

'''
В данном проекте используется:
- Классы и Функции
- Библиотеки:
    - requests
    - BeautifulSoup
    - psycopg2-binary
    - sqlalchemy
    - argparse
    - time
    - datetime
    - re
    - json
    - os
    - dotenv
- Запросы к:
    - PostgreSQL
    - API Курсов валют
- Работа с:
    - PostgreSQL
    - JSON
    - CSV
    - .env
- Регулярные выражения
- ООП
- Работа с файлами
- Работа с датой и временем
- Работа с аргументами командной строки
- Работа с API
- Работа с БД
- Работа с JSON
'''