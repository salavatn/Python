import requests
from bs4 import BeautifulSoup
'''
url = 'https://saverudata.online/#/?n=79091671073'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser', from_encoding='utf-8')
print(f"Soup:\t{soup}\n\n")
'''


url = 'https://saverudata.online/#/?n=79091671073'
# response = requests.get(url)
# content_type = response.headers.get('content-type')
# encoding = content_type.split('charset=')[-1]
# print(encoding)




# Отправка GET-запроса для получения HTML-кода страницы
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Создание объекта BeautifulSoup для парсинга HTML-кода страницы
    soup = BeautifulSoup(response.content, 'html.parser')

    # soup.find('span', {'title': 'Yandex Eda'})

    span_element = soup.find('span', {'title': 'Yandex Eda'})
    title_value = span_element.get('title')

    print(f"Title: {title_value}")
    # print(f"Title: {span_element}")
else:
    print('Ошибка при запросе страницы')





# print(f"CONTENT:\t{data.text}\n\n")

# def get_data(url):
#     content = requests.get(url)
#     soup = BeautifulSoup(content.text, 'html.parser')
#     return soup

# soup = get_data(url)

# data_block = get_data(url).find('div')
# print(data_block)
# phone_tag = data_block.find('b', string='Телефон:').find_next_sibling('br')
# phone_number = phone_tag.next_sibling.strip()
# print(phone_number)


'''div_tags = get_data(url).find_all('div', class_=None)


for div in div_tags:
    print(f"DIV: {div}\n\n")
    if div.find('b') is not None:
        print(f"DIV: {div}\n\n")

'''
'''
article = soup.find('article', class_='app_content__kzxes')
for element in article:
    print(element)
# print(article)
'''

# b_tags = soup.find_all('b', string='Телефон:')
# info = b_tags.find_next_sibling('span').next_sibling.strip()
# print(f"Phone: {b_tags}")
# print(f"Info: {info}")

# for tag in b_tags:
#     phone = tag.next_sibling.text.strip()
#     print(f"Phone: {phone}")




#           <article class="app_content__kzxes">
# <div style="display: none;" class="app_form__hVKoo"> </div>

# content = soup.find('b', string='Телефон:').find_next_sibling('br').next_sibling.strip()


# data = requests.get(url)
# # soup = BeautifulSoup(content.text, 'html.parser')

# print(f"CONTENT:\t{data.text}\n\n")
# content = soup.find_next_sibling('b', string='Заказы:')
# print(f"CONTENT:\t{content}\n\n")
# print(f"TYPE:\t{type(content)}")