import os
import django
import time
import logging
import logging.config
from app_webscrapping.scrapper_hh import ScrapperHeadHunter

# Import Q from django.db.models
from django.db.models import Q


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

logger.debug('FILE: handler_db.py')


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


    def set_location(self, city: str, country: str) -> int:
        '''Table LOCATION: add City and return ID'''
        logger.debug(f'HandlerDB.location: City={city}; Country={country};')
        
        table = self.location.objects.filter(city=city).first()

        if table:
            logger.debug(f'HandlerDB.location: Exist in Database;')
        else:
            data  = {'city': city, 'country': country}
            table = self.location(**data)
            table.save()
            logger.debug(f'HandlerDB.location: Added to Database;')
        
        return table.id
            

    def set_company(self, company: str, city: str, link: int) -> int:
        '''Table COMPANIES: add Company and return ID'''

        logger.debug(f'HandlerDB.company: Company={company}; City={city}; URL={link};')

        city_id = self.location.objects.filter(city=city).first()
        # q_filter = Q(company=company) & Q(city=city)
        table = self.company.objects.filter(company=company).first()

        if table:
            logger.debug(f'HandlerDB.company: Exist in Database;')
        else:
            data  = {'company': company, 'city': city_id, 'link': link}
            table = self.company(**data)
            table.save()
            logger.debug(f'HandlerDB.company: Added to Database;')

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
            

    def get_usd_salary(self, currency: str, minimum:int, maximum:int) -> Tuple[Optional[float], Optional[float]]: 
        '''Table CURRENCIES: add Currency and return ID'''
        
        # Checking #1: If currency is None, return None, None
        if currency is None:
            logger.debug(f'HandlerDB.currency: Current={currency}; Min={minimum}; Max={maximum};')
            # logger.debug(f'Currency is None. Minimum: {minimum}, Maximum: {maximum}')
            return None, None
        
        date  = datetime.datetime.now().strftime('%Y-%m-%d')
        table = self.currencies.objects.filter(currency=currency).first()

        # Checking #2: If currency is USD, return Min, Max
        if currency == 'USD':    
            logger.debug(f'HandlerDB.currency: Current={currency}; Min={minimum}; Max={maximum};')
            return minimum, maximum

        # Checking #3: If currency is not USD, convert to USD
        if not table:
            converter    = Converter(currency=currency)
            from_to_usd  = converter.get_convert()
            data  = {'currency': currency, 'usd': from_to_usd, 'date': date}
            table = self.currencies(**data)
            table.save()
            logger.debug(f'HandlerDB.currency: Convering; 1 {currency} = {from_to_usd} USD;')
        else:
            from_to_usd = table.usd
            # logger.debug(f'HandlerDB.currency: Current={currency}; Min={minimum}; Max={maximum};')
            logger.debug(f'HandlerDB.currency: Exist in database; 1 {currency} = {from_to_usd} USD;')

        # # Checking #4: If date is not today, update currency
        # if table.date.strftime('%Y-%m-%d') != date:
        #     converter    = Converter(currency=currency)
        #     from_to_usd  = converter.get_convert()
        #     table.usd    = from_to_usd
        #     table.date   = date
        #     table.save()
        #     logger.debug(f'Currency {currency} updated in database. USD = {from_to_usd}')

        logger.debug(f'HandlerDB.currency: Current={currency}; Min={minimum}; Max={maximum};')

        if minimum is not None: 
            # logger.debug(f'HandlerDB.currency: Min {minimum} {currency} to USD;')
            minimum = round((from_to_usd * minimum), 2)


        if maximum is not None: 
            # logger.debug(f'HandlerDB.currency: Max {maximum} {currency} to USD;')
            maximum = round((from_to_usd * maximum), 2)

        logger.debug(f'HandlerDB.currency: Current=USD; Min={minimum}; Max={maximum};')


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

