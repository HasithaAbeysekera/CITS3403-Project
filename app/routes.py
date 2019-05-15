from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from flask_login import logout_user
from app.models import User, Polls, PollVote, PollPlayer, Player
from app import app
from app.forms import LoginForm
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm, PlayerEntryForm, PollCreateForm


@app.route('/')
@app.route('/index')
#@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/admin')
def admin():
    if not current_user.admin:
        return redirect(url_for('unauthorised'))
    return render_template('admin.html', title='Admin Page')

@app.route('/unauthorised')
def unauthorised():
    return render_template('unauthorised.html', title='Error - You are unauthorised!')

@app.route('/polllist')
def polllist():
    polls = Polls.query.all()
    return render_template('polllist.html', polllist=polls)

@app.route('/poll/<pollid>')
#def poll(pollid):
##    poll = Polls.query.filter_by(pollid=pollid).first()
#    return render_template('poll.html', poll=pollid)

def poll(pollid):
    thispoll = Polls.query.filter_by(pollid=pollid).first()
    playervotes = PollPlayer.query.filter_by(pollid=pollid)
    uservotes = PollVote.query.filter_by(pollid=pollid)
    return render_template('poll.html', poll=thispoll, votes=playervotes, uservotes=uservotes)

@app.route('/pollcreate', methods=['GET', 'POST'])
def pollcreate():
    form = PollCreateForm()
    if form.validate_on_submit():
        newpoll = Polls(pollname=form.pollname.data, creatorid=current_user.id)
        newpollplayer1 = PollPlayer(pollid=newpoll.pollid, playerid = form.player1.data.playerid, votecount ='0')
        db.session.add(newpoll)
        db.session.commit()
        newpollplayer1 = PollPlayer(pollid=newpoll.pollid, playerid = form.player1.data.playerid, votecount ='0')
        db.session.add(newpollplayer1)
        db.session.commit()
        flash('Congratulations, you have created a new poll')
        return redirect(url_for('index'))
    return render_template('pollcreate.html', form=form)