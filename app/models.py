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
    createdpolls = db.relationship('Polls', backref='creator', lazy='dynamic')
    voter = db.relationship('PollVote', backref='voter', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Player(db.Model):

    playerid = db.Column(db.Integer, primary_key=True)
    playername = db.Column(db.String(128), index=True, unique=True)
    nationality = db.Column(db.String(64), index=True, unique=False)
    club = db.Column(db.String(64), index=True, unique=False)
    presentpoll = db.relationship('PollPlayer', backref='playerentry', lazy='dynamic')
    presentvote = db.relationship('PollVote', backref='playervotename', lazy='dynamic')

    def __repr__(self):
        return 'Player: {}, Club: {}, Country {}'.format(self.playername, self.club, self.nationality)


class Polls(db.Model):
    pollid = db.Column(db.Integer, primary_key=True)
    pollname = db.Column(db.String(64), index=True, unique=False)
    creatorid = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class PollVote(db.Model):
    voteid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    pollid = db.Column(db.Integer, db.ForeignKey('polls.pollid'))
    playerid = db.Column(db.Integer, db.ForeignKey('player.playerid'))


class PollPlayer(db.Model):
    pollplayerid = db.Column(db.Integer, primary_key=True)
    pollid =  db.Column(db.Integer, db.ForeignKey('polls.pollid'))
    playerid = db.Column(db.Integer, db.ForeignKey('player.playerid'))
    votecount = db.Column(db.Integer)

    def check_poll_dupe(self, thispollid, thisplayerid):
        return PollPlayer.query.filter_by(pollid=thispollid, playerid=thisplayerid).first()