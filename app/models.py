from . import db


class Pitch:
    '''
    News class to define Pitch Objects
    '''

    def __init__(self, id):
        self.id= id


class User:
    '''
        News class to define User Objects
        '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Login:
    '''
        News class to define User Objects
        '''
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Register:
    '''
        News class to define User Objects
        '''
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
