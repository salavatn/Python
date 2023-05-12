from database.db_handler import HandlerDB
from database.db_connection import session
from headhunter import ScrapperHeadHunter
from database.tables import TableCity, TableCompany, TableWebsite, TableSalaryUSD, TableDescription, TableJob
import argparse
import time


db = HandlerDB()

parser = argparse.ArgumentParser(description='Search vacancies on Job sites')
parser.add_argument('--search', type=str, help='Search term', required=True)
parser.add_argument('--page',   type=int, help='Page of search results', default=0)
parser.add_argument('--type',   type=str, help='Type of search', default='all', choices=['all', 'title', 'subject'])
args = parser.parse_args()

search_job = args.search.replace(' ', '+')
pages_job  = args.page

table_city      = TableCity
table_company   = TableCompany
table_website   = TableWebsite
table_salary_usd= TableSalaryUSD
table_desc      = TableDescription
table_job       = TableJob

scan_count = 0

while True:
    args
    hh = ScrapperHeadHunter(hh_query=search_job, hh_page=pages_job, hh_type=args.type)
    job_cards = hh.get_job_cards()
    if job_cards is None or len(job_cards) == 0:   
        print("\nScrapping is Finished!\n")
        break

    pages_job += 1
    for card in job_cards:
        scan_count += 1
        job_link    = hh.get_job_link(card)
        if "adsrv.hh.ru" in job_link:   
            continue
        
        print(f"\n\n\n=============================================== Job Scanning #{scan_count}")
       
        job_id      = hh.get_job_id(card)
        check_job   = db.check_job(check_id=job_id)
        if check_job:
            print(f"Job #{job_id} is already in database")
            continue

        job_title    = hh.get_job_title(card)
        job_city     = hh.get_job_city(card)
        job_source   = hh.get_job_source(card)
        job_desc     = hh.get_job_desc(job_link)
        company_num  = hh.get_company_id(card)
        company_name = hh.get_company_name(card)
        company_link = f'https://hh.ru/employer/{company_num}'
        salary_min, salary_max, currency = hh.get_job_salary(card)

        
        print(f"Job ID:         {job_id}")
        print(f"Job Title:      {job_title}")
        print(f"Job City ID:    {job_city}")
        print(f"Salary:         {salary_min} - {salary_max} {currency}")
        print(f"Company Name:   {company_name}")
        print(f"Company Number: {company_num}")
        print(f"Company Link:   {company_link}")
        print(f"Job Link:       {job_link}")
        print(f"Job Source:     {job_source}")


        time.sleep(1)

        # Save to PostgreSQL

        city_id     = db.get_city_id(set_city=job_city)
        company_id  = db.get_company_id(set_id=company_num, set_name=company_name, set_link=company_link)
        id_desc     = db.get_job_desc_id(set_description=job_desc)
        min_usd, max_usd = db.get_salary_usd(set_from=currency, set_min=salary_min, set_max=salary_max)
        currency_id = db.get_currency_id(set_currency=currency)
        website_id  = db.get_website_id(set_url=job_source)


        # Add Job
        job_record_id = db.add_job(
            set_id          = job_id,
            set_title       = job_title,
            set_usd_min     = min_usd,
            set_usd_max     = max_usd,
            set_min         = salary_min,
            set_max         = salary_max,
            set_currency_id = currency_id,
            set_link        = job_link,
            set_city_id     = city_id,
            set_company_id  = company_id,
            set_desc_id     = id_desc,
            set_website_id  = website_id)

        print(f"Job Record ID:  {job_record_id}")
