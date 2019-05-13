from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))  

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, index=False, default=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Player(db.Model):

    __table_args__ = (db.UniqueConstraint("firstname", "lastname"),)
    
    playerid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, unique=False)
    lastname = db.Column(db.String(64), index=True, unique=False)
    nationality = db.Column(db.String(64), index=True, unique=False)
    club = db.Column(db.String(64), index=True, unique=False)
    
    
    #sd

    def __repr__(self):
        return 'Player: {} {}, Club: {}, Country {}'.format(self.firstname, self.lastname, self.club, self.nationality)

class Poll(db.Model):
    pollid = db.Column(db.Integer, primary_key=True)
    creatorid = db.Column(db.Integer, db.ForeignKey('user.id'))
    #timecreated =
    #db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #timeleft = 

class PollVote(db.Model):
    voteid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    pollid = db.Column(db.Integer, db.ForeignKey('poll.pollid'))
    playerid = db.Column(db.Integer, db.ForeignKey('player.playerid'))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)