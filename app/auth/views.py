from wtforms import form
from ..models import  User
from flask import  render_template, redirect, url_for
from . import auth
from .forms import RegistrationForm
from .. import db



@auth.route('/auth/register', methods = ['GET', 'POST'])
def regester():
    regester = RegistrationForm()
    if regester.validate_on_submit():
        user = User(email =form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))


    return  render_template('auth', regester.html, register_form = regester)
