            #       содержать:
            # название источника;
            # наименование новости;
            # ссылку на новость;
            # дата публикации.
            # Сложить собранные новости в БД

import requests
from bs4 import BeautifulSoup as bs
from news import News
from news_methods import NewsMethods

newMetod = NewsMethods()

rubric = ['russia', 'world', 'ussr']

url_mail = "https://news.mail.ru/"
url_lenta = "https://lenta.ru/rubrics/"
url_yandex = "https://dzen.ru/news?utm_referrer=www.google.com"
url_hh = 'https://novosibirsk.hh.ru/'

def crete_request(url: str) -> bs:
    response = requests.get(url=url, headers={"Content-Type":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"})
    # print(response.status_code)
    soup = bs(response.content, "html.parser")
    return soup

def init_new_obj(data: dict) -> News:
    newsObj = News()
    newsObj.nameNew = data['name']
    newsObj.rubric = data['rubric']
    newsObj.refNew = data['refNew']  
    newsObj.date = data['date']
    newsObj.refSite = data['refSite']
    
    
    return newsObj

def find_data(response: bs, rubric: str):


    
    data = {
        "name" : None,
        "rubric" : rubric,
        "refNew" : None,
        "date" : None,
        "refSite" : 'lenta.ru',
    }

    block_news_next = response.find_all(class_='longgrid-feature-list__box')
    
    for news in block_news_next:
        try:
            items = news.find_all('a')
            # print(items)
            for item in items:
                data['refNew'] = data['refSite'] +'/'+ item['href']
                data['name'] = item.find('h3').text
                data['date'] = item.find('time').text
                newMetod.add_new_in_list(init_new_obj(data))
            
        except:
            print('not found block')

    
         
     


def main():
    response = crete_request(url_hh)
    print(response)
    # for el in rubric:
    #     response = crete_request(url_lenta + el)
    #     find_data(response = response, rubric= el)
    # newMetod.createDB()
    # newMetod.clearDB()
    # newMetod.insertDB()
    # newMetod.readDB()

if __name__ == '__main__':
    main()