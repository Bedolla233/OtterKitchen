from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

my_key = 'cd39d1a49e8a4ac994819fb6a1a19431'

endpoint1 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}'

endpoint2 = f'https://api.spoonacular.com/food/trivia/random?apiKey={my_key}'

endpoint3 = f'https://api.spoonacular.com/food/jokes/random?apiKey=cd39d1a49e8a4ac994819fb6a1a19431'

'''foodFacts = []
for i in range(3):
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
        singleFact = data.get('text')
        foodFacts.append(singleFact)
    
    jokesList = []
    endpoint3 = f'https://api.spoonacular.com/food/jokes/random?apiKey=cd39d1a49e8a4ac994819fb6a1a19431'
    for i in range(3):
        req2 = requests.get(endpoint3)
        data = req2.json()
        # print(data)
        singleJoke =  data.get('text')
        # print(singleJoke)
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


endpoint0 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&tags=vegetarian&instructionsRequired=true'
@app.route("/vegetarian")
def veggie():
    try:
        r = requests.get(endpoint0)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("vegetarian.html", data = data)

endpoint1 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&type=breakfast&instructionsRequired=true'
@app.route("/breakfast")
def breakfast():
    try:
        r = requests.get(endpoint1)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("breakfast.html", data = data)

endpoint2 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&type=lunch&instructionsRequired=true'
@app.route("/lunch")
def breakfast():
    try:
        r = requests.get(endpoint2)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("lunch.html", data = data)


endpoint3 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&type=dinner&instructionsRequired=true'
@app.route("/dinner")
def breakfast():
    try:
        r = requests.get(endpoint3)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("dinner.html", data = data)

endpoint4 = f'https://api.spoonacular.com/recipes/autocomplete?number=5&query=Sub&apiKey={my_key}'
@app.route("/sandwhich")
def sandwhich():
    foodData = []
    foodFinalData = []
    try:
        r = requests.get(endpoint4)
        data = r.json()
        # print(data[0])
        for i in data:
            foodData.append(i['id'])
            print(i['id'])
        # print(foodData)
        endpoint5 = f'https://api.spoonacular.com/recipes/informationBulk?apiKey={my_key}&ids={foodData[0]},{foodData[4]},{foodData[2]}'
        foodR = requests.get(endpoint5)
        foodFinalData = foodR.json()


    except:
        print('please try again')
    return render_template("sandwhich.html", data = foodFinalData)


endpoint6 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&type=vegan&instructionsRequired=true'
@app.route("/vegan")
def vegan():
    try:
        r = requests.get(endpoint6)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("vegan.html", data = data)