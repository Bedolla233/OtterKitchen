from flask import Flask, render_template, request, url_for
import requests, json
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import os



app = Flask(__name__)
bootstrap = Bootstrap5(app)

my_key = 'd53b43f7d9d14401a56568b6af67fe2e'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

csrf = CSRFProtect(app)
csrf.init_app(app)

endpoint1 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}'

endpoint2 = f'https://api.spoonacular.com/food/trivia/random?apiKey={my_key}'


endpoint3 = f'https://api.spoonacular.com/food/jokes/random?apiKey={my_key}'


@app.route("/")
def main():
    foodFacts = []

    for i in range(3):
        req = requests.get("https://api.spoonacular.com/food/trivia/random?apiKey=d53b43f7d9d14401a56568b6af67fe2e")
        data = req.json()
        singleFact = data.get('text')
        foodFacts.append(singleFact)
    
    jokesList = []
    endpoint3 = f'https://api.spoonacular.com/food/jokes/random?apiKey={my_key}'
    for i in range(3):
        req2 = requests.get('https://api.spoonacular.com/food/jokes/random?apiKey=d53b43f7d9d14401a56568b6af67fe2e')
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
def lunch():
    try:
        r = requests.get(endpoint2)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("lunch.html", data = data)


endpoint3 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&type=dinner&instructionsRequired=true'
@app.route("/dinner")
def dinner():
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
        
        endpoint4 = f'https://api.spoonacular.com/recipes/informationBulk?apiKey={my_key}&ids={foodData[0]},{foodData[4]},{foodData[2]}'
        foodR = requests.get(endpoint4)

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

#Search function
@app.route('/search', methods = ["POST"])
def search():
    form = SearchForm()
    values = []
    if form.validate_on_submit():
        word = request.form.get("searched")
        my_key = "&apiKey=d53b43f7d9d14401a56568b6af67fe2e"
        my_key2 = "?apiKey=d53b43f7d9d14401a56568b6af67fe2e"
        endpoint_search = 'https://api.spoonacular.com/recipes/complexSearch?query='+word+my_key

        r = requests.get(endpoint_search)
        data = r.json()
        number = data.get('number')
        if (type(number) is int):
            for entry in range(number):
                id = data.get("results")[entry].get('id')
                endpoint_ingredients = f'https://api.spoonacular.com/recipes/{id}/information'+my_key2
                r2 = requests.get(endpoint_ingredients)
                data2 = r2.json()
                values.append(data2)

        else:
            values.append("No search results")

    return render_template("search.html", form = form, values=values)
        
    
@app.context_processor
def base():
    form = SearchForm()
    return dict(form = form)
#Create searchform
class SearchForm(FlaskForm):
    searched = StringField("searched", validators=[DataRequired()])#Checks that the field is not empty
    submit = SubmitField("Submit")

