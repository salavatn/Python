from dotenv import load_dotenv
import requests
import json
import os

# Load environment variables
load_dotenv(dotenv_path='.env_api')
YOUR_API_ID = os.getenv('YOUR_API_ID')


class Converter:
    def __init__(self, from_currency = 'RUB'):
        self.valute_from  = from_currency
        self.valute_to    = 'USD'

    def get_convert(self):
        url      = "https://api.apilayer.com/currency_data/live"
        headers  = {"apikey": "G2qYZAAnSixyKA38ln4QMf23I2ZGh5mx"}
        params   = {"source": self.valute_from, "currencies": self.valute_to}
        from_to  = self.valute_from + self.valute_to
        response = requests.get(url, params=params, headers=headers)
        response_data = json.loads(response.text)

        print(f"Response status code: {response.status_code}")  # 200
        print(f"Response data: {response_data}")

        if response.status_code == 200 and response_data["success"]:
            exchange_rate   = response_data["quotes"][from_to]
            amount_to       = 10000000 * exchange_rate
            result = amount_to / 10000000
            # result = {f"{self.valute_from}": 1,
            #           f"{self.valute_to}": result}
            print(f"1 {self.valute_from} = {result} {self.valute_to}")
            print(f"Exchange rate is {exchange_rate}")
            return result
        else:
            return None


class ConverterV2:
    # API Service:
    # https://openexchangerates.org/account/usage

    def __init__(self, from_currency = 'RUB'):
        self.FROM = from_currency
        self.TO    = 'USD'

    def get_convert(self):
        url      = f"https://openexchangerates.org/api/latest.json?app_id={YOUR_API_ID}"
        headers  = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            current = response.json()["rates"][self.TO]
            USD     = response.json()["rates"][self.FROM]
            result  = current / USD
            # print(result)
            return result
        else:
            # print("Не удалось получить данные от API.")
            return None










## TESTING:
# testing = ConverterV2(from_currency="EUR")
# data = testing.get_convert()
# print(data)



# 1 USD = 82.124993 RUB
# 1 KZT = 0.180418 RUB
# 1 TRY = 4.228276 RUB
# 1 EUR = 90.618693 RUB

