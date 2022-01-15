from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from mongoengine.fields import BooleanField
from wtforms.fields.core import IntegerField
from flaskblog import db, login_manager 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except:
        return None

class User(db.Document, UserMixin):
    #id = db.Column(db.Integer, primary_key=True)
    username = db.StringField(unique=True, nullable=False)
    email = db.EmailField(unique=True, nullable=False)
    image_file = db.StringField(nullable=False, default='default.jpg')
    password = db.StringField(nullable=False)
    posts = db.ReferenceField('Post', backref='author',lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')


    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.objects.get(user_id)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Document):
    #id = db.Column(db.Integer, primary_key=True)
    title = db.StringField(nullable = False)
    date_posted = db.DateField(nullable = False, default = datetime.utcnow)
    content = db.StringField(nullable = False)
    address = db.StringField(max_length=150, nullable=False)
    #location = db.PointField()
    price = db.StringField()
    opening_hours = db.StringField()
    # #facilities
    toilet_paper = db.BooleanField(nullalbe=False)
    sink = db.BooleanField(nullable=False)
    soap = db.BooleanField(nullable=False)
    wheelchair_acc = db.BooleanField(nullable=False)
    toilet = db.BooleanField(nullable=False)
    urinal = db.BooleanField(nullable=False)
    

    #review_id = ReferenceList (Review)
    user_id = db.ReferenceField('User')

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Rating(db.Document):
    rating = db.IntField(nullable = False)
    comment = db.StringField(nullable = False)
    post_id = db.ReferenceField ('Post', backref='author',lazy=True)
    user_id = db.ReferenceField ('User')