from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)


app.config['SECRET_KEY'] = '738c359d905a2063b0bbffd11a30de51'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meusite.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça Login para acessar a página'
login_manager.login_message_category = 'alert-info'


from estudoboladao import routes