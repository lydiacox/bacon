from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    # Create the flask app object
    app = Flask(__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)

    # if __name__ == '__main__':
    #     app.run(debug=True)

    # Register our routes
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app