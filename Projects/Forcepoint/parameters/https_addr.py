import random
import requests


def get_https():
    url_region = [".ru/", ".com/", ".org/", ".net/", ".kz/", ".cn/", ".edu/"]
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    data = requests.get(word_site)
    select_word1 = random.randint(10, 1000)
    select_url = random.randint(0, 6)
    word_raw = data.content.splitlines()
    domain1 = str(word_raw[select_word1])[2:-1]
    domain2 = str(url_region[select_url])
    return f'Hostname "https://www.{url_start}{domain1}{domain2}"'