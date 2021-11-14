
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from . import db



class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(),unique=True,)
    password = db.Column(db.String(80), unique=True)

    @property
    def password(self):
        raise AttributeError('You can not read the password attribute')

    def password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self,password ):
        return check_password_hash(self.password,password)

    def __repr__(self):
            return f'User{self.username}'