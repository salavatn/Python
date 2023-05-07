from .db_connection      import session
from .tables.cities      import TableCity
from .tables.companies   import TableCompany 
from .tables.description import TableDescription
from .tables.salary      import TableSalaryUSD
from .tables.website     import TableWebsite
from .tables.jobs        import TableJob
from converter           import Converter
import datetime



class HandlerDB:
    def __init__(self,
                table_city         = TableCity,
                table_company      = TableCompany,
                table_description  = TableDescription,
                table_salary_usd   = TableSalaryUSD,
                table_website      = TableWebsite,
                table_job          = TableJob
                 ):
        self.CITY           = table_city
        self.COMPANY        = table_company
        self.DESCRIPTION    = table_description
        self.SALARY_USD     = table_salary_usd
        self.WEBSITE        = table_website
        self.JOB            = table_job

    def get_city_id(self, set_city):
        set_city  = set_city.title().strip()
        table     = session.query(self.CITY)
        record    = table.filter(self.CITY.name == set_city).first()

        if not record:
            row = self.CITY(name=set_city)
            session.add(row)
            session.commit()
            return row.id
        
        return record.id
    
    def get_company_id(self, set_id, set_name, set_link):
        table = session.query(self.COMPANY)
        record = table.filter(self.COMPANY.company_id == set_id).first()

        if not record:
            row = self.COMPANY(company_id=set_id, name=set_name, link=set_link)
            session.add(row)
            session.commit()
            return row.id
        
        return record.id
        
    def get_job_desc_id(self, set_description):
        table = session.query(self.DESCRIPTION)
        record = table.filter(self.DESCRIPTION.text == set_description).first()

        if not record:
            row = self.DESCRIPTION(text=set_description)
            session.add(row)
            session.commit()
            return row.id
        
        return record.id

    def get_salary_usd(self, set_from, set_min, set_max):
        if set_from is None:
            return None, None
    
        date    = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        table   = session.query(self.SALARY_USD)
        record  = table.filter(self.SALARY_USD.currency == set_from).first()

        if not record:
            if set_from == 'USD':
                row = self.SALARY_USD(currency='USD', usd=1, date=date)
                session.add(row)
                session.commit()
                USD = row.usd
                print(f'{set_from} added to database. USD = {USD}')
                return set_min, set_max
            
            converter   = Converter(from_currency=set_from)
            to_usd      = converter.get_convert()
            row         = self.SALARY_USD(currency=set_from, usd=to_usd, date=date)
            session.add(row)
            session.commit()
            USD = row.usd
            print(f'New currency {set_from} added to database. USD = {USD}')
        else:
            USD = record.usd
            print(f'Currency {set_from} already in database. USD = {USD}')

        if set_min is not None:
            set_min = round((USD * set_min), 2)
        else:
            set_min = None

        if set_max is not None:
            set_max = round((USD * set_max), 2)
        else:
            set_max = None

        return set_min, set_max

    def get_currency_id(self, set_currency):
        if set_currency is None:
            return None
        
        table   = session.query(self.SALARY_USD)
        record  = table.filter(self.SALARY_USD.currency == set_currency).first()

        if not record:
            row = self.SALARY_USD(currency=set_currency)
            session.add(row)
            session.commit()
            return row.id
        
        return record.id

    def get_website_id(self, set_url):
        table   = session.query(self.WEBSITE)
        record  = table.filter(self.WEBSITE.url == set_url).first()

        if not record:
            row = self.WEBSITE(url=set_url)
            session.add(row)
            session.commit()
            return row.id
        
        return record.id
        
    def add_job(self, set_id, set_title, set_link, set_min, set_max, set_usd_min, set_usd_max,
                      set_currency_id, set_city_id, set_company_id, set_desc_id, set_website_id):
        table = session.query(self.JOB)
        record = table.filter(self.JOB.job_id == set_id).first()
        if not record:
            row = self.JOB(
                job_id          = set_id,
                title           = set_title,
                usd_min         = set_usd_min,
                usd_max         = set_usd_max,
                current_min     = set_min,
                current_max     = set_max,
                currency        = set_currency_id,
                link            = set_link,
                city_id         = set_city_id,
                company_id      = set_company_id,
                job_desc_id     = set_desc_id,
                job_website_id  = set_website_id
                )
            session.add(row)
            session.commit()
            return row.id
        else:
            return record.id

    def check_job(self, check_id):
        table   = session.query(self.JOB)
        record  = table.filter(self.JOB.job_id == check_id).first()
        if not record:
            return False
        else:
            return True

'''
# Обратить внимание:
# command exeption
# Type Hint

# Lib Typing
from typing import Optional, List, Dict, Tuple, Union, Any, Callable, TypeVar, Generic, Type, cast, overload

def fn() -> List[int]:
    pass

Optional[int] # Union[int, None]
# Callable

# ООП
'''

