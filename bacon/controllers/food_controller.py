from flask import Blueprint, jsonify, request, render_template
from main import db
from models.food import Food
from schemas.food_schema import food_schema, multi_food_schema

food = Blueprint('food', __name__)

@food.route('/', methods=["GET", "POST"])
def home():
    """
    The homepage route. 
    '/' is the address here, which means it will be available from our host domain. 
    During production this is localhost:5000 or 127.0.0.1:5000
    """
    data = {
        "page_title": "Eggs & Bacon",
    }
    if request.method == "GET":
        return render_template("index.html", page_data=data)
    pax = (request.form)
    adults = int(pax['adults'])
    children = int(pax['children'])
    return render_template("index.html", page_data=data)

# @food.route('/login/', methods=["GET"])
# def login():
#     data = {
#         "page_title": "Login",
#     }
#     return render_template("login.html", page_data=data)

# @food.route('/signup/', methods=["GET"])
# def signup():
#     data = {
#         "page_title": "Sign Up",
#     }
#     return render_template("signup.html", page_data=data)

@food.route('/cook/', methods=["GET"])
def results():
    data = {
        "page_title": "Let's Cook!",
    }
    return render_template("cook.html", page_data=data)

# @food.route("/foods/", methods=["GET"])
# def get_foods():
#     foods = Food.query.all()
#     return jsonify(food_schema.dump(foods))