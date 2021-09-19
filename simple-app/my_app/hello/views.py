from my_app import app 
from my_app.hello.models import MESSAGES

@app.route('/')
@app.route('/hello')
def hello_world():
    return MESSAGES['default']


@app.route('/show/<key>') # http://127.0.0.1:5000/show/key
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key


@app.route('/add/<key>/<message>') # http://127.0.0.1:5000/add/name/John
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added or Updated" % key
