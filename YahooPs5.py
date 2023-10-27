# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests as rq
from bs4 import BeautifulSoup

url ='https://tw.buy.yahoo.com/search/product'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
param = {}
p = input('輸入查詢的商品: ')
param['p'] = p

data =rq.get(url,params=param,headers=header).text

soup =BeautifulSoup(data,'html.parser')

goods = soup.find('div',class_='ResultList_resultList_IpWJt')

items = goods.find_all('a')

for row in items:
    
    title = row.find('span',class_='sc-1d7r8jg-0 sc-dp9751-0 sc-1drl28c-5 czfCFU fUBIAU biZSHp')
    if title!= None:
        title = title.text
        print('標題: ' + title)
    
    link = row.get('href')
    print('連結: ' + link)
        
    price = row.find('span' , class_='sc-1d7r8jg-0 sc-dp9751-0 eLSRyH eEsfHX')
    if price !=None:
        price = price.text
        price = price.replace('$','')
        price=price.replace(',','')
        print('價錢: ' + price)
    
        
