from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import Required, Length, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField('username..', validators=[Required()])
    email = StringField('email...',validators=[Required(), Email()])
    password = PasswordField('Enter password...',validators=[Required(),Length(min=6, max=15)])
    confirm_psw = PasswordField('confirm pass...',validators=[Required(),EqualTo(password)])
    submit = SubmitField('Sign up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')