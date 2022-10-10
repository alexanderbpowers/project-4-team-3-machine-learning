from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 
import pickle
import requests
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

with open('ben_test.pickle', 'rb') as picklefile:
    saved_pipe = pickle.load(picklefile)

# nltk.download('stopwords')
port_stem = PorterStemmer()

###########

def stemming(content):

    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

###########

def article_reader(input):
   
    url = input
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    title = soup.title.text.strip()

    articles = soup.body.find_all('p')
    article_text = ""
    for article in articles:
        article_text += article.text

    scraped_data = {
        'title' : title,
        'text' : article_text,
    }

    X = article_text_transform(scraped_data)
    prediction = saved_pipe.predict(X)
    
    scraped_data = {
        'prediction' : prediction 
    }

    return scraped_data
    
###############

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

    df = pd.DataFrame(list(zip(title_li, article_li)))
    df.columns = ['title','text']

    X = homepage_text_transform(df)

    prediction_arr = []
    for x in X:
        prediction = saved_pipe.predict(x)
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

###################

def article_text_transform(data):

    input_data = pd.DataFrame.from_dict(data)
    input_data = data['title'].str.lower()
    input_data = input_data.apply(stemming)
    X = input_data.values

    return X 

def homepage_text_transform(data):

    X = []
    input_data = data['title'].str.lower()
    input_data = input_data.apply(stemming)
    X = input_data.values

    return X
    
    









