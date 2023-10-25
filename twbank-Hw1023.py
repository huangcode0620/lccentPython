# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:06:37 2023
@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

data = requests.get(url).text

soup = BeautifulSoup(data,'html.parser')

rate = soup.find(id ='ie11andabove')

tbody = rate.find('tbody')

trs = tbody.find_all('tr')

inquire = rate.find_all('a')

for row in trs:
    
    tds = row.find_all('td')    
    currency = tds[0].text.strip().split()
    
         
    print('幣別: ' + currency[0])
    print('現今匯率:')
    print('本行買入: ' + tds[1].text.strip())
    print('本行賣出: ' + tds[2].text.strip())
    print('即期匯率:')
    print('本行買入: ' + tds[3].text.strip())
    print('本行賣出: ' + tds[4].text.strip())
    
for row in inquire:
        title = row.get('title')
        link = row.get('href')  
        print(title)
        print(link)    
    
    