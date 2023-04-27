from database.db_handler import HandlerDB
import datetime
db = HandlerDB()

my_city = "Нижний новгород  "
id_city = db.get_city_id(city_name=my_city)
print(f'City ID: {id_city}')




company_id = 2381
company_name = "Softline"
company_link = f'https://hh.ru/employer/{company_id}'

id_company = db.get_company_id(
    company_id=company_id,
    company_name=company_name,
    company_link=company_link)
print(f'Company ID: {id_company}')





description = "SOFTLINE ЯВЛЯЕТСЯ АККРЕДИТОВАННОЙ IT-КОМПАНИЕЙ О ПРОЕКТЕ:  «Инфосекьюрити» — специализированный сервис-провайдер, оказывающий услуги в сфере информационной безопасности, системной интеграции и консалтинга. Компания вышла на рынок в 2010 году и развивает не только ключевые сервисы, но и собственные разработки. С 2018 компания года входит в группу Softline. «Инфосекьюрити» является лицензиатом ФСБ России и ФСТЭК России. Бизнес-процессы компании построены в соответствии с международными практиками и стандартами. https://in4security.com  КЛЮЧЕВЫЕ ЗАДАЧИ:  Внедряет решения DLP у клиентов Компании по РФ. Решает инциденты, связанные с технической поддержкой клиентов Компании. Осуществляет написание технической документации, используя положения нормативных документов в области информационных технологий и защиты информации. Подготавливает документы для презентации и защиты решений перед Заказчиком. Актуализирует персональные сертификаты и профессиональные статусы в общей базе компании на корпоративном портале, используемой для подготовки к тендерам.  НАШИ ОЖИДАНИЯ:  Опыт работы c DLP (Infowatch, Solar Dozor, Zecurion, StaffCop, Гарда Предприятие, Стахановец, Symantec, Forcepoint) системами от года, наличие сертификата по решениям выше приветствуется. Понимание принципов проектной работы, подготовка документации на проект по внедрению DLP (ТЗ, ПМИ, ПЗ и т.д).  МЫ ПРЕДЛАГАЕМ:"

id_desc = db.get_description_id(job_description=description)
print(f'Description ID: {id_desc}')




salary_min = None
salary_max = 248000
currency = 'RUB'

min_usd, max_usd = db.get_salary_usd(
    currency=currency,
    salary_min=salary_min,
    salary_max=salary_max)

print(f'Salary USD: {min_usd} - {max_usd} USD')


original_salary_id = db.get_original_salary_id(
    currency    = currency,
    salary_min  = salary_min,
    salary_max  = salary_max
    )

print(f'Original Salary ID: {original_salary_id}')



website = 'https://hh.ru'
id_website = db.get_website_id(website_url=website)
print(f'Website ID: {id_website}')