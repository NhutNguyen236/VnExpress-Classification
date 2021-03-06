'''
    try_scraper is a testing module to get href from a simple css_selector 
    So can you scrape href from a class_name -> Yes, you can but in my case, NO.
'''

from selenium import webdriver
import csv

driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

driver.get("https://vnexpress.net/hai-duong-them-6-ca-covid-19-4243653.html")

des = driver.find_element_by_class_name('description')

print(des.text.strip())
