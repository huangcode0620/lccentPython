# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:18:42 2023

@author: a8331
"""

import db
import requests as rq
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.setn.com/ViewAll.aspx?PageGroupID=0'
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
data = rq.get(url, headers=header ).text
soup = BeautifulSoup(data,'html.parser')

content = soup.find(id = 'NewsList')
news = content.find_all('div',class_='newsItems')

for item in news:
    h3 = item.find('h3')
    
    title = h3.text
    link = h3.find('a').get('href')
    if not('http' in link):
        link = 'https://www.setn.com/'+link#有些娛樂星聞以添加網址，需用if來新增網址
    post_date = item.find('time').text
    
    year = datetime.today().year
    post_date = str(year) + '/' + post_date
        
    sql = "select * from news where title = '{}' and platform='setn' ".format(title)
    db.cursor.execute(sql)
    
    if db.cursor.rowcount == 0:#表示資料表中沒有此筆資料
        sql ="insert into news(title,link_url,post_date,platform) values('{}','{}','{}','setn')".format(title,link,post_date,'setn')
        db.cursor.execute(sql)
        db.conn.commit()

db.conn.close()
        
        
        
        
        
        
        
        
        
        