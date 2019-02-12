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
def bbc():

    '''
    View page function that returns the profile page and its data
    '''

    title = 'Pitch Perfect'
    
    return render_template('profile.html', title=title)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_login(id):
    form = LoginForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('profile.html'))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)

