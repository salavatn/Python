import os
import django
import time
import logging
import logging.config
from app_webscrapping.scrapper_hh import ScrapperHeadHunter


# Set up Django environment
os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='job_finder.settings')
django.setup()

# Load the logging configuration from file
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

from typing import Optional, List, Dict, Tuple, Union, Any, Callable, TypeVar, Generic, Type, cast, overload
from app_db import models
from currancy import Converter
import datetime

logger.debug('FILE: handler_scrapping.py')


class HandlerDB:
    def __init__(self) -> None:
        '''Initiate database tables'''
        self.location    = models.Location
        self.company     = models.Companies
        self.description = models.Descriptions
        self.currencies  = models.Currencies
        self.resouce     = models.Resource
        self.vacancy     = models.Vacancies


    def check_job(self, check_id: int) -> bool:
        '''Table VACANCIES: check if job is already in database'''
        table = self.vacancy.objects.filter(job_id=check_id).first()
        if table:
            return True
        else:
            return False


    def set_location(self, city: str, country: str = None) -> int:
        '''Table LOCATION: add City and return ID'''
        data  = {'city': city, 'country': country}
        table = self.location.objects.filter(city=city).first()
        if table:
            return table.id
        else:
            table = self.location(**data)
            table.save()
            return table.id
            

    def set_company(self, company: str, city: str, link: int) -> int:
        '''Table COMPANIES: add Company and return ID'''

        data  = {'company': company, 'city': city, 'link': link}
        table = self.company.objects.filter(company=company).first()

        if table:
            return table.id
        else:
            table = self.company(**data)
            table.save()
            return table.id
        
        
    def set_description(self, description: str) -> int:
        '''Table DESCRIPTIONS: add Description and return ID'''

        data  = {'text': description}
        table = self.description.objects.filter(text=description).first()

        if table:
            return table.id
        else: 
            table = self.description(**data)
            table.save()
            return table.id
            

    def get_usd_salary(self, currency: str, minimum:int, maximum:int) -> Tuple[Optional[float], Optional[float]]: #currency: str, minimum:int, maximum:int

        '''Table CURRENCIES: add Currency and return ID'''
        
        date = datetime.datetime.now().strftime('%Y-%m-%d')


        # Checking #1: If currency is None, return None, None
        if currency is None:
            logger.debug(f'Currency is None. Minimum: {minimum}, Maximum: {maximum}')
            return None, None
        
        table = self.currencies.objects.filter(currency=currency).first()

        # Checking #2: If currency is USD, return minimum, maximum
        if currency == 'USD':    
            logger.debug(f'Currency is USD. Minimum: {minimum}, Maximum: {maximum}')
            return minimum, maximum

        # Checking #3: If currency is not USD, convert to USD
        if not table:
            converter    = Converter(currency=currency)
            from_to_usd  = converter.get_convert()
            data  = {'currency': currency, 'usd': from_to_usd, 'date': date}
            table = self.currencies(**data)
            table.save()
            logger.debug(f'New currency {currency} added to database. USD = {from_to_usd}')
        else:
            from_to_usd = table.usd
            logger.debug(f'Currency {currency} already exist in database. USD = {from_to_usd}')


        if minimum is not None: 
            logger.debug(f'Converting {minimum} {currency} to USD')
            minimum = round((from_to_usd * minimum), 2)


        if maximum is not None: 
            logger.debug(f'Converting {maximum} {currency} to USD')
            maximum = round((from_to_usd * maximum), 2)

        logger.debug(f'Currency is USD. Minimum: {minimum} USD, Maximum: {maximum} USD.')

        return minimum, maximum





    # def get_website_id(self, set_url):
    #     table   = session.query(self.WEBSITE)
    #     record  = table.filter(self.WEBSITE.url == set_url).first()

    #     if not record:
    #         row = self.WEBSITE(url=set_url)
    #         session.add(row)
    #         session.commit()
    #         return row.id
        
    #     return record.id
        
    # def add_job(self, set_id, set_title, set_link, set_min, set_max, set_usd_min, set_usd_max,
    #                   set_currency_id, set_city_id, set_company_id, set_desc_id, set_website_id):
    #     table = session.query(self.JOB)
    #     record = table.filter(self.JOB.job_id == set_id).first()
    #     if not record:
    #         row = self.JOB(
    #             job_id          = set_id,
    #             title           = set_title,
    #             usd_min         = set_usd_min,
    #             usd_max         = set_usd_max,
    #             current_min     = set_min,
    #             current_max     = set_max,
    #             currency        = set_currency_id,
    #             link            = set_link,
    #             city_id         = set_city_id,
    #             company_id      = set_company_id,
    #             job_desc_id     = set_desc_id,
    #             job_website_id  = set_website_id
    #             )
    #         session.add(row)
    #         session.commit()
    #         return row.id
    #     else:
    #         return record.id

