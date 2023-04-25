from database.tables.cities import TableCities
from database.tables.job import TableJob
from database.tables.employers import TableCompany
from database.db_connection import session
from headhunter import HeadHunter
import argparse
import time

company = TableCompany

parser = argparse.ArgumentParser(description='Search vacancies on Job sites')
parser.add_argument('--search', type=str, help='Search term', required=True)
parser.add_argument('--page',  type=int, help='Page of search results', default=0)
args = parser.parse_args()


searching = '+'.join(args.search.split())
hh = HeadHunter(keywords=searching, page=args.page)
job_pages   = hh.get_page_count()


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
        
# id          = Column(Integer, primary_key=True)
# job_id      = Column(String(50))
# title       = Column(String(200))
# salary      = Column(String(50))
# city_id     = Column(Integer, ForeignKey('jobs_cities.id'))
# employer_id = Column(Integer, ForeignKey('jobs_company.id'))
# description = Column(Text)



# Vacancy #187
# Traceback (most recent call last):
#   File "/Users/salavat/GitHub/Python/WebSraping/JobScrapping/main.py", line 37, in <module>
#     job_desc    = hh.get_vacancy_desc(job_link)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/salavat/GitHub/Python/WebSraping/JobScrapping/headhunter/scrapper.py", line 84, in get_vacancy_desc
#     desc      = vacancy.find('div', {'data-qa': 'vacancy-description'}).text
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'text'
# (venv) salavat@Salavat JobScrapping % 