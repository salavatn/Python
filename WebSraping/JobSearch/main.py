import requests
from bs4 import BeautifulSoup
from table import TableVacancies, TableFullVacancyDesc
from database import session
import time

db_table = TableVacancies

def html_parsing(url):
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    content  = response.content
    return BeautifulSoup(content, 'html.parser')

def get_vacancy_name(html):
    name = html.find('a', {'class': 'serp-item__title'}).text
    return name

def get_vacancy_salary(html):
    try:
        # salary = html.find('span', {'class': 'bloko-header-section-3'}).text
        salary = html.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text
        # print(f"SALARY: \t {salary}")
    except:
        salary = None
    return salary
    # от <!-- -->60 000<!-- --> <!-- -->руб.
    # до 110 000 руб.
    # 1 000 – 2 000 <!-- -->USD
    # 50 000 – 90 000 <!-- -->руб.

def get_vacancy_employer(html):
    return html.find('a', {'class': 'bloko-link bloko-link_kind-tertiary'}).text

def get_vacancy_address(html):
    return html.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text

def get_vacancy_link(html):
    link = html.find('a', {'data-qa': 'serp-item__title'})['href']
    link = link.split('?')[0]
    return link

def get_page_count(soup):
    try:
        count = int(soup.find_all('a', {'data-qa': 'pager-page'})[-1].text) - 1
    except:
        count = 0
    return count

def read_vacancies(vacancies_cards):
    # print("\n\nSTART READING VACANCIES")
    count = 1
    for card in vacancies_cards:
        vacancy_name     = get_vacancy_name(card)       # Python-разработчик (Junior)
        vacancy_salary   = get_vacancy_salary(card)     # от 100 000 руб.
        vacancy_employer = get_vacancy_employer(card)   # ООО «СКБ Контур»
        vacancy_address  = get_vacancy_address(card)    # Москва, Ленинградский проспект, 15с1
        vacancy_link     = get_vacancy_link(card)       # https://hh.ru/vacancy/37288389?query=Junior%20Python
        keywords         = hh_text

        row = db_table(
            keyword=keywords,
            title=vacancy_name, 
            salary=vacancy_salary, 
            employer=vacancy_employer, 
            address=vacancy_address, 
            link=vacancy_link)
        session.add(row)
        session.commit()

        print(f"Vacancy number:  \t{count}")
        print(f"Vacancy name:    \t{vacancy_name}")
        print(f"Vacancy salary:  \t{vacancy_salary}")
        print(f"Vacancy employer:\t{vacancy_employer}")
        print(f"Vacancy address: \t{vacancy_address}")
        print(f"Vacancy link:    \t{vacancy_link}\n\n\n")

        time.sleep(2)

        count += 1

user_input = input("Введите запрос: ")
query = '+'.join(user_input.split())


hh_page = 0
hh_text = query #'Forcepoint'
hh_url  = 'https://hh.ru/search/vacancy?text=' + hh_text + '&page=' + str(hh_page)
soup    = html_parsing(hh_url)

pages_count     =  get_page_count(soup)
vacancies_block  = soup.find('main', {'class': 'vacancy-serp-content'})
vacancies_cards = vacancies_block.find_all('div', {'class': 'serp-item'})

# print(f"Pages count:\t{pages_count}")
# print(f"URL address:\t{hh_url}")

for page in range(0, pages_count+1):
    # print(f"START READING PAGE: {page}")
    hh_page = page
    hh_url  = 'https://hh.ru/search/vacancy?text=' + hh_text + '&page=' + str(hh_page)
    # print(f"URL: {hh_url}")
    soup    = html_parsing(hh_url)
    vacancies_block = soup.find('main', {'class': 'vacancy-serp-content'})
    vacancies_cards = vacancies_block.find_all('div', {'class': 'serp-item'})
    read_vacancies(vacancies_cards)
