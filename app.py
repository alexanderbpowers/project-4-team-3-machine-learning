from flask import Flask, render_template, redirect, request
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests

app = Flask(__name__)

#--------------------------------------
# Flask Routes (website URL's)
#--------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

#--------------------------------------
# Flask API CALLS (javascript calling python code)
#--------------------------------------

# test
@app.route("/api/exampleScrape")
def exampleScrape(testParameter):
    return testParameter

# web scrapper -  ARTICLES
@app.route("/api/ArticleScrape/<input>")
def article_reader(input):

    text = request.form['articleURLInput']

   # variables
    # url = input
    # response = requests.get(url)
    # soup = bs(response.text, 'html.parser')

    # title = soup.title.text.strip()

    # articles = soup.body.find_all('p')
    # article_text = ""
    # for article in articles:
    #     article_text += article.text

    # scraped_data = {
    #     'title' : title,
    #     'text' : article_text,
    # }

    return text

if __name__ == '__main__':
    app.run(debug=True)

