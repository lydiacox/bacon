from main import ma 
from models.food import Food
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class FoodSchema(ma.SQLAlchemyAutoSchema):
    food_id = auto_field(dump_only=True)
    food_name = auto_field(required=True, validate=Length(min=1))
    food_qty = auto_field(required=True)
    
    class Meta:
        model = Food
        load_instance = True
        
food_schema = FoodSchema()
multi_food_schema = FoodSchema(many=True)