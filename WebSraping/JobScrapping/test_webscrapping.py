from headhunter.scrapper_hh import ScrapperHeadHunter

args_hh = {'hh_query': 'Python', 'hh_page': 0, 'hh_type': 'title'}

hh = ScrapperHeadHunter(**args_hh)

job_cards = hh.get_job_cards()
print(type(job_cards))
print(job_cards)