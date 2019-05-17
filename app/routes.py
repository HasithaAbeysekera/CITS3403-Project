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
from app.forms import RegistrationForm, PlayerEntryForm, PollCreateForm, PollNewEntryForm, PollVotingForm, PollNewEntryDropDown


@app.route('/')
@app.route('/index')
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
@login_required
def admin():
    if current_user.is_anonymous:
        return redirect(url_for('unauthorised'))
    if not current_user.admin:
        return redirect(url_for('unauthorised'))
    users = User.query.all()
    return render_template('admin.html', title='Admin Page', users=users)

@app.route('/unauthorised')
def unauthorised():
    return render_template('unauthorised.html', title='Error - You are unauthorised!')

@app.route('/playerlist')
def playerlist():
    playerlist = Player.query.all()
    return render_template('playerlist.html', playerlist=playerlist)    

@app.route('/playercreate', methods=['GET', 'POST'])
@login_required
def playercreate():
    form = PlayerEntryForm()
    if form.validate_on_submit():
        newplayer = Player(playername=form.playername.data, nationality=form.country.data, club=form.club.data)
        db.session.add(newplayer)
        db.session.commit()
        flash('Congratulations, you have added a new plyer')
        return redirect(url_for('playerlist'))
    return render_template('playercreate.html', form=form)   

@app.route('/polllist')
def polllist():
    polls = Polls.query.all()
    return render_template('polllist.html', polllist=polls)

@app.route('/poll/<pollid>', methods=['GET', 'POST'])
def poll(pollid):
    thispoll = Polls.query.filter_by(pollid=pollid).first()
    playervotes = PollPlayer.query.filter_by(pollid=pollid).all()
    uservotes = PollVote.query.filter_by(pollid=pollid)
    optionscount = PollPlayer.query.filter_by(pollid=pollid).count()
    if current_user.is_anonymous:
        thisuservoted = None
    else:
        thisuservoted = PollVote.query.filter_by(pollid=pollid, userid=current_user.id).first()
    form = PollVotingForm()
    form.entries.choices= [(player.playerid, player.playerentry.playername) for player in PollPlayer.query.filter_by(pollid=pollid).all()]
    form3 = PollNewEntryDropDown()
    form3.select.choices = [(option.playerid, option.playername) for option in Player.query.all()]
    if form.validate_on_submit():
        if current_user.is_anonymous or thisuservoted:
            return redirect(url_for('unauthorised'))
        if form.entries.data:    
            formplayerid = form.entries.data
            votedplayer = PollPlayer.query.filter_by(pollid=pollid, playerid=form.entries.data).first()
            votedplayer.votecount += 1
            newvote = PollVote(userid=current_user.id, pollid=pollid, playerid=formplayerid)
            db.session.add(newvote)
            db.session.commit()
        return redirect(url_for('poll', pollid=pollid))
    elif form3.validate_on_submit():
        if current_user.is_anonymous or thisuservoted:
            return redirect(url_for('unauthorised'))
        if form3.select.data:
            newresponseplayer = Player.query.filter_by(playerid=form3.select.data).first()
            dupecheck = PollPlayer.query.filter_by(pollid=thispoll.pollid, playerid=newresponseplayer.playerid).first()
            if dupecheck:
                dupecheck.votecount += 1
            else:
                newresponse = PollPlayer(pollid=thispoll.pollid, playerid=newresponseplayer.playerid, votecount='1')
                db.session.add(newresponse)
                db.session.commit()
            newvote = PollVote(userid=current_user.id, pollid=thispoll.pollid , playerid=newresponseplayer.playerid)
            db.session.add(newvote)
            db.session.commit()
        return redirect(url_for('poll', pollid=pollid))
    return render_template('poll.html', poll=thispoll, votes=playervotes, uservotes=uservotes, form=form, form3=form3, uservoted=thisuservoted, numvotes=optionscount)

