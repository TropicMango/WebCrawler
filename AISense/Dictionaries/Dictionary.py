import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

headers = {
    'User-Agent': USER_AGENT
}

def lookup_word(word):
    url = 'http://www.dictionary.com/browse/{}'.format(word)

    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # print resp.text
    dict_mod = soup.find('div', {'class': 'source-box'})
    pron = dict_mod.find('span', {'class': 'pron spellpron'}).text
    return pron[1:-2]



#print lookup_word('someone')
