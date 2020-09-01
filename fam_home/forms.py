from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from fam_home.models import User


class NameForm(FlaskForm):
    name = StringField("Bitte Namen eingeben:", validators=[DataRequired()])
    submit = SubmitField('Bestätigen')


class CalcForm(FlaskForm):
    add1 = IntegerField("Erster Summand:", validators=[DataRequired()])
    add2 = IntegerField("Zweiter Summand:", validators=[DataRequired()])
    submit = SubmitField('+')


class LogInForm(FlaskForm):
    email = StringField("Email Adress: ", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Bestätigen')


class RegisterForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    email = StringField("Email Adress: ", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken...')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken...')
