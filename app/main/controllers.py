from flask import render_template
from . import main

@main.route("/")
def home():
    msg = "Hello world from tech-dev"
    return render_template("main/home.html", msg=msg)

