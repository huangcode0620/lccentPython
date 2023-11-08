# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:46:14 2023

@author: a8331
"""
from selenium import webdriver#pip install selenium
import requests as rq
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome()

driver.implicitly_wait(3)#等待時間

driver.get('https://supertaste.tvbs.com.tw/food')

for i in range(5):
    driver.execute_script('latest_more.click()')#點擊載入更多
    time.sleep(1)