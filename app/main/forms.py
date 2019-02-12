from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class Login(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Submit')


class Register(FlaskForm):
    email = StringField('Email', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    password = StringField('Password', validators=[Required()])
    submit = SubmitField('Submit')


