from flask import render_template
from . import main
# from ..models import user
from.forms import LoginForm, RegisterForm
from flask_login import login_required


# Views
@main.route('/')
def index():

    '''
    View page function that returns the index page and its data
    '''
    title = 'Pitch Perfect'

    return render_template('index.html', title=title)


@main.route('/profile')
def profile():

    '''
    View page function that returns the profile page and its data
    '''

    title = 'Pitch Perfect'
    
    return render_template('profile.html', title=title)


# @main.route('/login', methods = ['GET','POST'])
# # @login_required
# def login():
#     logform = LoginForm()
#
#     title = 'Pitch Perfect'
#     return render_template('login.html', title = title, logform=logform)
#
#
# @main.route('/register', methods = ['GET','POST'])
# def register():
#     regform = RegisterForm()
#
#     title = 'Pitch Perfect'
#     return render_template('register.html', title = title, regform=regform)
#
