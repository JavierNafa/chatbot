from requests import get
from bs4 import BeautifulSoup
from settings import search_url

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
params = {
    'q':None,
    'hl':'en'
}

def search(user_input:str):
    params['q'] = user_input
    with get(search_url,params=params,headers=headers) as page:
        soup = BeautifulSoup(page.content,features='html.parser')
        raw_text = soup.find(class_='kno-rdesc')
        if raw_text:
            return raw_text.text.lower()
        return None