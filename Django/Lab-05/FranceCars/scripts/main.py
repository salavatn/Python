from Automobiles.models import t_automobiles
from django.db.models import Q
# import F
from django.db.models import F

def run():
    pass    


car_list = [
    {'brand': 'Peugeot', 'model': '3008', 'year': 2019, 'color': 'White', 'price': 2000000, 'engine': '1.6 PureTech', 'vin': 'VF3RFE00V5E000000'},
    {'brand': 'Dodge', 'model': 'Ram', 'year': 2019, 'color': 'White', 'price': 2000000, 'engine': '1.6 PureTech', 'vin': 'VF3RFE00V5E000000'},
    {'brand': 'Peugeot', 'model': '3008', 'year': 2019, 'color': 'White', 'price': 2000000, 'engine': '1.6 PureTech', 'vin': 'VF3RFE00V5E000000'},
    {'brand': 'Renault', 'model': 'Arkana', 'year': 2019, 'color': 'Brown', 'price': 1350000, 'engine': '1.3 TCe', 'vin': 'VF1RFE00V5E000000'},
    {'brand': 'Audi', 'model': 'Q5', 'year': 2020, 'color': 'Black', 'price': 2500000, 'engine': '2.0 TFSI', 'vin': 'WAUZZZFYXJ1234567'},
    {'brand': 'BMW', 'model': '3 Series', 'year': 2021, 'color': 'Blue', 'price': 2800000, 'engine': '2.0 TwinPower Turbo', 'vin': 'WBA5R1C50M7C12345'},
    {'brand': 'Mercedes-Benz', 'model': 'GLE', 'year': 2022, 'color': 'Silver', 'price': 3500000, 'engine': '3.0L Inline-6 Turbo', 'vin': 'W1N0G8EB2LX123456'},
    {'brand': 'Toyota', 'model': 'Camry', 'year': 2021, 'color': 'Red', 'price': 1800000, 'engine': '2.5L Dynamic Force', 'vin': '4T1C11BKXLU123456'},
    {'brand': 'Honda', 'model': 'Civic', 'year': 2020, 'color': 'White', 'price': 1500000, 'engine': '1.5L Turbocharged', 'vin': '2HGFC1F31LH123456'},
    {'brand': 'Ford', 'model': 'Mustang', 'year': 2022, 'color': 'Yellow', 'price': 3200000, 'engine': '5.0L V8', 'vin': '1FA6P8CF6L1234567'},
    {'brand': 'Volkswagen', 'model': 'Passat', 'year': 2021, 'color': 'Gray', 'price': 1900000, 'engine': '2.0 TSI', 'vin': '1VWAA7A31LC123456'},
    {'brand': 'Nissan', 'model': 'Sentra', 'year': 2020, 'color': 'Black', 'price': 1400000, 'engine': '1.8L DOHC', 'vin': '3N1AB8CV5LY123456'},
    {'brand': 'Chevrolet', 'model': 'Optima', 'year': 2021, 'color': 'Silver', 'price': 1700000, 'engine': '1.6L Turbo', 'vin': '3GNKBKRSXJG123456'},
    {'brand': 'Hyundai', 'model': 'Elantra', 'year': 2022, 'color': 'White', 'price': 1600000, 'engine': '2.0L MPI', 'vin': '5NPD84LF7LH123456'},
    {'brand': 'Subaru', 'model': 'Legacy', 'year': 2021, 'color': 'Blue', 'price': 2000000, 'engine': '2.5L BOXER', 'vin': '4S3BWAN65M3000000'},
    {'brand': 'Kia', 'model': 'Forte', 'year': 2020, 'color': 'Red', 'price': 1500000, 'engine': '2.0L MPI', 'vin': '3KPF24AD0LE123456'}
]

for item in car_list:
    car = t_automobiles(**item)
    car.save()

'''
table = TableAutomobiles.objects
# query = table.filter(Q(Brand__startswith='K') | Q(Model__startswith='F')).values()
query_Kia = Q(Brand='Kia')
query_Mitsubishi = Q(Brand='Mitsubishi')
query_Dodge = Q(Brand='Dodge')

query = table.filter(query_Dodge | query_Mitsubishi)
print(*query.values())

'''




# table    = t_automobiles.objects

# q_color = Q(color='Brown') | Q(color='Yellow')

# query = table.filter(q_color)

# result   = query.values('brand', 'model', 'color', 'year')

# sql_query = result.query

# print(sql_query)

# for item in result:
#     print(item)



# # Example Queries
# q_color = Q(Color__contains='w')        # Case Sensitive                 - white, Yellow, Brown 
# q_color = Q(Color__icontains='w')       # Case Insensitive               - white, White, BROWN, yellow
# q_color = Q(Color__startswith='Bl')     # Case Sensitive & Starts With   - Black, Blue
# q_color = Q(Color__istartswith='w')     # Case Insensitive & Starts With - white, White
# q_color = Q(Color__iexact='white')      # Case Insensitive & Exact       - white, White  
# q_color = Q(Color__endswith='e')        # Case Sensitive & Ends With     - White, Blue
# q_color = Q(Color__iendswith='e')       # Case Insensitive & Ends With   - WHITE, white, BLUE, blue, E, e
# q_color = Q(Color__regex=r'^(Wh|Bl)')   # Case Sensitive & Regex         - White, Blue, Black
# q_color = Q(Color__iregex=r'^(Wh|Bl)')  # Case Insensitive & Regex       - White, white, BLUE, blue, Black, black

# q_year  = Q(Year__gt=2019)              # Greater Than          - 2020, 2021, 2022
# q_year  = Q(Year__gte=2019)             # Greater Than or Equal - 2019, 2020, 2021, 2022
# q_year  = Q(Year__lt=2020)              # Less Than             - 2019
# q_year  = Q(Year__lte=2020)             # Less Than or Equal    - 2020, 2019
# q_year  = Q(Year__range=(2019, 2021))   # Range                 - 2019, 2020, 2021
# q_year  = Q(Year__in=[2019, 2020, 2021])# In                    - 2019, 2020, 2021
# q_year  = Q(Year__isnull=True)          # Is Null               - None
# q_year  = Q(Year__isnull=False)         # Is Not Null           - 2019, 2020, 2021, 2022
# q_year  = Q(Year__exact=2019)           # Exact                 - 2019

# q_year  = Q(Year=2019)                  # Exact                 - 2019
# q_year  = Q(Year=2019) | Q(Year=2020)   # OR                    - 2019 or 2020


# q_color = Q(Color='White') | Q(Color='Black')   # OR        - White or Black
# q_query = Q(Color='White') & Q(Year=2019)       # AND       - White and 2019
# q_query = ~Q(Color='White')                     # NOT       - Not White
# q_query = ~Q(Color='White') & Q(Year=2019)      # NOT AND   - Not White and 2019
# q_color = ~(Q(Color='White') | Q(Color='Black'))# NOT       - Not (White or Black)
