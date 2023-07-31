from flask import Flask

app = Flask(__name__)
@app.route("/")
def bem_vindo():
    return "<h1>Seja bem vindo</h1>"
