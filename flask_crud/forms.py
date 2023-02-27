from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,RadioField,IntegerField
from wtforms.validators import DataRequired,EqualTo

class RegForm(FlaskForm):
    id = IntegerField('ID : ',validators=[DataRequired()])
    name= StringField('Enter Name : ',validators=[DataRequired()])
    gender= RadioField('Gender : ',choices=[('M','Male'),('F','Female')])
    pwd= PasswordField('Password : ',validators=[DataRequired()])
    cpwd= PasswordField('ConfirmPassword : ',validators=[DataRequired(), EqualTo('pwd')])
    submit= SubmitField('Sign Up')
                       
class LoginForm(FlaskForm):
    id = IntegerField('ID : ',validators=[DataRequired()])
    pwd= PasswordField('Password',validators=[DataRequired()])
    submit= SubmitField('Login')