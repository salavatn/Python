from ..app_db.handler_db import HandlerDB
from app_webscrapping.scrapper_hh import ScrapperHeadHunter
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start program')


db = HandlerDB()


hh_arguments = {'query': search_kw, 'page': search_pg, 'type': search_tp}
hh = ScrapperHeadHunter(**hh_arguments)


job_cards = hh.get_job_cards()
if job_cards is None or len(job_cards) == 0:
    logging.info('No jobs found')
    exit()


scan_count = 0
for card in job_cards:
    scan_count += 1

    logging.info(f"Scanning job #{scan_count}")
    
    # Checking and ignoring ads vacancies:
    job_link    = hh.get_job_link(card)
    if "adsrv.hh.ru" in job_link:   
        continue
    
    # Checking if job is already in database:
    vacancy_id = hh.get_job_id(card)
    job_exist  = db.check_job(vacancy_id)
    if job_exist:
        logging.info(f"Job #{vacancy_id} is already in database")
        continue

    # Get vacancies info:
    job_id       = hh.get_job_id(card)              # OK
    job_title    = hh.get_job_title(card)           # OK
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
'''
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
'''