# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:16:31 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = 'https://supertaste.tvbs.com.tw/food'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

data = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')

# food = soup.find('div',class_='article__content') #class為python專用詞不可使用，可使用下方字典方式

food = soup.find('div',{'class':'article__content'})#key,value

a = food.find_all('a')

for row in a:
    img = row.find('img').get('data-original')
    title = row.find('h3').text.strip()
    post = row.find('span').text.strip()
    link = 'https://supertaste.tvbs.com.tw' + row.get('href')
    
    print('標題: ' + title)
    print('日期: ' + post)
    print('圖片: ' + img)    
    print('連結: ' + link)
    print()    