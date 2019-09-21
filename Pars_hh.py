import requests
from bs4 import BeautifulSoup as bs

# Эмулирование поведения браузера(Edge):
headers = {'Accept' : '*/*',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; ServiceUI 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}

# Эмулирование поведения браузера(Google search):
#headers = {'accept' : 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
#        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}

base_url = 'https://hh.ru/search/vacancy?search_period=3&clusters=true&area=1&text=Python&enable_snippets=true'

def hh_parse(headers, base_url):
    # Задание сессии для создания иллюзии работы пользователя в браузере(если проверяется корректность cookie):
    session = requests.Session()
    # Эмулирование открытия страницы в браузере, ожидание ответа 5 секунд:
    request = requests.get(base_url, timeout =5, headers = headers)
    if request.status_code == 200:
        # Представление ответа от сервера request.content в удобочитаемом виде с помощью встроенного парсера
        # Результатом выполнени является html страница
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs = {'data-qa' : 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a',attrs = {'data-qa' : 'vacancy-serp__vacancy-title'}).text
            href = div.find('a',attrs = {'data-qa' : 'vacancy-serp__vacancy-title'})['href']
            print(title)
            print(href)
    else:
        print('Error')

hh_parse(headers, base_url)
