from bs4 import BeautifulSoup
import requests
import time
import re


def get_job_title(job_card):
    # Получаем название вакансии
    try:
        title = job_card.find('a', {'data-qa': 'serp-item__title'}).text.strip()
    except:
        title = None
    return title

def get_job_id(job_card):
    # Получаем ID вакансии
    try:
        url     = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        job_id  = url.split('?')[0].split('/')[-1]
    except:
        job_id = None
    return int(job_id)

def get_job_salary(job_card):
    try:
        salary = job_card.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text.strip()
        # print(f"Line 27. Salary: {salary}")
        salary = salary.replace(" ", "")
        # print(f"Line 30. Salary: {salary}")
        salary = salary.replace("\n", " ")
        # print(f"Line 33. Salary: {salary}")
        salary = re.sub(r'\s+', ' ', salary)
        # print(f"Line 36. Salary: {salary}")
        salary = salary.split(" ")
        # print(f"Line 59. Salary: {salary}")
    except:
        return None, None, None

    salarymin, salarymax, job_currency = None, None, None  # инициализация переменных
    
    if "от" in salary: # or salary[0].find("от") != -1:
        # print(f"ELIF - ОТ")
        salarymin = salary[1]
        if salarymin.isdigit(): salarymin = int(salarymin)
        # print(f"SalaryMin: {salarymin}")
        # print(f"SalaryMax: {salarymax}")
        

    elif "до" in salary: # or salary[0].find("до") != -1:
        # print(f"ELIF - ДО")
        salarymax = salary[1]
        if salarymax.isdigit(): salarymax = int(salarymax)
        # print(f"SalaryMin: {salarymin}")
        # print(f"SalaryMax: {salarymax}")


    elif "–" in salary: # or salary[0].find("–") != -1:
        # print(f"ELIF - Диапазон")
        salarymin = salary[0]
        salarymax = salary[2]
        if salarymin.isdigit(): salarymin = int(salarymin)
        if salarymax.isdigit(): salarymax = int(salarymax)
        # print(f"SalaryMin: {salarymin}")
        # print(f"SalaryMax: {salarymax}")


    if "руб." in salary:   job_currency = "RUB"
    if "USD" in salary:    job_currency = "USD"
    if "EUR" in salary:    job_currency = "EUR"
    if "KZT" in salary:    job_currency = "KZT"
    # print("Currency: ", job_currency)
    return salarymin, salarymax, job_currency

def get_job_city(job_card):
    # Получаем город, в котором находится вакансия
    try:
        city = job_card.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text.strip()
        city = list(city.split(' '))[0].strip()
    except:
        return None
    return city

def get_job_link(job_card):
    # Получаем ссылку формата: https://hh.ru/vacancy/12345678
    try:
        link = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        link = link.split('?')[0].strip()
    except:
        return None
    return link

def get_job_source(job_card):
    # Эта функция возможно не нужна, так как мы скрапим только с hh.ru
    try:
        source = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
        source = source.split('vacancy/')[0].strip()
    except:
        return None
    return source

def get_job_desc(job_link):
    # Получаем описание вакансии
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

def get_company_id(job_card):
    # Получаем ID компании
    try:
        company_id = job_card.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})['href']
        company_id = company_id.split('?')[0].split('/')[-1]
    except:
        return None
    return int(company_id)


def get_company_name(job_card):
    # Получаем название компании
    try:
        company_name = job_card.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text.strip()
        company_name = company_name.replace('\n', '')
        # print(f"Original:    \t{company_name}")
        company_name = company_name.split(',')[0].strip()
        # print(f"Remove , :\t{company_name}")

        company_name = re.sub(r'\s+', ' ', company_name)
        # print(f"Company name: \t{company_name}")

    except:
        return None
    return company_name
    # <span class="company-header-title-name" data-qa="company-header-title-name">
    # Ассоциация Когнитивно-Поведенческой Психотерапии<!-- --> </span>

# =================
with open('hh.html', 'r', encoding='utf-8') as f:
    content = f.read()

full_html  = BeautifulSoup(content, 'html.parser')

job_page = full_html.find('main', {'class': 'vacancy-serp-content'})
job_cards  = job_page.find_all('div', {'class': 'serp-item'})

count = 1
for card in job_cards:

# =================

# with open('card.html', 'r', encoding='utf-8') as file:
#     content = file.read()

# card = BeautifulSoup(content, 'html.parser')

# =================
    print(f"\n\n\n=============================================== Job #{count}")
    # job_title = get_job_title(card)
    # print(f"\n\n\nJob Title:  {job_title}")
    # job_id    = get_job_id(card)
    # print(f"Job ID:     {job_id}")
    # salary_min, salary_max, currency = get_job_salary(card)
    # print(f"Salary min: {salary_min}")
    # print(f"Salary max: {salary_max}")
    # print(f"Currency:   {currency}")
    # job_city  = get_job_city(card)
    # print(f"City:       {job_city}")
    # job_link = get_job_link(card)
    # print(f"Link:       {job_link}")
    # job_source = get_job_source(card)
    # job_desc  = get_job_desc(job_link)    # Большой объем данных
    company_id = get_company_id(card)
    print(f"Company ID: \t{company_id}")
    company_name = get_company_name(card)
    print(f"Company name: \t{company_name}")


# print(f"Job Title:  {job_title}")
# print(f"Job ID:     {job_id}")
# print(f"Salary min: {salary_min}")
# print(f"Salary max: {salary_max}")
# print(f"Currency:   {currency}")
# print(f"City:       {job_city}")
# print(f"Link:       {job_link}")
# print(f"Source:     {job_source}")
# print(f"Company ID: {company_id}\n\n")
# print(f"Description:\n{job_desc}")

    time.sleep(1)



# result = card
# with open('card_result.html', 'w', encoding='utf-8') as file:
#     file.write(result.prettify())

    count += 1
    
    # if count > 15:
    #     break

