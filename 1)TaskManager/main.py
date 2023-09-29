from flask import Flask
from func import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091, load_dotenv=True,debug=True)