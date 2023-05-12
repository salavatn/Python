from dotenv import load_dotenv
from typing import Union
import requests
import logging
import os

load_dotenv(dotenv_path='.env')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
app_id = os.getenv('YOUR_API_ID')

logger.debug('FILE: currancy.py')

class Converter:
    def __init__(self, currency: str = 'RUB') -> None:
        self.currency_from = currency
        self.currency_usd  = 'USD'

    def get_convert(self) -> Union[float, None]:
        '''Get currency rate from API'''
        logger.debug(f"Getting currency rate for {self.currency_from} -> {self.currency_usd}")
        url      = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"
        headers  = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            current = response.json()["rates"][self.currency_usd]
            usd     = response.json()["rates"][self.currency_from]
            result  = current / usd
            logger.debug(f"Result: {result}")
            return result

        
    # API Service:
    # https://openexchangerates.org/account/usage

    # Examples:
    # 1 USD = 82.124993 RUB
    # 1 KZT = 0.180418 RUB
    # 1 TRY = 4.228276 RUB
    # 1 EUR = 90.618693 RUB

