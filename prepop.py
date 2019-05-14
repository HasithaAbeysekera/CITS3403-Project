import os
from app import app, db
from app.models import User, Post, Player, Polls, PollVote

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'app.db')


#create users
u1 = User(id='00000000', username = 'Hasi', email = 'hasi@test.com', admin = True)
u2 = User(id='11111111', username = 'Sam', email = 'sam@test.com', admin = True)
u3 = User(id='22222222', username = 'Tom', email = 'tom@test.com', admin = False)
u1.set_password('Hasitest1')
u2.set_password('Samtest1')
u3.set_password('Tomtest1')
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)

#create Players
p1= Player(playerid = '01', playername='Lionel Messi', nationality = 'Argentina', club = 'Barcelona')
p2= Player(playerid = '02', playername='Cristiano Ronaldo', nationality = 'Portugal', club = 'Juventus')
p3= Player(playerid = '03', playername='Manuel Neuer', nationality = 'Germany', club = 'Bayern Munich')
p4= Player(playerid = '04', playername='Neymar', nationality = 'Brazil', club = 'Barcelona')
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)


#createPolls
po1= Polls(pollid='1', pollname='Best Barca Player', creatorid='00000000')
po2= Polls(pollid='2', pollname='Best Player', creatorid='11111111')
po3= Polls(pollid='3', pollname='Best Player #2', creatorid='22222222')
db.session.add(po1)
db.session.add(po2)
db.session.add(po3)

#startvoting
pv1= PollVote(voteid='1', userid='00000000', pollid='1', playerid='01')
pv2= PollVote(voteid='2', userid='11111111', pollid='1', playerid='01')
pv3= PollVote(voteid='3', userid='22222222', pollid='1', playerid='04')

pv4= PollVote(voteid='4', userid='00000000', pollid='2', playerid='02')
pv5= PollVote(voteid='5', userid='11111111', pollid='2', playerid='03')
pv6= PollVote(voteid='6', userid='22222222', pollid='2', playerid='04')

pv7= PollVote(voteid='7', userid='00000000', pollid='3', playerid='01')
pv8= PollVote(voteid='8', userid='11111111', pollid='3', playerid='04')
pv9= PollVote(voteid='9', userid='22222222', pollid='3', playerid='02')
db.session.add(pv1)
db.session.add(pv2)
db.session.add(pv3)
db.session.add(pv4)
db.session.add(pv5)
db.session.add(pv6)
db.session.add(pv7)
db.session.add(pv8)
db.session.add(pv9)

db.session.commit()    