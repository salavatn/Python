from bs4 import BeautifulSoup
import requests
import time


class HeadHunter:
    def __init__(self, keywords, page=0):
        # Поиск по всем параметрам
        self.url  = f'https://hh.ru/search/vacancy?text={keywords}&page={page}'
        
        # self.url  = f'https://hh.ru/search/vacancy?search_field=name&enable_snippets=true&text={keywords}&page={page}'

    def get_job_cards(self):
        headers    = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response   = requests.get(self.url, headers=headers)
        content    = response.content
        full_html  = BeautifulSoup(content, 'html.parser')   # Получаем весь HTML код страницы
        jobs_block = full_html.find('main', {'class': 'vacancy-serp-content'})
        job_cards  = jobs_block.find_all('div', {'class': 'serp-item'})
        self.html  = full_html
        # vacancies_cards = vacancies_block.find_all('div', {'data-qa': 'vacancy-serp__vacancy'})
        return job_cards

    def get_vacancy_title(self, job_card):
        title = job_card.find('a', {'data-qa': 'serp-item__title'}).text
        return title
        # Tag <a>: 
        #   class="serp-item__title" 
        #   data-qa="serp-item__title" 
        #   target="_blank" 
        #   href="https://hh.ru/analytics_source/vacancy/79675546?from=vacancy_search_list&amp;query=Python&amp;r">
        # 
        # Text: Программист Python (Junior)

    def get_vacancy_id(self, job_card):
        url = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        vacancy_id = url.split('?')[0].split('/')[-1]
        return vacancy_id
        # Tag <a>: 
        #   href="https://hh.ru/analytics_source/vacancy/79675546?from=vacancy_searc

    def get_vacancy_salary(self, job_card):
        try:
            salary = job_card.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text
        except:
            salary = None
        return salary
        #     # Получаем зарплату вакансии
        #     # до 110 000 руб.
        #     # 1 000 – 2 000 <!-, -->USD
        #     # 50 000 – 90 000 <!-, -->руб.

    def get_employer_id(self, job_card):
        employer_url = job_card.find('a', {'class': 'bloko-link bloko-link_kind-tertiary'})['href']
        employer_url = employer_url.split('?')[0]
        employer_id = employer_url.split('/')[-1]
        return employer_id
        # Получаем ID компании работодателя
        # <a 
        #   data-qa="vacancy-serp__vacancy-employer" 
        #   class="bloko-link bloko-link_kind-tertiary" 
        #   href="/employer/5451293?hhtmFrom=vacancy_search_list">
        #       Раздоров и Компания
        # /employer/1156409
        # </a>

    def get_vacancy_city(self, job_card):
        return job_card.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
        # Получаем адрес вакансии
        # <div data-qa="vacancy-serp__vacancy-address" class="bloko-text">Ростов-на-Дону</div>

    def get_vacancy_link(self, job_card):
        link = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        self.link = link.split('?')[0]
        # print(f"Vacancy link: {self.link}")
        return self.link
        # Получаем ссылку на вакансию

    def get_vacancy_desc(self, job_link):
        headers   = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response  = requests.get(job_link, headers=headers)
        content   = response.content
        vacancy   = BeautifulSoup(content, 'html.parser')
        desc      = vacancy.find('div', {'data-qa': 'vacancy-description'}).text
        if desc == '':
            desc = None
        return desc
        # Получаем описание вакансии

    def get_page_count(self):
        headers    = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response   = requests.get(self.url, headers=headers)
        content    = response.content
        full_html  = BeautifulSoup(content, 'html.parser')
        try:
            count = int(full_html.find_all('a', {'data-qa': 'pager-page'})[-1].text) - 1
        except:
            count = 0
        return count
