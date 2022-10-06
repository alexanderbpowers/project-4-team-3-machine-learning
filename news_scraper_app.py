from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 
import pymongo
import pyreadstat
import pickle


filename = 'nlp_logistical_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def article_reader(input):
    
    scraped_data = {}

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = input
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    title = soup.find('h1', {"id" : "story-headline"}).get_text(strip=True)

    articles = soup.find_all('div', {'id' : 'story-primary'})
    article_text = ""
    for article in articles:
        article_text += article.text

    scraped_data['title'] = title
    scraped_data['article'] = article_text

    browser.quit()

    X = text_transform(scraped_data)
    prediction = loaded_model.predict(X)

    update_page(X)





def text_transform():


    return X

def update_page();




