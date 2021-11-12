from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask import app

db  = SQLAlchemy()
def create_app(config_name):

    app = Flask(__name__)
    
    
    db.init_app(app)

    app.config.from_object(config_options[config_name])


    #regestering the blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #innitialising flask extensions
    


    return app