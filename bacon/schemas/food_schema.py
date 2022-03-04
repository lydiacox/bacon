from main import ma 
from models.food import Food
from marshmallow_sqlalchemy import auto_field

class FoodSchema(ma.SQLAlchemyAutoSchema):
    food_id = auto_field(dump_only=True)
    
    class Meta:
        model = Food
        load_instance = True
        
food_schema = FoodSchema()
multi_food_schema = FoodSchema(many=True)