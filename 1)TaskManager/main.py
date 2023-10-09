from flask import Flask, render_template
from func import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign_in')
def sign_in():
    
    return render_template("login.html") 

@app.route('/sign_up')
def sign_up():

    return "hello world/sign_up"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091, load_dotenv=True,debug=True)