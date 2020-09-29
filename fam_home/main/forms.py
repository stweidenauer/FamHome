from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField("Bitte Namen eingeben:", validators=[DataRequired()])
    submit = SubmitField('Bestätigen')


class CalcForm(FlaskForm):
    add1 = IntegerField("Erster Summand:", validators=[DataRequired()])
    add2 = IntegerField("Zweiter Summand:", validators=[DataRequired()])
    submit = SubmitField('+')