@app.route('/pollcreate', methods=['GET', 'POST'])
@login_required
def pollcreate():
    form = PollCreateForm()
    # choices = [0,  "-- select an option --"]
    # choices = []
    
    form.select1.choices = [(option.playerid, option.playername) for option in Player.query.all()]
    form.select2.choices = [(option.playerid, option.playername) for option in Player.query.all()]
    form.select3.choices = [(option.playerid, option.playername) for option in Player.query.all()]
    
    if form.validate_on_submit():
        if current_user.is_anonymous:
            return redirect(url_for('unauthorised'))
        newpoll = Polls(pollname=form.pollname.data, creatorid=current_user.id)
        db.session.add(newpoll)
        db.session.commit()
        if form.select1.data:
            newpollplayer1 = PollPlayer(pollid=newpoll.pollid, playerid = form.select1.data, votecount ='0')
            db.session.add(newpollplayer1)
            db.session.commit()
        db.session.commit()
        if not form.select1.data == form.select2.data:
            newpollplayer2 = PollPlayer(pollid=newpoll.pollid, playerid = form.select2.data, votecount ='0')
            db.session.add(newpollplayer2)
            db.session.commit()
        if (form.select3.data == form.select1.data) or (form.select3.data == form.select2.data):
            db.session.commit()
        else: 
            newpollplayer3 = PollPlayer(pollid=newpoll.pollid, playerid = form.select3.data, votecount ='0')
            db.session.add(newpollplayer3)
            db.session.commit()
        flash('Congratulations, you have created a new poll')
        return redirect(url_for('polllist'))
    return render_template('pollcreate.html', form=form)

@app.route('/delplayer/<playerid>')
def delplayer(playerid):
    if not current_user.admin:
        return redirect(url_for('unauthorised'))
    PollVote.query.filter_by(playerid=playerid).delete()
    PollPlayer.query.filter_by(playerid=playerid).delete()
    Player.query.filter_by(playerid=playerid).delete()
    db.session.commit()
    return redirect(url_for('playerlist'))

@app.route('/delvote/<pollid>/<playerid>/<userid>')
def delvote(pollid, playerid, userid):
    if not current_user.admin:
        return redirect(url_for('unauthorised'))
    thisplayerVote = PollPlayer.query.filter_by(playerid=playerid, pollid=pollid).first()
    thisplayerVote.votecount -= 1
    thisvote = PollVote.query.filter_by(userid=userid, pollid=pollid, playerid=playerid).first()
    db.session.delete(thisvote)
    db.session.commit()
    return redirect(url_for('poll', pollid=pollid))

@app.route('/delpoll/<pollid>')
def delpoll(pollid):
    if not current_user.admin:
        return redirect(url_for('unauthorised'))
    Polls.query.filter_by(pollid=pollid).delete()
    PollPlayer.query.filter_by(pollid=pollid).delete()
    PollVote.query.filter_by(pollid=pollid).delete()
    db.session.commit()
    return redirect(url_for('polllist'))

@app.route('/deluser/<userid>')
def deluser(userid):
    if current_user.is_anonymous:
        return redirect(url_for('unauthorised'))
    if not current_user.admin:
        return redirect(url_for('unauthorised'))
    if current_user.id == userid:
        return redirect(url_for('unauthorised'))
        ##go thru pollvotes first
    uservotes = PollVote.query.filter_by(userid=userid).all()
    for vote in uservotes:
        playervote = PollPlayer.query.filter_by(pollid=vote.pollid, playerid=vote.playerid).first()
        playervote.votecount -= 1
        db.session.delete(vote)
        db.session.commit()
    
    createdpolls = Polls.query.filter_by(creatorid=userid).all()
    for poll in createdpolls:
        votes = PollVote.query.filter_by(pollid=poll.pollid).all()
        for onevote in votes:
            db.session.delete(onevote)
            db.session.commit()
        db.session.delete(poll)
        db.session.commit()
    User.query.filter_by(id=userid).delete()
    db.session.commit()
    return redirect(url_for('admin'))