from ..models import t_auto
from django.db.models import F, Q

def run():
    pass


table = t_auto.objects
q_year = Q(year=2019)
f_price = F('price')*0.85
# query = table.filter(q_year).values('brand', 'model', 'year', 'price', 'discounted_price', discounted_price=f_price)
# update = table.filter(q_year).update(price=f_price)

# print(update.query)
# for item in update:
#     print(item)


methods = dir(table)
for method in methods:
    print(method)
