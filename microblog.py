from app import app, db
from app.models import User, Post, Player, Poll, PollVote

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Player': Player, 'Poll': Poll, 'PollVote': PollVote}