from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    '''
        News class to define User Objects
        '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username, self.password, self.email}'


class Pitch:
    '''
    News class to define Pitch Objects
    '''

    def __init__(self, id):
        self.id= id




#
# class Login:
#     '''
#         News class to define User Objects
#         '''
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#
# class Register:
#     '''
#         News class to define User Objects
#         '''
#     def __init__(self, email, username, password):
#         self.email = email
#         self.username = username
#         self.password = password
