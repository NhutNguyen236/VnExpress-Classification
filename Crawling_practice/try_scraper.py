'''
    try_scraper is a testing module to get href from a simple css_selector 
    So can you scrape href from a class_name -> Yes, you can but in my case, NO.
'''

from selenium import webdriver
import pandas as pd 
import os 
import re
from nltk.corpus import stopwords

driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

driver.get("https://e.vnexpress.net/news/life/style/ninh-binh-restaurant-wins-international-architecture-prize-4241664.html")

contents = driver.find_elements_by_class_name("Normal")
print(bool(contents))
content_array = []

p_count = 0

for p in contents:
    if(p_count == 3):
        break
    else:
        #print(headline.text.strip())
        content = str(p.text.strip())
        content_array.append(content)
        p_count = p_count + 1

# Convert the the array into 1 line string
content_str = " ".join(str(index) for index in content_array)

content_str =  content_str.lower()
content_str =  content_str.replace('[^\w\s]','')

print(content_str)
