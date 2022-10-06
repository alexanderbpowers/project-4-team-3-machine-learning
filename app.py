from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import news_scraper_app
# import pymongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/news_ddb"
mongo = PyMongo(app)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    scraped_data = news_scraper_app.scraper()
    mongo.db.news_db.replace_one({}, scraped_data, upsert=True)
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)

