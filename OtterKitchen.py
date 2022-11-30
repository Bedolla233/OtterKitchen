from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

my_key = '601b6bca78294aaf9ea387a7157142bf'

endpoint1 = 'https://api.spoonacular.com/recipes/random?apiKey=601b6bca78294aaf9ea387a7157142bf'


@app.route("/random")
def index():
    try:
        r = requests.get(endpoint1)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template("random.html", data = data)

@app.route("/")
def main():
    return render_template("frontpage.html")

endpoint = 'https://api.spoonacular.com/recipes/random?apiKey=601b6bca78294aaf9ea387a7157142bf&number=3&tags=vegetarian&instructionsRequired=true'
@app.route("/vegetarian")
def veggie():
    try:
        r = requests.get(endpoint)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template("vegetarian.html", data = data)

endpoint = 'https://api.spoonacular.com/recipes/random?apiKey=601b6bca78294aaf9ea387a7157142bf&number=3&type=breakfast&instructionsRequired=true'
@app.route("/breakfast")
def breakfast():
    try:
        r = requests.get(endpoint)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template("breakfast.html", data = data)

endpoint = 'https://api.spoonacular.com/recipes/random?apiKey=601b6bca78294aaf9ea387a7157142bf&number=3&tags=lunch&instructionsRequired=true'
@app.route("/lunch")
def lunch():
    try:
        r = requests.get(endpoint)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template("lunch.html", data = data)

endpoint = 'https://api.spoonacular.com/recipes/random?apiKey=601b6bca78294aaf9ea387a7157142bf&number=3&tags=dinner&instructionsRequired=true'
@app.route("/dinner")
def dinner():
    try:
        r = requests.get(endpoint)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template("dinner.html", data = data)
