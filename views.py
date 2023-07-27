from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

# home route
@views.route("/")
def home():
    return render_template("index.html")

# contact route
@views.route("/contact")
def contact():
    return render_template("contact.html")

# redirection route
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))