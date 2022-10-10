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

filename = 'nlp_logistical_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

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
        'prediction' : prediction 
    }

    X = text_transform(scraped_data)
    prediction = loaded_model.predict(X)

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

###################

def text_transform(data):

    input_data = pd.DataFrame.from_dict(data)
    input_data['text'] = input_data['text'].apply(stemming)
    X = input_data['text'].values
    vectorizer = TfidfVectorizer()
    vectorizer.fit(X)
    X = vectorizer.transform(X)

    return X 









