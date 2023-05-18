from faker  import Faker
from bs4    import BeautifulSoup
from typing import List, Dict, Union, Optional, Any, Tuple, Callable, TypeVar, Generic, Sequence, Iterable, Mapping, Set, Deque, Iterator, NamedTuple, overload, cast, no_type_check
import requests
import re
import logging
import logging.config

import datetime
import locale

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


fake = Faker()

class ScrapperHeadHunter:
    # print('ScrapperHeadHunter')
    def __init__(self, query: str, page=0, type='all') -> None:
        # print('ScrapperHeadHunter.__init__')
        self.type     = type
        self.keywords = query
        self.page     = page

        if self.type == 'title':
            self.url = f'https://hh.ru/search/vacancy?search_field=name&enable_snippets=true&text={self.keywords}&page={self.page}'
        elif self.type == 'subject':
            self.url = f'https://hh.ru/search/vacancy?search_field=description&enable_snippets=true&text={self.keywords}&page={self.page}'
        else: # self.type == 'all':
            self.url  = f'https://hh.ru/search/vacancy?text={self.keywords}&page={self.page}'


    def get_job_cards(self) -> List[BeautifulSoup]:
        # print('ScrapperHeadHunter.get_job_cards')
        '''ALL JOB CARDS'''
        try:
            headers     = {'User-Agent': fake.user_agent()}
            response    = requests.get(self.url, headers=headers).content
            full_html   = BeautifulSoup(response, 'html.parser')
            jobs_block  = full_html.find('main', {'class': 'vacancy-serp-content'})        
            job_cards   = jobs_block.find_all('div', {'class': 'serp-item'})
            return job_cards
        except AttributeError:
            return None


    def get_job_title(self, job_card: BeautifulSoup) -> str:
        # print('ScrapperHeadHunter.get_job_title')
        '''JOB TITLE'''
        title = job_card.find('a', {'data-qa': 'serp-item__title'}).text.strip()
        return title


    def get_job_id(self, job_card: BeautifulSoup) -> Optional[int]:
        '''JOB ID'''
        url = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        id  = int(url.split('?')[0].split('/')[-1])
        return id


    def get_job_salary(self, job_card: BeautifulSoup) -> Tuple[Optional[int], Optional[int], Optional[str]]:
        '''SALARY'''
        try:
            salary = job_card.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text.strip()
            salary = salary.replace(" ", "")
            salary = salary.replace("\n", " ")
            salary = re.sub(r'\s+', ' ', salary)
            salary = salary.split(" ")
        except AttributeError:
            return None, None, None

        salarymin, salarymax, job_currency = None, None, None 
        
        if "от"   in salary:
            salarymin = salary[1]
            if salarymin.isdigit(): salarymin = int(salarymin)
        elif "до" in salary:
            salarymax = salary[1]
            if salarymax.isdigit(): salarymax = int(salarymax)
        elif "–"  in salary:
            salarymin = salary[0]
            salarymax = salary[2]
            if salarymin.isdigit(): salarymin = int(salarymin)
            if salarymax.isdigit(): salarymax = int(salarymax)
        
        if "руб." in salary:   job_currency = "RUB"
        if "сум" in salary:    job_currency = "UZS"
        if "USD" in salary:    job_currency = "USD"
        if "EUR" in salary:    job_currency = "EUR"
        if "KZT" in salary:    job_currency = "KZT"

        return salarymin, salarymax, job_currency


    def get_job_city(self, job_card: BeautifulSoup) -> Optional[str]:
        '''CITY'''
        city = job_card.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text.strip()
        city = list(city.split(','))[0].strip()
        return city


    def get_job_link(self, job_card: BeautifulSoup) -> str:
        '''URL LINK'''
        link = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        link = link.split('?')[0].strip()
        return link


    def get_job_source(self, job_card: BeautifulSoup) -> str:
        '''JOB SOURCE'''
        source = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        source = source.split('vacancy/')[0].strip()
        return source


    def get_job_desc(self, job_link: str) -> Optional[str]:
        '''JOB DESCRIPTION'''
        headers    = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response   = requests.get(job_link, headers=headers)
        if response.status_code == 200:
            html = response.text
        else:
            return None
        soup = BeautifulSoup(html, 'html.parser')
        job_desc = soup.find('div', {'data-qa': 'vacancy-description'}).text.strip()
        return job_desc


    def get_company_id(self, job_card: BeautifulSoup) -> Optional[int]:
        '''COMPANY ID'''
        company_id = job_card.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})['href']
        company_id = company_id.split('?')[0].split('/')[-1]
        if company_id.isdigit(): company_id = int(company_id)
        return company_id


    def get_company_name(self, job_card: BeautifulSoup) -> Optional[str]:
        '''COMPANY NAME'''
        company_name = job_card.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text.strip()
        company_name = company_name.replace('\n', '').split(',')[0].strip()
        # company_name = company_name.split(',')[0].strip()
        company_name = re.sub(r'\s+', ' ', company_name)
        return company_name


    def get_job_posted(self, job_link: str) -> Optional[str]:
        '''DATE POSTED'''
        headers     = {'User-Agent': fake.user_agent()}
        response   = requests.get(job_link, headers=headers)
        if response.status_code == 200:
            html = response.content
        else:
            return None
        full_html = BeautifulSoup(html, 'html.parser')
        job_published = full_html.find('p', {'class': 'vacancy-creation-time-redesigned'})
        if job_published is None:
            job_published = full_html.find('p', {'class': 'vacancy-creation-time'})
            logger.debug(f'ScrapperHH.published: Used old style class="vacancy-creation-time"')
        job_published = job_published.text.strip()
        logger.debug(f'ScrapperHH.published: {job_published}')
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        date_string = job_published.split('опубликована ')[1].split(' в ')[0].strip() # 12 июля 2021
        date = datetime.datetime.strptime(date_string, '%d %B %Y')
        date_only = date.date()
        return date_only
