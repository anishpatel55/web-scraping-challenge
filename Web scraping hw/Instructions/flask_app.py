from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars.py"
mongo = PyMongo(app)

@app.route("/")
def home():
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", vacation=destination_data)


@app.route("/scrape")
def scrape():
    data = scrape_mars.scrape_info()

    mongo.db.collection.update({}, scrape_mars, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)