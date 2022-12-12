from flask import Flask
from views import view

application = Flask(__name__)
application.config['SECRET_KEY'] = 'gfsgjkdjnkdjd fjskfgnjksngjlf'
application.register_blueprint(view, url_prefix="/")



