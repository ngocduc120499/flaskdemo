from flask import Flask,Blueprint, app
from flask_sqlalchemy import SQLAlchemy
from .views import main
from .extensions import db
def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/qlsv'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main)
   
    return app
    