# area das url e direcionamentos
from flask import render_template, url_for
from peterest import app
from flask_login import login_required

# mplementaçao
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)