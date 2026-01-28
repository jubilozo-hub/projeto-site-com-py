#importaçao de coisas que vao ser utilizadas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask_bcrypt import Bcrypt
from flask_login import LoginManager
# criaçao do app
app = Flask(__name__)
# configuraçao do app para receber uma base de dados sqlite da comunidade db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = ""
#criaçao da variavel database que avi armazenas as planilhas/informaçoes de usuario
database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
Login_Manager = LoginManager(app)
Login_Manager.login_view = "homepage"

from peterest import routs