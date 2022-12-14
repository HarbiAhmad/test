
import os
from flask import Flask, request, url_for, redirect, render_template

application = Flask(__name__)

@application.route('/')
def hello():
    return redirect(url_for('Main'))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)



#from flask import Flask, render_template, request, redirect, url_for 
#from views import view

#application = Flask(__name__)
#application.config['SECRET_KEY'] = 'gfsgjkdjnkdjd fjskfgnjksngjlf'
#application.register_blueprint(view, url_prefix="/")

#@application.route("/")
#def home():
    #return render_template("Main.HTML", name="Ahmad")
    #return 'hhhhh'
    #return redirect()