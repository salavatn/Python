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


db  = HandlerDB()

page = 0
scan_count = 0
while True:

    hh_data = {'query': 'Python', 'page':page, 'type': 'title'}
    hh  = ScrapperHeadHunter(**hh_data)

    job_cards = hh.get_job_cards()

    if job_cards is None or len(job_cards) == 0:
        logger.info(f'HanlderWS: No jobs found')
        exit()

    logger.info(f'HanlderWS: Scanning Page #{page}')

    
    for card in job_cards:

        logger.info(f"HanlderWS: Scanning Job #{scan_count}")
        scan_count += 1
        
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
        logger.debug(f'HandlerWS.Job ID = {job_num}')      
        job_title    = hh.get_job_title(card)   
        logger.debug(f'HandlerWS.Job Title = {job_title}')
        job_city     = hh.get_job_city(card)
        logger.debug(f'HandlerWS.Job City ID = {job_city}')
        job_source   = hh.get_job_source(card)
        logger.debug(f'HandlerWS.Job Source = {job_source}')
        job_desc     = hh.get_job_desc(job_link)
        logger.debug(f'HandlerWS.Job Link = {job_link}')
        company_num  = hh.get_company_id(card)
        logger.debug(f'HandlerWS.Company Number = {company_num}')
        company_name = hh.get_company_name(card)
        logger.debug(f'HandlerWS.Company Name = {company_name}')
        company_link = f'https://hh.ru/employer/{company_num}'
        logger.debug(f'HandlerWS.Company Link = {company_link}')
        salary_min, salary_max, currency = hh.get_job_salary(card)
        logger.debug(f'HandlerWS.Salary = {salary_min} - {salary_max} {currency}')
        job_posted   = hh.get_job_posted(job_link=job_link)
        logger.debug(f'HandlerWS.Job Posted = {job_posted}')
        
        
        
        
        
        
        
        
        
        
        

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


        # Table DESCRIPTIONS: add Description and return ID
        data = {'description': job_desc}
        desc_id = db.set_description(**data)


        # Table RESOURCE: add Resource and return ID
        data = {'url': job_source}
        resource_id = db.set_resource(**data)


        # Table VACANCIES: add Vacancy
        data = {'check_id': job_num}
        job_exist = db.check_job(**data)

        # if not job_exist:
        data = {
            'job_id': job_num, 
            'job_title': job_title, 
            'job_link': job_link, 
            'salary_min_usd': minimum, 
            'salary_max_usd': maximum, 
            'salary_min': salary_min, 
            'salary_max': salary_max, 
            'currency': currency, 
            'city': city_id, 
            'company': company_id, 
            'resource': resource_id, 
            'desc': desc_id, 
            'published': job_posted}
        db.set_vacancy(**data)
        logging.info(f"Job #{job_num} added to database")

    page += 1