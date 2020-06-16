from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "hard to guess string"


class NameForm(FlaskForm):
    name = StringField("Bitte Namen eingeben:", validators=[DataRequired()])
    submit = SubmitField('Bestätigen')


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/user', methods=['GET', 'POST'])
def user():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('user.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True, port=8400)
