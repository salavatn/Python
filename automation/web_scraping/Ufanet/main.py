from database   import session, Vacancy
from bs4        import BeautifulSoup
import requests
import time


url       = 'https://vkomandu.ufanet.ru/vacancy/ufa#vacancy2076'
content   = requests.get(url)
soup      = BeautifulSoup(content.text, 'html.parser')
vacancies = soup.find_all('div', class_='vacancies__item')

def get_title(vacancy):
    title = vacancy.find('div', class_='vacancy__title').text.strip()
    return title

def get_salary(vacancy):
    salary = vacancy.find('div', class_='vacancy__salary').text.strip()
    return salary

def get_paragraph(vacancy, message):
    desc_full = vacancy.find('div', class_='vacancy__desc vacancy__desc_full')
    title = desc_full.find('div', class_='vacancy__desc__title', string=message)
    p_desc = title.find_next('p')
    paragraph = p_desc.text.strip()

    while True:
        next_element = p_desc.find_next_sibling()
        if not next_element or next_element.name == 'div':
            break
        p_desc = next_element
        paragraph += f"\n{next_element.text.strip()}"
    return paragraph

def get_link(vacancy):
    desc_full = vacancy.find('div', class_='vacancy__desc__title vacancy__desc__title_first')
    link = desc_full.find_next_sibling('a').get('href')
    return link


for vacancy in vacancies: 
    job_title   = get_title(vacancy)
    job_salary  = get_salary(vacancy)
    job_tasks   = get_paragraph(vacancy, 'Чем Вы будете заниматься:')
    job_expect  = get_paragraph(vacancy, 'Мы ждём от Вас:')
    job_offer   = get_paragraph(vacancy, 'Мы предлагаем:')
    job_link    = get_link(vacancy)
    
    table = Vacancy(
        title=job_title,    
        salary=job_salary,  
        tasks=job_tasks,
        expect=job_expect,  
        offer=job_offer,    
        link=job_link)
    session.add(table)
    session.commit()
    time.sleep(1)
