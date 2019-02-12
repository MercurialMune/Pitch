from flask import render_template
from . import main


# Views
@main.route('/')
def index():

    '''
    View page function that returns the index page and its data
    '''
    title = 'Pitch Perfect'

    return render_template('index.html', title=title)


@main.route('/profile')
def bbc():

    '''
    View page function that returns the profile page and its data
    '''

    title = 'Pitch Perfect'
    
    return render_template('profile.html', title=title)

