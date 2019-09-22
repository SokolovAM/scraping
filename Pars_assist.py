import requests as rq
from bs4 import BeautifulSoup as bs

class Assist:
    headers = {'Accept':'*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; ServiceUI 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
    base_url = 'https://yandex.ru/'

    def __init__(self):
        session = rq.session()
        req = rq.get(self.base_url, headers = self.headers)
        if req.status_code == 200:            
            self.soup = bs(req.content, 'html.parser')
            print('I\'m Ok!')
        else:
            print('Error')

    def news(self):
        """Method returns titles and refs of top 4 news of Yandex"""        
        news_list = self.soup.find_all('li',attrs = {'class' : 'list__item list__item_icon'})        
        for i, news in enumerate(news_list):
            news_href = news.find('a',attrs = {'class' : 'home-link list__item-content list__item-content_with-icon home-link_black_yes'})['href']
            print('{} - {}'.format(i + 1, news.text))
            print(news_href,'\n')                       
        
    def ex_rate(self):
        """Method returns current rate of USD & EUR on the MOEX"""        
        rate_USD = self.soup.find('div',attrs = {'class' : 'b-inline inline-stocks__item inline-stocks__item_id_2002 hint__item inline-stocks__part'})
        USD_inf = rate_USD.find('span',attrs = {'class' : 'inline-stocks__item__baloon_inner'}).text
        USD_value = rate_USD.find('span',attrs = {'class' : 'inline-stocks__value_inner'}).text        
        print('USD\n', USD_inf.strip(), ' : ', USD_value, '\n')

        rate_EUR = self.soup.find('div', attrs = {'class' : 'b-inline inline-stocks__item inline-stocks__item_id_2000 hint__item inline-stocks__part'})
        EUR_inf = rate_EUR.find('span', attrs = {'class' : 'inline-stocks__item__baloon_inner'}).text
        EUR_value = rate_EUR.find('span', attrs = {'class' : 'inline-stocks__value_inner'}).text
        print('EUR\n', EUR_inf.strip(), ' : ', EUR_value, '\n')

    def weather(self):
        '''Method returns current weather conditions'''
        weather_content = self.soup.find('div', attrs = {'class' : 'weather__content'})
        weather_condition = weather_content.find('div', attrs = {'class' : 'weather__icon weather__icon_ovc'})['title']
        temperature = weather_content.find('div', attrs = {'class' : 'weather__temp'}).text
        print('WEATHER')
        print('Condition : ',weather_condition,'\nTemperature : ',temperature)

    def search(self, search_query, page = 0):
        '''Method searches given phrase in Yandex and returns titles of articles and their refs'''
        parametrs = {'text':f'{search_query}','page' : f'{page}'}       
        req = rq.get(self.base_url + 'search/', params=parametrs, headers = self.headers)
        if req.status_code == 200:
            sp = bs(req.content, 'html.parser')
            serps = sp.find_all('li',attrs = {'class':'serp-item'})
            for i, serp in enumerate(serps):                
                name = serp.find('div',attrs = {'class':'organic__url-text'}).text                
                href = serp.find('a',attrs = {'class':'link_theme_outer'})["href"]                
                print('***'*20)
                print(f'{i + 1} - {name}')                
                print(href,'\n')
        else:
            print('Error')        


Assist1 = Assist()
Assist1.news()
Assist1.ex_rate()
Assist1.weather()
Assist1.search('Python requests')