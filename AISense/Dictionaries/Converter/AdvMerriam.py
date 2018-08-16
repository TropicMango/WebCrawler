import requests
import re
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

headers = {
    'User-Agent': USER_AGENT
}

GWord = "omg"
GPron = "hi"

def lookup_word(word):
    try:
        url = 'https://www.merriam-webster.com/dictionary/{}'.format(word)

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # print resp.text
        dict_mod = soup.find('div', {'class': 'inner-box-wrapper'})
        word = dict_mod.find('h1').text
        pron = dict_mod.find('span', {'class': 'pr'}).text


        global GWord
        GWord = re.sub('\W+','', word)
        
        global GPron
        GPron = pron[1:-1]

        return GPron
    except AttributeError:
        GPron = "------------"
        GWord = "------------"
        return "------------"

def getWord ():
    return GWord

def getPron ():
    return GPron


