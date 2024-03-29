from flask_sqlalchemy import SQLAlchemy
import datetime
from blogger import app, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)
    dateofreg = db.Column(db.DateTime, default=datetime.datetime.now)

    # should password be take out of this? Can it be queried?
    # def __init__(self, firstname, lastname, username, password, email):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.username = username
    #     self.password = password
    #     self.email = email
    
    # errors out when someone tries to read it
    @property
    def password(self):
        raise AttributeError('password is not readable')

    # allow user to write password
    @password.setter
    def password(self, password):
       # flask already has a function that helps with hashing and adding salt
        self.password_hash = generate_password_hash(password)

    # it takes the password and hash together and returns true if correct
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # login manager needs help with getting users
    # LoginManager will call load_user() to find out info about users
    # takes an id and returns the user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    puid = db.Column(db.Integer, db.ForeignKey('users.id'))

    # def __init__(self, title, description, puid):
    #     self.title = title
    #     self.description = description
    #     self.puid = puid


db.create_all()
