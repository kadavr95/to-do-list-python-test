from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "<h1><a href=\"http://dimini.tk\">Dimini Inc</a></h1>"

@app.route("/memes")
def memes():
    return send_from_directory("", "web.html")

app.run()
