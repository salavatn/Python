import requests
from bs4 import BeautifulSoup

request = requests.get('https://saverudata.online/#/?n=79169233970')

status = request.status_code
headers = request.headers['content-type']
encoding = request.encoding

# print(request.text)


# soup = BeautifulSoup(request.content, "html.parser")
soup2 = BeautifulSoup(markup=request.content, features="html.parser")
search = 'class="app_content__kzxes"'
results = soup2.find(title="LinkedIn")

print(results)
