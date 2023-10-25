# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:58:38 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

data = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')

rate = soup.find(id = 'exchangeRate')

tbody = rate.find('tbody')

trs = tbody.find_all('tr')

for row in trs:
    tds = row.find_all('td',recursive = False)
    if len(tds) ==4:
        print(tds[0].text.strip().split()[0])
        print(tds[1].text.strip())
        print(tds[2].text.strip())
        print(tds[3].text.strip())