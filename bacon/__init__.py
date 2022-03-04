from enum import unique
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

(
    db_user, 
    db_pass, 
    db_name, 
    db_domain
) = (os.environ.get(item) for item in [
    "DB_USER", 
    "DB_PASS", 
    "DB_NAME", 
    "DB_DOMAIN"
    ]
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Food(db.Model):
    __tablename__ = "food"
    food_id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(80), unique=True, nullable=False)
    food_qty = db.Column(db.Float(100), unique=False, nullable=False)

    def __init__(self, food_name):
        self.food_name = food_name

    @property
    def serialize(self):
        return {
            "food_id": self.food_id,
            "food_name": self.food_name,
            "food_qty": self.food_qty
        }

db.create_all()

@app.route('/')
def hello_world():
    """
    The homepage route. 
    
    This will later contain information about what classes are available to enroll in.
    '/' is the address here, which means it will be available from our host domain. 
    During production this is localhost:5000 or 127.0.0.1:5000
    """
    return "Hello, world! Check this out!"

if __name__ == '__main__':
    app.run(debug=True)