from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 
import pickle
import requests


filename = 'nlp_logistical_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def article_reader(input):
    
    url = input
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    title = soup.title.text.strip()

    articles = soup.body.find_all('p')
    article_text = ""
    for article in articles:
        article_text += article.text

    X = text_transform(scraped_data)
    prediction = loaded_model.predict(X)

    scraped_data = {
        'title' : title,
        'text' : article_text,
        'prediction' : prediction 
    }

    return scraped_data


def homepage_reader():

    url = 'https://www.news.com.au/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    titles = soup.find_all('h4', class_="storyblock_title")
    title_li = []
    for title in titles:
        title_li.append(title.text)

    articles = soup.find_all('p', class_='storyblock_standfirst g_font-body-s')
    article_li = []
    for article in articles:
        article_li.append(article.text)

    scraped_data = pd.DataFrame(list(zip(title_li, article_li)))

    scraped_data.columns = ['title','text']

    X = text_transform(scraped_data)

    prediction_arr = []
    for x in X:
        prediction = loaded_model.predict(x)
        prediction_arr(prediction)

    X_filtered = filter(lambda x: x == 0, prediction_arr)
    X_filtered = list(X_filtered)
    trustworthy_percent = (len(X_filtered)/len(X)) * 100

    scraped_data = {
        'title' : title_li,
        'text' : article_li,
        'trustworthy_percent' : trustworthy_percent 
    }

    return scraped_data



def text_transform_homepage():


    return X









