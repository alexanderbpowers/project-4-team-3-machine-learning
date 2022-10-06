from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 
import pymongo
import pyreadstat

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

    model = pyreadstat.read_sav('file_path')

    
    

    return scraped_data

scraper()


