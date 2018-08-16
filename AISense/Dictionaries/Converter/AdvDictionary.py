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
        url = 'http://www.dictionary.com/browse/{}'.format(word)

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # print resp.text
        dict_mod = soup.find('div', {'class': 'source-box'})
        word = dict_mod.find('span', {'class': 'me'}).text
        pron = dict_mod.find('span', {'class': 'pron spellpron'}).text

        global GWord
        GWord = re.sub('\W+','', word)
        
        global GPron
        GPron = pron[1:-2]
        
        return GWord
    except AttributeError:
        GPron = "------------"
        GWord = "------------"
        return "------------"

def getWord ():
    return GWord

def getPron ():
    return GPron

#print lookup_word('someone')
