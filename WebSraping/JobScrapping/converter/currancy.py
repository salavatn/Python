from dotenv import load_dotenv
import requests
import os

load_dotenv(dotenv_path='.env_api')
app_id = os.getenv('YOUR_API_ID')


class Converter:
    def __init__(self, from_currency = 'RUB'):
        self.FROM  = from_currency
        self.TO    = 'USD'

    def get_convert(self):
        try:
            url      = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"
            headers  = {"accept": "application/json"}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                current = response.json()["rates"][self.TO]
                USD     = response.json()["rates"][self.FROM]
                result  = current / USD
                print(f"Request to API: {url}")         # DEBUG
                return result
        except:
            return None
        
    # API Service:
    # https://openexchangerates.org/account/usage




## TESTING:
# testing = ConverterV2(from_currency="EUR")
# data = testing.get_convert()
# print(data)



# 1 USD = 82.124993 RUB
# 1 KZT = 0.180418 RUB
# 1 TRY = 4.228276 RUB
# 1 EUR = 90.618693 RUB

