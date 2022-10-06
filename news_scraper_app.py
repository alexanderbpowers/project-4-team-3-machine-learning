from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 
import pickle
import requests


filename = 'nlp_logistical_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def article_reader(input):
    
    scraped_data = {}
    
    url = "https://www.news.com.au/lifestyle/food/restaurants-bars/my-heart-aches-iconic-melbourne-cbd-venues-bar-americano-and-pentolina-to-close/news-story/3058ae72173263c24e01ad87f140029a"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    title = soup.title.text.strip()

    articles = soup.body.find_all('p')
    article_text = ""
    for article in articles:
        article_text += article.text

    scraped_data['title'] = title
    scraped_data['article'] = article_text

    X = text_transform(scraped_data)
    prediction = loaded_model.predict(X)

    update_page(prediction)



def text_transform():


    return X



def update_page();




