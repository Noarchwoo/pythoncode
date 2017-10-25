import os
import webbrowser

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
query = raw_input('Enter the song to be played: ')
query = query.replace(' ', '%20')

url = 'http://music.163.com/#/search/m/?s=%s&type=1' %(query)

page = requests.get(url, headers=headers, timeout=15)

plain_txt = page.text
soup = BeautifulSoup(plain_txt, 'html.parser')
data = soup.find_all('iframe')
songs = soup.find_all('div', {'class': 'm-top'})

driver = webdriver.PhantomJS()
driver.get(url)

driver.switch_to.frame('g_iframe')

print driver



print data
#webbrowser.open(url)
