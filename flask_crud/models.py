from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']= 'ce58aced29237619be03c4695b76f6d3'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db= SQLAlchemy(app)

class data(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(30),nullable=False)
    gender= db.Column(db.String(10),nullable=False)
    pwd= db.Column(db.String(10),nullable=False)
    
    def __repr__(self):
        return f"data('{self.id}','{self.name}','{self.gender}','{self.pwd}')"