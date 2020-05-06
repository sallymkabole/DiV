from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/sallym/DiV/todo.db'

db = SQLAlchemy(app)
class Task(db.Model): 
    name = db.Column(db.String(200), unique=True, nullable=False, primary_key=True) 
    date = db.Column(db.DateTime)
    severity = db.Column(db.Integer) 
@app.route('/', methods=['POST', 'GET'])
def todos():
    resultsList = []
    if request.form:
        task = Task(name=request.form.get("name"))
        db.session.add(name)
        db.session.commit()
    return render_template("tasks.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5055)