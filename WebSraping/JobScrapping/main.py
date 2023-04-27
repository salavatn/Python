from database.db_connection import session
from headhunter import ScrapperHeadHunter
from database.tables.salary import TableSalaryAll
from database.tables.cities import TableCity
from database.tables.employers import TableCompany
from database.tables.website import TableWebsite
from database.tables.description import TableDescription
from database.tables.jobs import TableJob
from converter import Converter
import argparse
import time




parser = argparse.ArgumentParser(description='Search vacancies on Job sites')
parser.add_argument('--search', type=str, help='Search term', required=True)
parser.add_argument('--page',   type=int, help='Page of search results', default=0)
args = parser.parse_args()

search_job = args.search.replace(' ', '+')
pages__job = args.page


table_city      = TableCity()
table_company   = TableCompany()
table_website   = TableWebsite()
table_salary    = TableSalaryAll()
# table_salary_usd = TableSalaryUSD()
table_desc      = TableDescription()
table_job       = TableJob()
RUB_USD         = Converter(from_currency='RUB', to_currency='USD')
KZT_USD         = Converter(from_currency='KZT', to_currency='USD')



# hh = ScrapperHeadHunter(hh_query=search_job, hh_page=pages__job) # Default
hh = ScrapperHeadHunter(hh_query='Forcepoint', hh_page=0)


job_cards = hh.get_job_cards()
if job_cards is None or len(job_cards) == 0:   
    print("\nScrapping is Finished!\n")
    exit()

for card in job_cards:
    job_title   = hh.get_job_title(card)
    job_id      = hh.get_job_id(card)
    job_city    = hh.get_job_city(card)
    job_link    = hh.get_job_link(card)
    job_source  = hh.get_job_source(card)
    job_desc    = hh.get_job_desc(job_link)
    company_id  = hh.get_company_id(card)
    company_name= hh.get_company_name(card)
    salary_min, salary_max, currency = hh.get_job_salary(card)

    print(f"\n\n\n=============================================== Job #{job_id}")
    print(f"Job ID:      {job_id}")
    print(f"Job Title:   {job_title}")
    print(f"Job City ID: {job_city}")
    print(f"Company:     {company_name}")
    print(f"Salary:      {salary_min} - {salary_max} {currency}")
    print(f"Job Link:    {job_link}")
    # print(f"Source:     {job_source}")
    # print(f"Desc:       {job_desc}")

    time.sleep(1)

    # Save to PostgreSQL
    # City
    query      = session.query(table_city)
    city_name  = query.filter(table_city.city == job_city).first()

    if not city_name:
        row = table_city(city = job_city)
        session.add(row)
        session.commit()

    break
    '''if not city_name:
        city_name = table_city(city=job_city)
        session.add(city_name)
        session.commit()
    
    
    # Company
    company_name = session.query(table_company).filter(table_company.company == company_name).first()
    if not company_name:
        company_name = table_company(company=company_name)
        session.add(company_name)
        session.commit()

    # Website
    website_name = session.query(table_website).filter(table_website.website == job_source).first()
    if not website_name:
        website_name = table_website(website=job_source)
        session.add(website_name)
        session.commit()

    # Salary Original
    salary_all = table_salary(
        salary_min=salary_min, 
        salary_max=salary_max, 
        currency=currency)
    session.add(salary_all)
    session.commit()

    # Salary USD
    if currency == 'KZT':
        salary_min_usd = KZT_USD * salary_min
        salary_max_usd = KZT_USD * salary_max
    elif currency == 'RUB':
        salary_min_usd = RUB_USD * salary_min
        salary_max_usd = RUB_USD * salary_max

    # Description
    description = table_desc(job_desc=job_desc)
    session.add(description)
    session.commit()

    


    website_id      = website_name.id
    city_id         = city_name.id
    company_id      = company_name.id
    salary_all_id   = salary_all.id
    description_id  = description.id

    job = table_job(
        job_id          = job_id,
        job_title       = job_title,
        salary_min      = salary_min_usd,
        salary_max      = salary_max_usd,
        id_salary_all   = salary_all_id,
        job_link        = job_link,
        id_city_name    = city_id,
        id_company_name = company_id,
        id_website_name = website_id,
        id_description  = description_id
    )
    session.add(job)
    session.commit()

    print(f"Job #{job_id} is saved to PostgreSQL")


'''



'''
count = 1
for page in range(0, job_pages+1):
    print(f"======== START READING PAGE #{page}/{job_pages} ========")

    hh = HeadHunter(keywords=searching, page=page)
    job_cards = hh.get_job_cards()
    # print(f"Cards count:\t{len(job_cards)}")    

    for card in job_cards:
        time.sleep(0.5)
        print(f"\n\nVacancy #{count}")

        job_id      = hh.get_vacancy_id(card)
        job_title   = hh.get_vacancy_title(card)
        job_salary  = hh.get_vacancy_salary(card)
        job_city    = hh.get_vacancy_city(card)
        job_link    = hh.get_vacancy_link(card)
        # job_desc    = hh.get_vacancy_desc(job_link)
        employer_id = hh.get_employer_id(card)


        table_city = TableCities
        query      = session.query(table_city)
        city_name  = query.filter(table_city.city == job_city).first()

        if not city_name:
            row = table_city(city = job_city)
            session.add(row)
            session.commit()
        
        city_name  = query.filter(table_city.city == job_city).first()

        # Get city ID
        job_city_id = city_name.id


        table_job = TableJob
        

        # Check if job already exists in DB
        query      = session.query(table_job)
        job_exists = query.filter(table_job.job_id == job_id).first()
        
        if job_exists:
            print(f"\tJob #{job_exists.job_id} already exists in DB")
            count += 1
            continue

        print(f"\tJob ID:      {job_id}")
        print(f'\tTitle:       {job_title}')
        print(f"\tSalary:      {job_salary}")
        print(f"\tCity:        {job_city}")
        print(f"\tLink:        {job_link}")
        print(f"\tEmployer ID: {employer_id}")
     

        row = table_job(
            job_id      = job_id,
            title       = job_title,
            salary      = job_salary,
            city_id     = job_city_id,     # City ID
            company_id  = employer_id) #,
            # description = job_desc)
        session.add(row)
        session.commit()
        
        count += 1

'''




'''
+ Таблица Города
+ Вакансии (добавить ссылку на вакансию, Source_ID - ссылк на таблицу Sources )

+ Описание вакансии (отдельно) 
+ Sources - это веб-сайт, ресурс с вакансиями
+ Конвертация валют

- Таблица Страны
- Категория навыков (skills)
- Навыки (skills)
+ Компания
'''