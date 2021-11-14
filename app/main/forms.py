from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms import validators
from wtforms.validators import Required, Email
from wtforms import ValidationError
from models import User

class regestrationForm(FlaskForm):
    username = StringField('Enter your name',validators=[Required()])
    email = StringField('Fill in your email',validators=[Required(), Email()])
    password = PasswordField('Correct password',validators=[Required()])
    password_confirm = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Sign Up')
    


