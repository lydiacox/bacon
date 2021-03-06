from flask import Blueprint, jsonify, request, render_template
from main import db
from models.food import Food
from schemas.food_schema import food_schema, multi_food_schema

food = Blueprint('food', __name__)

menu= {
    "bacon": .125,
    "eggs": 2
}

def dozen(num):
    if not num % 12:
        return int(num / 12)
    elif num % 12 > 6:
        return (round(num//12)) + 1
    else:
        return (round(num//12)) + .5

def calculate_pax(pax):
    adults, children = pax['adults'], pax['children']
    if adults:
        adults = int(adults)
    else:
        adults = 0
    if children:
        children = int(children)
    else:
        children = 0
    total_pax = adults + (children *.5)
    return total_pax

def quantities(total_pax):
    bacon = round(total_pax * menu["bacon"], 1)
    eggs = int(total_pax * menu["eggs"])
    return bacon, eggs

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
    total_pax = calculate_pax(pax)
    if total_pax > 1000:
        return render_template("toomuch.html", page_data=data)
    qty = quantities(total_pax)
    dozens = dozen(qty[1])
    data = {
        "page_title": "Let's cook!",
        "bacon": str(qty[0]),
        "eggs": str(qty[1]),
        "dozen": str(dozens)
    }
    return render_template("cook.html", page_data=data)

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

# @food.route('/cook/', methods=["GET"])
# def results():
#     data = {
#         "page_title": "Let's Cook!",
#     }
#     return render_template("cook.html", page_data=data)

# @food.route("/foods/", methods=["GET"])
# def get_foods():
#     foods = Food.query.all()
#     return jsonify(food_schema.dump(foods))