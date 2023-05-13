import os
import django
import time
import logging
import logging.config
from app_webscrapping.scrapper_hh import ScrapperHeadHunter
from handler_db import HandlerDB


# Set up Django environment
os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='job_finder.settings')
django.setup()

# Load the logging configuration from file
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

logger.debug('FILE: handler_scrapping.py')

hh_data = {'query': 'Python', 'page':0, 'type': 'title'}

hh  = ScrapperHeadHunter(**hh_data)
db  = HandlerDB()

job_cards = hh.get_job_cards()
if job_cards is None or len(job_cards) == 0:
    logging.info('No jobs found')
    exit()


scan_count = 0
for card in job_cards:
    scan_count += 1
    logging.info(f"Scanning job #{scan_count}")
    
    # Checking #1: Ignoring ads vacancies
    job_link    = hh.get_job_link(card)
    if "adsrv.hh.ru" in job_link:   
        continue

    # Checking #2: Continue, if job is already in database
    vacancy_id = hh.get_job_id(card)
    job_exist  = db.check_job(check_id=vacancy_id)
    if job_exist:
        logging.debug(f"Job #{vacancy_id} is already in database")
        continue


    # Get vacancies info:
    job_num      = hh.get_job_id(card)           
    job_title    = hh.get_job_title(card)   
    job_city     = hh.get_job_city(card)
    job_source   = hh.get_job_source(card)
    job_desc     = hh.get_job_desc(job_link)
    company_num  = hh.get_company_id(card)
    company_name = hh.get_company_name(card)
    company_link = f'https://hh.ru/employer/{company_num}'
    salary_min, salary_max, currency = hh.get_job_salary(card)
    job_posted   = hh.get_job_posted(job_link=job_link)



    logging.debug(f"Job ID:         {job_num}")
    logging.debug(f"Job Title:      {job_title}")
    logging.debug(f"Job City ID:    {job_city}")
    logging.debug(f"Salary:         {salary_min} - {salary_max} {currency}")
    logging.debug(f"Company Name:   {company_name}")
    logging.debug(f"Company Number: {company_num}")
    logging.debug(f"Company Link:   {company_link}")
    logging.debug(f"Job Link:       {job_link}")
    logging.debug(f"Job Source:     {job_source}")
    logging.debug(f"Job Posted:     {job_posted}")
    logging.debug(f"")

    time.sleep(2)

    # Save to PostgreSQL

    # Table CURRENCIES: add Currency and Min/Max USD
    data = {'minimum': salary_min, 'maximum': salary_max, 'currency': currency}
    minimum, maximum = db.get_usd_salary(**data)


    # Table LOCATION: add City and return ID
    data = {'city': job_city, 'country': 'Unknown'}
    city_id = db.set_location(**data)



    # Table COMPANIES: add Company and return ID
    data = {'company': company_name, 'city': job_city, 'link': company_link}
    company_id = db.set_company(**data)
