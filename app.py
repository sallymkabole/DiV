from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/sallym/DiV/todo.db'

db = SQLAlchemy(app)
class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(200)) 
    date = db.Column(db.DateTime)
    severity = db.Column(db.Integer) 
@app.route('/')
def todos():
    now= datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    dict =[
        {'id':1, 'name':'Exploratory Data Analysis', 'date':now ,'severity':2},
        {'id':2, 'name':'Cleaning Datasets', 'date':now ,'severity':4},
        {'id':3, 'name':'Data Scraping', 'date':now ,'severity':5}
    ]
    return render_template("tasks.html", result=dict)

if __name__ == '__main__':
    app.run()