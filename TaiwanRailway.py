# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:08:18 2023

@author: USER
"""

import requests as rq

from bs4 import BeautifulSoup

url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation'
header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
param = {'_csrf':'82060953-2ec5-4972-861a-a150d58393d0',
         'rideDate':'2023/10/27',
         'station':'3300-臺中'}

data = rq.post(url,data = param , headers = header).text

soup = BeautifulSoup(data,'html.parser')

ride = soup.find(id = 'tab1')

items = ride.find_all('tr')[1:]

for row in items:
    car = row.find('a').text
    tds = row.find_all('td')
    sp = row.find_all('span')
    print('車次: ' + car)
    print(sp[2].text,sp[3].text,sp[4].text)
    print('出發時間: ',tds[1].text)
    print('終點站: ',tds[2].text)
    print()