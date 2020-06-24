from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "hard to guess string"


class NameForm(FlaskForm):
    name = StringField("Bitte Namen eingeben:", validators=[DataRequired()])
    submit = SubmitField('Bestätigen')


class CalcForm(FlaskForm):
    add1 = IntegerField("Erster Summand:", validators=[DataRequired()])
    add2 = IntegerField("Zweiter Summand:", validators=[DataRequired()])
    submit = SubmitField('+')


class SubBtn(FlaskForm):
    submit = SubmitField('Passiert was')


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/user', methods=['GET', 'POST'])
def user():
    name = None
    text = ''
    form = NameForm()
    form2 = SubBtn()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    if form2.validate_on_submit():
        text = "Ein wichtiger Text"
    return render_template('user.html', form=form, form2=form2, name=name, text=text)


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    add1 = None
    add2 = None
    result = 0
    form = CalcForm()
    if form.validate_on_submit():
        add1 = form.add1.data
        form.add1.data = ''
        add2 = form.add2.data
        result = add1 + add2
    return render_template('calc.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=8400)
