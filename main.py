from flask import Flask, redirect, render_template, session
from login_form import LoginForm
from add_post_form import AddPostForm
from reg_form import RegisterForm
from db import DB
from user_model import UserModel
from posts_model import PostModel
from flask import request
from PIL import Image
import os
import random


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
    all_photos = os.listdir("static")
    list_of_random_items = random.sample(all_photos, 3)
    # return render_template(
    #     'start_page.html',
    #     title='Три.ч - Свободное общение.',
    #     img1=list_of_random_items[0],
    #     img2=list_of_random_items[1],
    #     img3=list_of_random_items[2])
    return render_template('start_page.html', title='Три.ч - Свободное общение.')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_model = UserModel(db2.get_connection())
        user_model.insert(form.username.data, form.password.data)
        return redirect("/login")
    return render_template('register.html', title='Регистрация', form=form)


def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        raise RuntimeError('Width or height required!')

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size


@app.route('/add_post/<thread>', methods=['GET', 'POST'])
def add_post(thread):
    if 'username' not in session:
        return redirect('/login')

    form = AddPostForm()
    if request.method == 'POST':
        try:
            filename = request.files['file'].filename
            f = request.files['file']
            with open("static/" + filename, mode="wb") as file:
                a = f.read()
                file.write(a)

            file_path = os.path.join("static", filename)
            splited_fp = file_path.split(".")
            try:
                small_fp = splited_fp[0] + "_small." + splited_fp[1]
                scale_image(input_image_path=file_path,
                            output_image_path=small_fp,
                            width=500)
            except BaseException:
                small_fp = file_path
        except BaseException:
            small_fp = "1pixel.png"
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        u_name = session['username']
        pm = PostModel(db1.get_connection())
        pm.insert(thread, title, content, u_name, session['user_id'], small_fp)
        return redirect("/" + thread)
    return render_template(
        'add_post.html',
        title='Создание поста',
        form=form,
        username=session['username'])


@app.route('/delete_post/<thread>/<int:post_id>', methods=['GET'])
def delete_post(thread, post_id):
    if 'username' not in session:
        return redirect('/login')
    pm = PostModel(db1.get_connection())
    if session['username'] == 'admin':
        pm.delete_all(thread, post_id)
    pm.delete(thread, post_id, session['user_id'])
    return redirect("/" + thread)


@app.route('/thread1', methods=['GET', 'POST'])
def thread1():
    posts = PostModel(db1.get_connection()).get_all('thread1')
    try:
        return render_template(
            'thread1.html',
            username=session['username'],
            posts=posts)
    except BaseException:
        return render_template('thread1.html', posts=posts)


@app.route('/thread2', methods=['GET', 'POST'])
def thread2():
    posts = PostModel(db1.get_connection()).get_all('thread2')
    try:
        return render_template(
            'thread2.html',
            username=session['username'],
            posts=posts)
    except BaseException:
        return render_template('thread2.html', posts=posts)


@app.route('/thread3', methods=['GET', 'POST'])
def thread3():
    posts = PostModel(db1.get_connection()).get_all('thread3')
    try:
        return render_template(
            'thread3.html',
            username=session['username'],
            posts=posts)
    except BaseException:
        return render_template('thread3.html', posts=posts)


@app.route('/thread4', methods=['GET', 'POST'])
def thread4():
    posts = PostModel(db1.get_connection()).get_all('thread4')
    try:
        return render_template(
            'thread4.html',
            username=session['username'],
            posts=posts)
    except BaseException:
        return render_template('thread4.html', posts=posts)


@app.route('/thread5', methods=['GET', 'POST'])
def thread5():
    posts = PostModel(db1.get_connection()).get_all('thread5')
    try:
        return render_template(
            'thread5.html',
            username=session['username'],
            posts=posts)
    except BaseException:
        return render_template('thread5.html', posts=posts)


@app.route('/thread6', methods=['GET', 'POST'])
def thread6():
    posts = PostModel(db1.get_connection()).get_all('thread6')
    try:
        return render_template(
            'thread6.html',
            username=session['username'],
            posts=posts)
    except BaseException:
        return render_template('thread6.html', posts=posts)


@app.route('/thread7', methods=['GET', 'POST'])
def thread7():
    posts = PostModel(db1.get_connection()).get_all('thread7')
    try:
        return render_template(
            'thread7.html',
            username=session['username'],
            posts=posts)
    except BaseException:
        return render_template('thread7.html', posts=posts)


@app.route('/error', methods=['GET', 'POST'])
def error():
    return "error, unknown user"


@app.route('/logout')
def logout():
    session.pop('username', 0)
    session.pop('user_id', 0)
    return redirect('/start_page')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
