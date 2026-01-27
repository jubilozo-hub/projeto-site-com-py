#importaçao de coisas que vao ser utilizadas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# criaçao do app
app = Flask(__name__)
# configuraçao do app para receber uma base de dados sqlite da comunidade db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

#criaçao da variavel database que avi armazenas as planilhas/informaçoes de usuario
database = SQLAlchemy(app)

from peterest import routs