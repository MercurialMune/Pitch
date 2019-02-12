from flask import render_template
from . import main


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Mercurial News Highlights'

    return render_template('index.html', title=title)


@main.route('/highlights/bbc')
def bbc():

    '''
    View root page function that returns the bbc highlights page and its data
    '''

    bbc_news = get_bbc_news()
    print(bbc_news)
    title = 'Mercurial News Highlights'

    return render_template('bbc-highlights.html', title=title, bbc_news=bbc_news)

