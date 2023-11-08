# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:20:08 2023

@author: a8331
"""

from PIL import Image #圖形辨識
import pytesseract #圖形轉文字

FileName = 'number02.png'
pytesseract.pytesseract.tesseract_cmd = r''

img = Image.open(FileName)

text = pytesseract.image_to_string(img,lang='eng',config='-c tessedit_char_whitelist=0123456789 --psm 9')
 
#--oem 有4個參數(0,1,2,3)
#--psm有13個參數(自動頁面分割) 10為將圖像視為單一字元,8,9視為單字,7視為1行文字,6為區塊文章

print(text)

