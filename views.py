from flask import Blueprint, render_template, request, redirect, url_for 

view = Blueprint(__name__, "views")

@view.route("/")
def home():
    return render_template("Main.HTML", name="Ahmad")

@view.route("/")
def Go_to_Home():
    return redirect(url_for(view.home))