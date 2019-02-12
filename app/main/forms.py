from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Submit')


