# WELCOME TO `MIDTERM` FOLDER

- This shall be a good place for you to find my midterm attempt for a basic natural language processing implementation :tada:
- I should keep the intro short, let's get it begin 

## :bookmark: Objectives
Crawl data from vnexpress (at least 5 topic, 40 documents/1 topic)

Output:  
-  Pre processing (stopword, html,tokenize…)
Extract TF-IDF feature
Using SVM for training of document classification
Evaluate by Accuracy

## :bookmark: Objective evaluation 
- [x] Crawl data from Vnexpress from 5 topics, 40 articles/topic => 200 articles in total
- [x] Data pre-processing
- [x] Extract model using TF-IDF feature -> Converting Text to Features using TF-IDF
- [x] Using SVM for training of document classification
- [x] Evaluate by Accuracy



## :question: How I started? 
- Look, as a dummy in Machine Learning, I do read the books first and things that read are all in `Books` folder

## :question: Crawling data from a website - VnExpress

- Articles you can reach
    
    * [Best 3 Ways to Crawl Data from a Website](https://www.octoparse.com/blog/how-to-crawl-data-from-a-website)

- But look, I have some here :smile:

<p align = "center">
    <img src = "https://i.ibb.co/qM27wr0/image.png" width="250px"/>
</p>

- Okie, let's practice, let the game begin with crawling data manually from a simple article. Visit `Crawling_practice` for more
    - URL: https://e.vnexpress.net/news/news/first-saigon-metro-line-gets-power-4237364.html

- It's new to me so I will try to build myself a web crawler using Python

- We're gonna need a driver for your browser to make it work as a middleware. If you are using Chrome, [click here](http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-windows-install/) for detailed installation

- Trying Scrapy from Python for website crawling lib

```
pip install scrapy
```

- But this requires Microsoft Visual C++ 14.0 or up so make sure you have it before the `pip`. But I don't recommend using `scrapy`

- Next, `Selenium`, still a scrawling tool but it does not require VS C++ or else just go ahead and 
```
pip install selenium
```

- This is noted by 05/03/2021, I have finished my web scraper but it is not good enough but I will give it an update soon.

## :question: Data pre-processing

- After crawling from VnExpress, the :page_with_curl: garbage I have here is a list of things like this
<p align = "center">
    <img src = "https://i.ibb.co/XYvC8z3/image.png" width="250px" height="350px"/>
</p>

- Then, the mission of my here is that I'm going to merge them to 1 xls file only. But the problem here is that there are some duplicated data so let do something about that... but hey :smile:, I will move to Google Colab since my computer does not have  Visual C++ 14.0 - which is a legendary mistake of all time... :cry: I just want to say, please use Anaconda or Python Notebook instead, you don't want this "build-tool" to install a whole Visual Studio that you don't even need :angry:
- My next choice shall be Google Colab, trust me, it looks much better than your IDE :) 
<p align = "center">
    <img src = "https://i.ibb.co/1XDFRBT/image.png" width="250px" height="100px"/>
</p>

- Tasks that I did
### :book: Lowercase

### :book: Punctuation removal

### :book: Stopwords removal
- For Stopwords removal, nltk needs to be `nltk.download()` first to download stopwords lib

### :book: String tokenization
- 
