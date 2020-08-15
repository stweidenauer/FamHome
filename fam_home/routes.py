import os
from flask import render_template, session, redirect, url_for
from fam_home import app
from fam_home.forms import CalcForm, NameForm, LogInForm, RegisterForm
from fam_home.models import User, Post


@app.route('/')
def index():
    path_to_pictures = os.path.join('fam_home', 'static', 'pictures')
    pictures = []
    # path ist cwd
    # erstellt eine Liste aller Pfadangaben,
    # aller Bilder im Verzeichnis /static/pictures
    for picture in os.listdir(path_to_pictures):
        pictures.append(os.path.join(path_to_pictures, picture))
    print(pictures)
    return render_template('Index.html', pictures=pictures)


@app.route('/user', methods=['GET', 'POST'])
def user():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for("user"))
    return render_template('User.html', form=form, name=session.get('name'))


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    add1 = None
    add2 = None
    result = 0
    form = CalcForm()
    if form.validate_on_submit():
        add1 = form.add1.data
        # form.add1.data = ''
        add2 = form.add2.data
        result = add1 + add2
    return render_template('calc.html', form=form, result=result)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        print("whatever")
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("whatever")
    return render_template('register.html', form=form)
