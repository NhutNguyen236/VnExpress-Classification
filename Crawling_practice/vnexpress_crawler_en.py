'''
After hanging around the whole day with my scrape_page which is a scraper that will scrape
title, content, topic of the news. I came up with the idea of making it more automational

Gotta add that auto crawl topic later, this is gonna take time

Steps to perform: 
- Get all url using find_element_by_css selector from page
- driver get every url in for loop to access to page
- Use technique in page_scrape to get content, title and topic
- Done

This scraper is not on top of the world tho because it needs a static url to run so you have to change it time to time
This is English edition crawler
'''

# Libs import
from selenium import webdriver # Chromedriver 
import xlwt
from xlwt import Workbook
import time
import string

# Define topic list here to crawl 

# If you did not leave your web driver in Scripts of Python, it will never work until  you determine the path to it 
driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

# Define url path
main_url = "".join(["https://e.vnexpress.net/news/travel/food"])
# Get url path
driver.get(main_url)

# Write titles to excel file
workbook = Workbook()
title_style = xlwt.easyxf('font: bold 1') 
sheet1 = workbook.add_sheet('Sheet 1')

# Show more stories  by clicking 'View more stories'
view_more_button = driver.find_element_by_xpath('/html/body/div[2]/section/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/a')
# view_more_button = driver.find_element_by_xpath('//*[@id="vnexpress_folder_load_more"]')
for i in range(0, 12):
    view_more_button.click()

# Step 1: Get all urls
# First, I am getting a list of web-element which stands for news title
# This is the weak point of using css_selector, different pages got different ways to arrange their element so the tags got changed to adapt
titles = driver.find_elements_by_css_selector("h2 a[href*='https://e.vnexpress.net']")

# Get urls from titles
url_array = []
for t in titles:
    url = t.get_attribute('href')
    url_array.append(url)

# Then delete duplicate links
for link in url_array:
    if(str(link).find('#box_comment') != -1):
        url_array.remove(link)

new_url_array = list(set(url_array))

print(new_url_array)

# Specify row as the point to kick start writing
row = 1

# Specify head row for each field
content_style = xlwt.easyxf('alignment: wrap True')
sheet1.write(0, 0, 'Title', title_style)
sheet1.write(0, 1, 'Content', title_style)
sheet1.write(0, 2, 'Topic', title_style)

# Actually, this one is just an url reader
for u in new_url_array:
    # Step 2: Now I can get url from the title above
    # Go to the url to scrape things
    driver.get(u)

    # Write the title in xls first 
    title = driver.find_element_by_class_name('title_post')
    sheet1.write(row, 0, str(title.text.strip()))

    # now this is where the game begins, let's scrape all the contents and topics baby!!!
    # This is for scraping the rest of the content
    contents = driver.find_elements_by_class_name("Normal")
    content_array = []

    # define break-point
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

    # Re-write the array in cell of excel
    sheet1.write(row, 1, content_str, content_style)

    # Second, it is for topics
    # This is for the white theme only so it could be a mess for the black one
    xpath = '/html/body/div[2]/section/div[1]/div/div/a'
    # Solution for this problem is | operator

    topic = driver.find_element_by_xpath(xpath)
    
    sheet1.write(row, 2, topic.text)

    # Now increase the row for something else
    row = row + 1
    time.sleep(2.5)

# Save excel file .... and hhhm this needs a specification, fosho
workbook.save('./Data/Raw_Data/EN/food.xls')