from flask import Flask, redirect, render_template, session
from login_form import LoginForm
from add_post_form import AddPostForm
from reg_form import RegisterForm
from db import DB
from user_model import UserModel
from posts_model import PostModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db1 = DB('posts.db')
db2 = DB('users.db')

def exits(args):
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_model = UserModel(db2.get_connection())
        exists = user_model.exists(user_name, password)
        if (exists[0]):
            session['username'] = user_name
            session['user_id'] = exists[1]
        return redirect("/start_page")
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/start_page', methods=['GET', 'POST'])
def start_page():
    return render_template('start_page.html', title='Три.ч - Свободное общение.')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_model = UserModel(db2.get_connection())
        user_model.insert(form.username.data, form.password.data)
        return redirect("/login")
    return render_template('register.html', title= 'Регистрация', form=form)

@app.route('/add_post/<thread>', methods=['GET', 'POST'])
def add_post(thread):
    if 'username' not in session:
        return redirect('/login')
    form = AddPostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        u_name = session['username']
        pm = PostModel(db1.get_connection())
        pm.insert(thread, title, content, u_name, session['user_id'])
        return redirect("/index")
    return render_template('add_post.html', title='Создание поста', form=form, username=session['username'])


@app.route('/delete_post/<thread>/<int:post_id>', methods=['GET'])
def delete_post(thread, post_id):
    print(thread)
    if 'username' not in session:
        return redirect('/login')
    pm = PostModel(db1.get_connection())
    pm.delete(thread, post_id)
    return redirect("/index")


@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect('/login')
    posts = PostModel(db1.get_connection()).get_all('thread1')
    return render_template('index.html', username=session['username'], posts=posts)


@app.route('/error', methods=['GET', 'POST'])
def error():
    return "error, unknown user"


@app.route('/logout')
def logout():
    session.pop('username',0)
    session.pop('user_id',0)
    return redirect('/login')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
