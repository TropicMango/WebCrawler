import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

headers = {
    'User-Agent': USER_AGENT
}

def lookup_word(word):
    url = 'https://www.facebook.com/'

    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    print(resp.text)
    #dict_mod = soup.find('div', {'id': 'dictionary-modules'})
    #pron = dict_mod.find('span', {'class': 'lr_dct_ph'}).text
    #return pron[:-1]


print(lookup_word('vertex'))

