from .db_connection      import session
from .tables.cities      import TableCity
from .tables.employers   import TableCompany
from .tables.description import TableDescription
from .tables.salary      import TableSalaryUSD
from .tables.salary      import TableSalaryAll
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
                table_salary_all   = TableSalaryAll,
                table_website      = TableWebsite,
                table_job          = TableJob
                 ):
        self.CITY           = table_city
        self.COMPANY        = table_company
        self.DESCRIPTION    = table_description
        self.SALARY_USD     = table_salary_usd
        self.SALARY_ALL     = table_salary_all
        self.WEBSITE        = table_website
        self.JOB            = table_job

    def get_city_id(self, city_name):
        city_name = city_name.title().strip()
        table     = session.query(self.CITY)
        record    = table.filter(self.CITY.city == city_name).first()

        if not record:
            new = self.CITY(
                city=city_name)
            session.add(new)
            session.commit()
            return new.id
        else:
            return record.id
    
    def get_company_id(self, company_id, company_name, company_link):
        table = session.query(self.COMPANY)
        record = table.filter(self.COMPANY.id == company_id).first()
        if not record:
            new = self.COMPANY(
                id      = company_id, 
                company = company_name, 
                link    = company_link)
            session.add(new)
            session.commit()
            return new.id
        else:
            return record.id
        
    def get_description_id(self, job_description):
        table = session.query(self.DESCRIPTION)
        record = table.filter(self.DESCRIPTION.job_desc == job_description).first()
        if not record:
            new = self.DESCRIPTION(job_desc=job_description)
            session.add(new)
            session.commit()
            return new.id
        else:
            return record.id

    def get_salary_usd(self, currency, salary_min, salary_max):
        if currency is None:
            return None, None
        
        if currency == 'USD':
            return salary_min, salary_max

        date    = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        table   = session.query(self.SALARY_USD)
        record  = table.filter(self.SALARY_USD.currency_from == currency).first()


        if record.currency_USD is None:
            converter   = Converter(from_currency=currency)
            to_usd      = converter.get_convert()
            # print(f'Current USD currency {record.currency_USD}')
            # print(f'For 1 {currency} in USD = {to_usd}')

            record.currency_USD = to_usd
            session.commit()
            USD = record.currency_USD
            # print(f"USD: {USD}")

        elif not record:
            # print(f'Currency {currency} not in database. Adding...')
            converter   = Converter(from_currency=currency)
            to_usd      = converter.get_convert()
            # print(f'For 1 {currency} in USD = {to_usd}')
            new = self.SALARY_USD(
                currency_from     = currency,
                currency_USD      = to_usd,
                convertation_date = date
                )
            session.add(new)
            session.commit()
            USD = new.currency_USD
            print(f'New currency {currency} added to database. USD = {USD}')
        else:
            USD = record.currency_USD
            print(f'Currency {currency} already in database. USD = {USD}')

        if record.convertation_date != date:
            converter   = Converter(from_currency=currency)
            to_usd      = converter.get_convert()
            record.currency_USD      = to_usd
            record.convertation_date = date
            session.commit()
            USD = record.currency_USD
            # print(f'Currency {currency} updated in database. USD = {USD}')

        
        salary_min_usd = None
        salary_max_usd = None

        # print(f"Salary min: {salary_min}, Salary max: {salary_max}")
        if salary_min is not None:
            salary_min_usd = round((USD * salary_min), 2)
        if salary_max is not None:
            salary_max_usd = round((USD * salary_max), 2)

        return salary_min_usd, salary_max_usd

    def get_original_salary_id(self, currency, salary_min, salary_max):
        if currency is None:
            return None
        new = self.SALARY_ALL(
            min_original = salary_min,
            max_original = salary_max,
            currency     = currency
            )
        session.add(new)
        session.commit()
        return new.id

    def get_website_id(self, website_url):
        table = session.query(self.WEBSITE)
        record = table.filter(self.WEBSITE.website == website_url).first()
        if not record:
            new = self.WEBSITE(website=website_url)
            session.add(new)
            session.commit()
            return new.id
        else:
            return record.id
        
    def add_job(self, 
            set_job_id,             set_job_title,      set_salary_min, set_salary_max,
            set_salary_original_id, set_job_link,       set_city_id,
            set_company_id,         set_description_id, set_website_id
            ):
        table = session.query(self.JOB)
        record = table.filter(self.JOB.job_id == set_job_id).first()
        if not record:
            new = self.JOB(
                job_id              = set_job_id,
                job_title           = set_job_title,
                salary_min          = set_salary_min,
                salary_max          = set_salary_max,
                id_original_salary  = set_salary_original_id,
                job_link            = set_job_link,
                id_city_name        = set_city_id,
                id_company_name     = set_company_id,
                id_description      = set_description_id,
                id_website          = set_website_id
                )
            session.add(new)
            session.commit()
            return new.id
        else:
            return record.id

    def check_job(self, job_id):
        table = session.query(self.JOB)
        record = table.filter(self.JOB.job_id == job_id).first()
        if not record:
            return False
        else:
            return True