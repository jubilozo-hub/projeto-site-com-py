from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "bem vindo cadastre-se, e adicione seu bb."

if __name__ == "__main__":
    app.run(debug=True)