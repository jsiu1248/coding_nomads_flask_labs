from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'hello_world'
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# instance of loginmanager
login_manager = LoginManager()
#endpoint if user logs into protected page
login_manager.login_view = 'auth.login'

# initialize login_manager
login_manager.init_app(app)

from blogger import models
from blogger import views

