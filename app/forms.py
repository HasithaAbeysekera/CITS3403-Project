from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import User, Player, Polls, PollPlayer, PollVote

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PlayerEntryForm(FlaskForm):
    playername = StringField('PlayerName', validators=[DataRequired()])
    country = StringField('Country')
    club = StringField('Club')
    submit = SubmitField('Submit')

    def validate_playername_dupe(self, playername):
        name = Player.query.filter_by(playername=playername.data).first()
        if name is not None:
            raise ValidationError('This player already exists.')

class PollCreateForm(FlaskForm):
    def player_choices():      
        return Player.query.all()
    
    pollname = StringField('Poll Name', validators=[DataRequired()])
    player1 = QuerySelectField(u'Skill level',      
                               validators=[DataRequired()],
                               query_factory=player_choices)
    #player2 = SelectField
    #player3 = SelectField
    #player4 = SelectField
    #player5 = SelectField
    submit = SubmitField('Submit')

class PollVotingForm(FlaskForm):
    newname = StringField('Player Name')
    submit = SubmitField('Submit')

    def validate_dupes(self, newname):
        new = Player.query.filter_by(playername=newname.data).first()
        if new is None:
            raise ValidationError('This player does not exist.')