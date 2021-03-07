from flask import Blueprint,Flask,render_template,request,redirect,url_for,flash
from .extensions import Data
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
main = Blueprint('main', __name__)

@main.route('/')
def Index():
    all_data = Data.query.all()
    
    return render_template("index.html", employees = all_data)
