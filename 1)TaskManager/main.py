from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, logout_user
from func import *

#login_manager = LoginManager()
app = Flask(__name__)

app.config.from_object(__name__)

'''login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "info"#success
'''


@app.before_request
def before_request():
    '''Установление соединения с БД перед выполнением запроса'''
    
    global connection
    connection= sqlite3.connect('folio.db')
    global cursor 
    cursor = connection.cursor()
    #db = get_db()
    

@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    connection.close()



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign_in')
def sign_in():
    
    return render_template("login.html") 

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))

@app.route('/sign_up')
def sign_up():

    return "hello world/sign_up"

@app.route("/tasks")
@login_required
def tasks():

    return render_template("index.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091, load_dotenv=True,debug=True)