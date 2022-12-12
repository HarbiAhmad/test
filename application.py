from flask import Flask, render_template, request, redirect, url_for 
#from views import view

application = Flask(__name__)
#application.config['SECRET_KEY'] = 'gfsgjkdjnkdjd fjskfgnjksngjlf'
#application.register_blueprint(view, url_prefix="/")

@application.route("/")
def home():
    return render_template("Main.HTML", name="Ahmad")
    #return 'hhhhh'
