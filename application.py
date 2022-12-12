from flask import Flask

application = Flask(__name__)
application.config['SECRET_KEY'] = 'gfsgjkdjnkdjd fjskfgnjksngjlf'

@application.route('/')

def hllow():
    return 'High'

