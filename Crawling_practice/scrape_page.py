'''
This is a simple page scraper which can access using a generic url, I will try to build it to scrape
    [x] Title
    [x] Topic
    [x] Content
'''

from selenium import webdriver

# Write data to Excel file 
import xlwt
from xlwt import Workbook

# If you did not leave your web driver in Scripts of Python, it will never work until  you determine the path to it 
driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

# Define a generic url path
url = "".join(["https://vnexpress.net/giuliani-khong-giup-trump-trong-phien-toa-luan-toi-4223032.html"])
# Get url path
driver.get(url)

headlines = driver.find_elements_by_class_name("title-detail")

# Write titles to excel file
workbook = Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet('Sheet 1')

# Specify row as the point to kick start writing
row = 1
# Specify style and title as head row for title
title_style = xlwt.easyxf('font: bold 1') 
sheet1.write(0, 0, 'Title', title_style)

# Title section
for headline in headlines:
    #print(headline.text.strip())
    title = headline.text.strip()
    if(len(title) == 0):
        continue
    else:
        sheet1.write(row, 0, str(title))
        row = row + 1

# Specify style and content as head row for title
title_style = xlwt.easyxf('font: bold 1') 
sheet1.write(0, 1, 'Content', title_style)

contents = driver.find_elements_by_class_name("Normal")

# Content section
# Use array to store every p then store them back in excel cell later
content_array = []

for p in contents:
    #print(headline.text.strip())
    content = str(p.text.strip())
    content_array.append(content)

# Convert the the array into 1 line string
content_str = "\n".join(str(index) for index in content_array)

# Re-write the array in cell of excel
content_style = xlwt.easyxf('alignment: wrap True')
sheet1.write(1, 1, content_str, content_style)

# Scrape topic
sheet1.write(0, 2, 'Topic', title_style)

xpath = "/html/body/section[5]/div/div[2]/div[1]/ul/li/a"
topic = driver.find_element_by_xpath(xpath)
sheet1.write(1, 2, topic.text, content_style)

# Save excel file .... and hhhm this needs a specification, fosho
workbook.save('./Data/page_data.xls')