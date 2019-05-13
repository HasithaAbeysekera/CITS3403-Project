import unittest, os
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
        u1 = User(id='00000000', username = 'Hasi', email = 'hasi@test.com', admin = True)
        u2 = User(id='11111111', username = 'Sam', email = 'sam@test.com', admin = True)
        u3 = User(id='22222222', username = 'Tom', email = 'tom@test.com', admin = False)
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
        #u1 = User(id='00000000', username = 'Hasi', email = 'hasi@test.com', admin = True)
        #u2 = User(id='11111111', username = 'Sam', email = 'sam@test.com', admin = True)
        #u3 = User(id='22222222', username = 'Tom', email = 'tom@test.com', admin = False)
        #db.session.add(u1)
        #db.session.add(u2)
        #db.session.add(u3)
        #db.session.commit()
        #u1 = User(username='Hasi')
        #u3 = User(username ='Tom')
        self.assertFalse(u3.admin)
        self.assertTrue(u1.admin)

if __name__ == '__main__':
    unittest.main(verbosity=2)