from flask import Blueprint, jsonify, request
from main import db
from models.food import Food

food = Blueprint('food', __name__)

@app.route('/')
def hello_world():
    """
    The homepage route. 
    
    This will later contain information about what classes are available to enroll in.
    '/' is the address here, which means it will be available from our host domain. 
    During production this is localhost:5000 or 127.0.0.1:5000
    """
    return "Hello, world! Check this out!"

@app.route('/login/', methods=["GET"])
def login():
    return "The login page"

@app.route('/signup/', methods=["POST"])
def signup():
    return "The signup page"

@app.route('/cook/', methods=["GET"])
def cook():
    return "The cooking page"