import requests


website = 'http://bashorg.org'
content = requests.get(website)


status   = content.status_code
header   = content.headers
html_txt = content.text
