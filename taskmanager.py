from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/sallym/DiV/todo.db'

db = SQLAlchemy(app)


class Task(db.Model):
    name = db.Column(db.String(200), unique=True,
                     nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    severity = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, name,  severity):
      self.name = name
      
      self.severity = severity


@app.route('/', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
      if not request.form['name']  or not request.form['severity']:
         flash('Please enter all the fields', 'error')
      else:
         task = Task(request.form['name'], 
            request.form['severity'])

         db.session.add(task)
         db.session.commit()
         return redirect('/')
        
    else:
        tasks=Task.query.order_by(Task.date.desc()).all()
        return render_template("tasks.html", tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5055)
