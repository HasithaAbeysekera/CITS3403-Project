import unittest, os
from app import app, db, login
from app.models import User, Polls, PollVote, PollPlayer, Player

class UserModelCase(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
        u1 = User(id='1', username = 'Hasi', email = 'hasi@test.com', admin = True)
        u2 = User(id='2', username = 'Sam', email = 'sam@test.com', admin = True)
        u3 = User(id='3', username = 'Tom', email = 'tom@test.com', admin = False)
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='Hasi')
        u.set_password('hasitest')
        self.assertFalse(u.check_password('password1'))
        self.assertTrue(u.check_password('hasitest'))

    def test_admin(self):
        u1 = User.query.filter_by(username='Hasi').first()
        u3 = User.query.filter_by(username='Tom').first()
        self.assertTrue(u1.admin)
        self.assertFalse(u3.admin)

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 

class PollsModelCase(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
        poll1 = Polls(pollid='1', pollname='First Poll', creatorid='1')
        db.session.add(poll1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # def test_backref(self):
    #     poll = Polls.query.filter_by(pollname='First Poll').first()
    #     self.assertTrue(poll.creator)
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def register(self, username, email, password, confirm):
        return self.app.post('/register', data=dict(username=username, email=email, password=password, confirm=confirm),
        follow_redirects=True)

    def login(self, email, password):
        return self.app.post('/login', data=dict(email=email, password=password),
            follow_redirects=True)  

    def test_valid_user_registration(self):
        response = self.register('Hasi2', 'Hasi2@test.com', 'Hasi2test1', 'Hasi2test1')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.login('Hasi', 'Hasitest1')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.logout()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)