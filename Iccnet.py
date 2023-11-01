# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:54:48 2023

@author: USER
"""

import requests as  rq
from bs4 import BeautifulSoup

url = 'https://member.lccnet.com.tw/'
params={
       'Account': '105433770',
       'Password': '21374217p',
       'RememberMe': 'false',
       '__RequestVerificationToken': '9kC_T3GykSU_pSNcY4ibfGzJOS9mWsTtkxw9_2HtYeUQhgETnNkIlab4fyEBKdFWvcLrqNsq6939bO4nMcoTUI-SYf1P2iq-iUWX4cxZJRU1'
       }
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie':
    '_cuid=d26a0a7a-35eb-40c1-9152-2477ae6c9160; _cuserid=; _cusertrait=%7B%7D; _ctrait=%7B%7D; _cgrpid=; _cgrptrait=%7B%7D; _ss_pp_id=0c3944a69cfb0581c0a1687810088393; _hjSessionUser_1446807=eyJpZCI6ImM4MTE0NWFjLTg5YzEtNThlZi1iMGYyLTgwMGUyMzU0YTNkYiIsImNyZWF0ZWQiOjE2ODc4Mzg4ODY1MTEsImV4aXN0aW5nIjp0cnVlfQ==; _ga_TDP4KNDS80=GS1.1.1689314436.3.0.1689314436.60.0.0; script_flag=fd13385c-97e5-4e21-ac73-ac7f33c5bbc8; _gcl_au=1.1.667955781.1698835031; _fbp=fb.2.1698835031234.1812209554; _gid=GA1.3.2001615010.1698835031; url_flag=https://www.lccnet.com.tw/lccnet; _hjIncludedInSessionSample_1446807=0; _hjSession_1446807=eyJpZCI6ImU3Njk3MmVlLTJjNGUtNGVlMy1hOWVmLWFhNjkyZDZhM2VlZiIsImNyZWF0ZWQiOjE2OTg4NDMzMDkwMjMsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=0; _uetsid=9d52724078a211ee8c3a876098aefedd; _uetvid=3847673014a011eeabce1f9513625979; _td=16350bed-ab40-4982-aa57-0dd5cf0f17ec; cto_bundle=N3kzx18lMkJRN050aUw3d1k0TklTa20lMkJyVm5nVm9BSzQlMkZuSnhqemlybyUyQk5NSVhBTHY4S3Z5SUJRMnIlMkJzcUJoVlZzTnNvQ29FJTJCZThmYkMzd0dHVzRyUHEzZURKMDdYM3JWbUNFSHV6ekhxbThTUmh6bWJvZ2hJJTJCYTFvRDlUemVLJTJCTk9PbVJKMlpoUVNaUVdhc2ZNc0slMkJDazRqZ0ElM0QlM0Q; __RequestVerificationToken=PsKIm8vNDyqatc2I5QTpvsbqhbhq0CHGoH8vPNbOcIgPTahCJfOOIkOOhL90Hy9iypIYlpoe1YfGdHpvayHohBhZlMaiGWaTdCpoMJ5HbyE1; _ga=GA1.4.489821006.1687838887; _gid=GA1.4.2001615010.1698835031; _ga_QY8DQDPMSR=GS1.1.1698843308.5.1.1698843326.42.0.0; _ga_FNFG97HXYJ=GS1.1.1698843308.2.0.1698843326.0.0.0; _ga_Q39DSHDCZC=GS1.1.1698843309.2.0.1698843326.0.0.0; adgeek_login_path=/; adgeek_lccnet_user_id=05-1071211003; _dc_gtm_UA-8399363-4=1; _gat_gtag_UA_8399363_3=1; _ga_RV6BDWB9GV=GS1.1.1698843311.1.1.1698843788.0.0.0; _ga=GA1.1.489821006.1687838887; _ga_ENRV8GBKH8=GS1.1.1698843309.2.1.1698843788.51.0.0; adgeek_login_status=true; _ga_RHTTWMMSB7=GS1.1.1698843309.2.1.1698843835.4.0.0'
    }
    
session_rq = rq.session()

content = session_rq.post(url,data=params,headers=header).text

url2 = 'https://member.lccnet.com.tw/Booking'

content= session_rq.get(url2).text
soup = BeautifulSoup(content,'html.parser')

course = soup.find('ul',class_='courseListWrapper')
li = course.find_all('li')
for item in li:
    
    name =  item.find('h4').text
    time = item.find_all('p')
    
    print(name)
    for i in time:
        print(i.text)      
        
    print('-'*40)
    
    




