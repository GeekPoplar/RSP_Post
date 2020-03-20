from flask_login import UserMixin
from rsppost import db,login
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
#from rsppost import 


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    is_admin=db.Column(db.Boolean,default=False)

    timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)

    is_anonymous=db.Column(db.Boolean,default=False)

    posts=db.relationship('Post',backref='author',lazy='dynamic')
    comments=db.relationship('Comment',backref='author',lazy='dynamic')

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    #user_id=db.Column(db.Integer)
    title = db.Column(db.String(140))
    url = db.Column(db.String(140))
    body = db.Column(db.String(140))

    likes=db.Column(db.Integer,default=0)
    liked_by=db.Column(db.String(20)) #点赞用户

    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    comments=db.relationship('Comment',backref='father_post',lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.title)



class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(140))
    likes=db.Column(db.Integer,default=0)

    post_id=db.Column(db.Integer,db.ForeignKey('post.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Comment {}>'.format(self.content)