from main import db

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