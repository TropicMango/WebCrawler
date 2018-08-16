import requests
import re

from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/536.36 (KHTML, like Gecko) ' \
             'Chrome/59.0.3071.115 Safari/537.36 '

headers = {
    'User-Agent': USER_AGENT
}

GWord = "omg"
GPron = "hi"


def lookup_word(word):
    try:
        url = 'https://www.google.com/search?q=define%3A{}'.format(word)

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # print resp.text
        dict_mod = soup.find('div', {'id': 'dictionary-modules'})
        word = dict_mod.find('span', {'data-dobid': 'hdw'}).text
        pron = dict_mod.find('span', {'class': 'lr_dct_ph'}).text

        global GWord
        GWord = re.sub('\W+', '', word)

        global GPron
        GPron = pron[:-1]

        return GWord
    except AttributeError:
        GPron = "------------"
        GWord = "------------"
        return "------------"


def getWord():
    return GWord


def getPron():
    return GPron


#print lookup_word('apple')
# print getPron()
