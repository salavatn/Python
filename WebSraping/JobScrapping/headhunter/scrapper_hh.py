from bs4 import BeautifulSoup
import requests
# import time
import re
from faker import Faker

fake = Faker()



class ScrapperHeadHunter:
    def __init__(self, hh_query, hh_page=0, hh_type='all'):
        self.type     = hh_type
        self.keywords   = hh_query
        self.page       = hh_page
    
    def get_job_cards(self):
        if self.type == 'title':
            url = f'https://hh.ru/search/vacancy?search_field=name&enable_snippets=true&text={self.keywords}&page={self.page}'
        elif self.type == 'subject':
            url = f'https://hh.ru/search/vacancy?search_field=description&enable_snippets=true&text={self.keywords}&page={self.page}'
        elif self.type == 'all':
            url  = f'https://hh.ru/search/vacancy?text={self.keywords}&page={self.page}'
        
        print(f"URL:\t{url}")

        headers     = {'User-Agent': fake.user_agent()}
        response    = requests.get(url, headers=headers).content
        full_html   = BeautifulSoup(response, 'html.parser')
        jobs_block  = full_html.find('main', {'class': 'vacancy-serp-content'})
        if jobs_block is None:
            return None
        job_cards  = jobs_block.find_all('div', {'class': 'serp-item'})
        return job_cards

    def get_job_title(self, job_card):
        try:
            title = job_card.find('a', {'data-qa': 'serp-item__title'}).text.strip()
        except:
            return None
        return title

    def get_job_id(self, job_card):
        try:
            url     = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
            # print(f"URL:\t{url}")
            job_id  = url.split('?')[0].split('/')[-1]
            if job_id.isdigit(): 
                job_id = int(job_id)
            # print(f"Job ID:\t{job_id}")
        except:
            return None
        
        return job_id

    def get_job_salary(self, job_card):
        try:
            salary = job_card.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text.strip()
            salary = salary.replace(" ", "")
            salary = salary.replace("\n", " ")
            salary = re.sub(r'\s+', ' ', salary)
            salary = salary.split(" ")
            
        except:
            return None, None, None

        salarymin, salarymax, job_currency = None, None, None  # инициализация переменных
        
        if "от" in salary:
            salarymin = salary[1]
            if salarymin.isdigit(): salarymin = int(salarymin)
        elif "до" in salary:
            salarymax = salary[1]
            if salarymax.isdigit(): salarymax = int(salarymax)
        elif "–" in salary:
            salarymin = salary[0]
            salarymax = salary[2]
            if salarymin.isdigit(): salarymin = int(salarymin)
            if salarymax.isdigit(): salarymax = int(salarymax)
        
        if "руб." in salary:   job_currency = "RUB"
        if "USD" in salary:    job_currency = "USD"
        if "EUR" in salary:    job_currency = "EUR"
        if "KZT" in salary:    job_currency = "KZT"

        return salarymin, salarymax, job_currency

    def get_job_city(self, job_card):
        try:
            city = job_card.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text.strip()
            city = list(city.split(','))[0].strip()
        except:
            return None
        return city

    def get_job_link(self, job_card):
        try:
            link = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
            link = link.split('?')[0].strip()
        except:
            return None
        return link

    def get_job_source(self, job_card):
        try:
            source = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
            source = source.split('vacancy/')[0].strip()
        except:
            return None
        return source

    def get_job_desc(self, job_link):
        try:
            headers    = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response   = requests.get(job_link, headers=headers)
            if response.status_code == 200:
                html = response.text
            else:
                return None
            soup = BeautifulSoup(html, 'html.parser')
            job_desc = soup.find('div', {'data-qa': 'vacancy-description'}).text.strip()
        except:
            return None
        return job_desc

    def get_company_id(self, job_card):
        try:
            company_id = job_card.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})['href']
            company_id = company_id.split('?')[0].split('/')[-1]
            if company_id.isdigit(): company_id = int(company_id)
        except:
            return None
        return company_id

    def get_company_name(self, job_card):
        try:
            company_name = job_card.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text.strip()
            company_name = company_name.replace('\n', '')
            company_name = company_name.split(',')[0].strip()
            company_name = re.sub(r'\s+', ' ', company_name)
        except:
            return None
        return company_name



