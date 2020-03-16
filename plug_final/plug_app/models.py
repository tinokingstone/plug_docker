from datetime import datetime
from plug_app import db
from plug_app import login_manager
from flask_login import UserMixin
from sqlalchemy import MetaData, Column

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	Posts = db.relationship('Post', backref='author', lazy=True)
	Projects = db.relationship('Projects', backref='author', lazy=True)
	Skilltag = db.relationship('Skilltag', backref='author', lazy=True)
	
	Firstname = db.Column(db.String(20), unique=False, nullable=False)
	Secondname = db.Column(db.String(120), unique=False, nullable=False)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False,default='default.jpg')
	password = db.Column(db.String(60), nullable=False)


	def __repr__(self):
		return f"User('{self.id}', '{self.username}','{self.Firstname}', '{self.Secondname}', '{self.image_file}')  "

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"


class Projects(db.Model):
	__tablename__ = "Projects"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
	
	Project_id = db.Column(db.String(200), unique=True, nullable=True)
	
	Title = db.Column(db.String(200), unique=True, nullable=True)
	TxtContent = db.Column(db.String(1000), unique=True, nullable=True)
	
	Img_id = db.Column(db.String(200), unique=True, nullable=True)

	Vid_id = db.Column(db.String(200), unique=True, nullable=True)
	Doc_id = db.Column(db.String(200), unique=True, nullable=True)

	Requests = db.Column(db.String(200), unique=True, nullable=True)

	date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"Projects('{self.Title}', '{self.TxtContent}', '{self.Img_id}', '{self.date_time}')"



class Skilltag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=True)

	skill = db.Column(db.String(999), nullable=False)
	s_uid = db.Column(db.String(200), unique=False, nullable=True)

	def __repr__(self):
		return f"Skilltag('{self.skill}', '{self.s_uid}')"
