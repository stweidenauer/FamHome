import os
from flask import render_template, session, redirect, url_for, request, Blueprint
from fam_home.main.forms import (CalcForm, NameForm)
from fam_home.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def index():
    path_to_pictures = os.path.join('fam_home', 'static', 'pictures')
    pictures = []
    for picture in os.listdir(path_to_pictures):
        pictures.append(url_for('static', filename='pictures/' + picture))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('Index.html', pictures=pictures, posts=posts)


@main.route('/benutzer', methods=['GET', 'POST'])
def benutzer():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for("main.benutzer"))
    return render_template('benutzer.html', form=form, name=session.get('name'))


@main.route('/calc', methods=['GET', 'POST'])
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
