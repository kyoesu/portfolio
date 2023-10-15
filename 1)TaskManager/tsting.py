'''
1. Регистрация и аутентификация пользователя:
    - Регистрация нового пользователя с использованием логина и пароля.
    - Аутентификация пользователя с проверкой соответствия введенных данных.

2. Создание задач:
    - Возможность создания новой задачи с указанием заголовка, описания и даты выполнения.
    - Сохранение задачи в базе данных.

3. Просмотр и редактирование задач:
    - Отображение списка задач пользователя.
    - Возможность редактирования заголовка, описания и даты выполнения задачи.
    - Возможность пометить задачу как выполненную или удалить ее.

4. Фильтрация и сортировка задач:
    - Возможность фильтровать задачи по статусу (выполненные, невыполненные) или дате выполнения.
    - Сортировка задач по дате создания или дате выполнения.

5. Уведомления:
    - Отправка уведомлений пользователю о приближающихся сроках выполнения задач.
    - Оповещение пользователя о выполнении задачи другим пользователем (если такая возможность требуется).

6. Безопасность и защита данных:
    - Хранение паролей пользователей в зашифрованном виде.
    - Защита от несанкционированного доступа к данным и функциям приложения.

7. Дизайн и интерфейс:
    - Создание пользовательского интерфейса с помощью HTML, CSS и возможно JavaScript.
    - Разработка привлекательного и интуитивно понятного дизайна.

8. Тестирование и отладка:
    - Создание модульных и функциональных тестов для проверки работоспособности функций приложения.
    - Отладка и исправление ошибок, выявленных в процессе тестирования.

9. Документация:
    - Создание документации, описывающей функциональность и использование приложения.
'''

"""
рег/аунт.

1. Установите Flask-Login:
   
   pip install flask-login
   

2. Создайте модель пользователя:
   - Создайте таблицу в базе данных SQLite для хранения информации о пользователях (например, User).
   - В модели User определите необходимые поля, такие как id, username, password и другие по вашему усмотрению.
   - Реализуйте методы get_id(), is_authenticated(), is_active() и is_anonymous() в модели User.

3. Создайте формы для регистрации и входа:
   - Используйте Flask-WTF или другую библиотеку для создания форм.
   - Создайте форму для регистрации с полями, такими как username, password и подтверждение пароля.
   - Создайте форму для входа с полями username и password.

4. Создайте представления (views) для регистрации и входа:
   - Создайте представление для регистрации, которое обрабатывает POST-запросы, проверяет данные формы, создает нового пользователя и сохраняет его в базе данных.
   - Создайте представление для входа, которое обрабатывает POST-запросы, проверяет данные формы, аутентифицирует пользователя и устанавливает сеанс.

5. Используйте Flask-Login для управления сеансами:
   - Импортируйте LoginManager из Flask-Login и настройте его в вашем приложении.
   - Определите функцию load_user(user_id), которая загружает пользователя по его идентификатору.
   - Используйте декоратор @login_required для защиты доступа к определенным представлениям, которым нужна аутентификация пользователя.

6. Добавьте вспомогательные функции:
   - Реализуйте функцию для проверки учетных данных пользователя (например, check_credentials(username, password)), чтобы убедиться, что пользователь с указанным именем пользователя и паролем существует в базе данных.

7. Добавьте ссылки на регистрацию и вход на вашу веб-страницу:
   - Создайте шаблоны Jinja2 для отображения форм и ссылок на регистрацию и вход.
   - Добавьте ссылки на страницы регистрации и входа на вашу веб-страницу.
"""

"""
уведы

Для реализации уведомлений в веб-приложении на Python с использованием Flask, вы можете использовать различные подходы, в зависимости от ваших требований и предпочтений. Вот несколько вариантов, которые можно рассмотреть:

1. Уведомления через электронную почту:
   - Используйте стандартную библиотеку Python smtplib для отправки электронных писем.
   - Приближающиеся сроки выполнения задачи могут быть отправлены пользователю по электронной почте.
   - Реализуйте функцию, которая будет отправлять электронные письма с уведомлениями о задачах.

2. Уведомления через веб-сокеты:
   - Используйте библиотеку Flask-SocketIO для реализации веб-сокетов в вашем приложении.
   - Приближающиеся сроки выполнения задачи могут быть отправлены пользователю через веб-сокеты.
   - Реализуйте функцию, которая будет отправлять уведомления о задачах через веб-сокеты.

3. Уведомления через внешний сервис:
   - Используйте внешний сервис для отправки уведомлений, такой как Firebase Cloud Messaging (FCM) или Pusher.
   - Подключите ваше веб-приложение к выбранному сервису и отправляйте уведомления о задачах через него.
   - Реализуйте функцию, которая будет отправлять уведомления о задачах через выбранный внешний сервис.


"""

"""
регистрация - flask-login
формы для регстрации - flask-WTF
для управления сессиями - flask-login, LoginManager


для уведомлений - flask-SoketIO
для уведомлений по почте - smtplib



"""

import os
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import sqlite3

DATABASE = '/flsite.db'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'folio.db')))

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id, dbase)

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None
@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
def index():
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())

@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category = 'error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template('add_post.html', menu = dbase.getMenu(), title="Добавление статьи")


@app.route("/post/<alias>")
@login_required
def showPost(alias):
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)

@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == "POST":
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            rm = True if request.form.get('remainme') else False
            login_user(userlogin, remember=rm)
            return redirect(request.args.get("next") or url_for("profile"))

        flash("Неверная пара логин/пароль", "error")

    return render_template("login.html", menu=dbase.getMenu(), title="Авторизация")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
            and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('login'))
            else:
                flash("Ошибка при добавлении в БД", "error")
        else:
            flash("Неверно заполнены поля", "error")

    return render_template("register.html", menu=dbase.getMenu(), title="Регистрация")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return f"""<p><a href="{url_for('logout')}">Выйти из профиля</a>
                <p>user info: {current_user.get_id()}"""



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091, load_dotenv=True,debug=True)



