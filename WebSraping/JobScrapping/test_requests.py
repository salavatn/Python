from bs4 import BeautifulSoup
import requests
from faker import Faker

fake = Faker()



class ScrapperHeadHunter:
    def __init__(self, hh_query, hh_page=0):
        self.keywords = hh_query
        self.page = hh_page
    
    def get_job_cards(self):
        url  = f'https://hh.ru/search/vacancy?text={self.keywords}&page={self.page}'
        print(f"URL:   \t{url}")
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        headers = {'User-Agent': fake.user_agent()}
        response = requests.get(url, headers=headers).content
        full_html = BeautifulSoup(response, 'html.parser')

        jobs_block = full_html.find('main', {'class': 'vacancy-serp-content'})
        if jobs_block is None:
            print(f"Jobs_block is None")
            return None
        job_cards  = jobs_block.find_all('div', {'class': 'serp-item'})
        return job_cards

    def get_job_link(self, job_card):
        try:
            link = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
            print(f"Link:   \t{link}")
            link = link.split('?')[0].strip()
            print(f"Link:    \t{link}")
        except:
            print(f"Link is None")
            return None
        return link

    def get_job_source(self, job_card):
        try:
            source = job_card.find('a', {'data-qa': 'serp-item__title'})['href']
            print(f"Source1:    \t{source}")
            source = source.split('vacancy/')[0].strip()
            print(f"Source2:    \t{source}")
        except:
            print(f"L43, source is None")
            return None
        return source


hh = ScrapperHeadHunter('python')
job_cards = hh.get_job_cards()
job_link = hh.get_job_link(job_cards[0])
job_source = hh.get_job_source(job_cards[0])
