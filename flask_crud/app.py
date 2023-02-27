from flask import Flask,render_template, request, flash,redirect,url_for
from forms import RegForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import data

app= Flask(__name__)

app.config['SECRET_KEY']= 'ce58aced29237619be03c4695b76f6d3'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db= SQLAlchemy(app)

migrate= Migrate(app,db)
manager= Manager(app)
manager.add_command('db', MigrateCommand)

admin= Admin(app)
admin.add_view(ModelView(data,db.session))

class data(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(30),nullable=False)
    gender= db.Column(db.String(10),nullable=False)
    pwd= db.Column(db.String(10),nullable=False)
    
    def __repr__(self):
        return f"data('{self.id}','{self.name}','{self.gender}','{self.pwd}')"

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/post')
def post():
    return render_template('Posts.html')


@app.route('/reg', methods= ['GET', 'POST'])
def reg():
    form= RegForm()
    if request.method=='POST':
        if form.validate()== False:
            flash('All Fields are required','success')
            return render_template('Registration.html',form= form)
        else:
            id=form.id.data
            name=form.name.data
            gen=form.name.data
            pwd=form.name.data
            dtls= data(id=id, name=name, gender=gen, pwd=pwd)
            db.session.add(dtls)
            db.session.commit()
            return 'Registration Successfully!'
    
    return render_template('Registration.html',form= form)
   
@app.route('/Login', methods=['POST','GET'])
def login():
    form= LoginForm()
    if request.method=='POST':
        if form.validate()== False:
            flash('All Fields are required','Success')
            return render_template('Login.html',form= form)
        else:
            return redirect(url_for('/datareg'))
    return render_template('Login.html', form=form)




if __name__=='__main__':
    app.run(debug=True)