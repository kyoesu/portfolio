from flask import Flask, render_template
from func import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/ind')
def ind():
    return render_template("index.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091, load_dotenv=True,debug=True)