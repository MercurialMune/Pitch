from flask import render_template
from . import main
# from ..models import user
from.forms import LoginForm, RegisterForm


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


@main.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()

    title = 'Pitch Perfect'
    return render_template('login.html', title = title, form=form)


@main.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()

    title = 'Pitch Perfect'
    return render_template('login.html', title = title, form=form)

