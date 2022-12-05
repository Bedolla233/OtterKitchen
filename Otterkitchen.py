from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

my_key = '601b6bca78294aaf9ea387a7157142bf'

endpoint1 = 'https://api.spoonacular.com/recipes/random?apiKey=601b6bca78294aaf9ea387a7157142bf'

endpoint2 = 'https://api.spoonacular.com/food/trivia/random?apiKey=601b6bca78294aaf9ea387a7157142bf'

endpoint3 = 'https://api.spoonacular.com/food/jokes/random?apiKey=601b6bca78294aaf9ea387a7157142bf'




'''for i in range(3):
    req = requests.get(endpoint2)
    data = req.json()
    singleFact = data.get("text")
    foodFacts.append(singleFact)'''



@app.route("/")
def main():
    foodFacts = []
    for i in range(3):
        req = requests.get(endpoint2)
        data = req.json()
        singleFact = data.get("text")
        foodFacts.append(singleFact)
    
    jokesList = []
    for i in range(3):
        req2 = requests.get(endpoint3)
        data = req2.json()
        singleJoke = data.get("text")
        jokesList.append(singleJoke)

    return render_template("frontpage.html", foodFacts = foodFacts, jokesList=jokesList)



@app.route("/random")
def index():
    try:
        r = requests.get(endpoint1)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template("random.html", data = data)

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
