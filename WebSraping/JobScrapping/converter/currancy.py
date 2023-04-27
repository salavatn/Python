import requests
import json


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

        if response.status_code == 200 and response_data["success"]:
            exchange_rate   = response_data["quotes"][from_to]
            amount_to       = 10000000 * exchange_rate
            result = amount_to / 10000000
            # result = {f"{self.valute_from}": 1,
            #           f"{self.valute_to}": result}

            return result
        else:
            return None



# 1 USD = 82.124993 RUB
# 1 KZT = 0.180418 RUB
# 1 TRY = 4.228276 RUB
# 1 EUR = 90.618693 RUB