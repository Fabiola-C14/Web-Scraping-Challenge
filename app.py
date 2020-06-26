from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():

    website = mongo.db.website.find_one()
    return render_template("index.html", website=website)


@app.route("/scrape")
def scraper():
    website=mongo.db.website
    website_data =scrape_mars.scrape_info()
    print(website_data)
    website.update({}, website_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
