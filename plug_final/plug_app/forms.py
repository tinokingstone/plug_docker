from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField , SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
	First_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=60)])
	Second_name = StringField('Second Name', validators=[DataRequired(),Length(min=2, max=60)])
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=60)])
	email = StringField('Email', validators=[DataRequired(),Email(),Length(min=2, max=60)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	picture = FileField('upload Your Profile picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(),Email(),Length(min=0, max=60)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('log in')


class SkilltagForm(FlaskForm):
	skill = StringField('what are you ?', validators=[DataRequired(), Length(min=2, max=60)])
	submit = SubmitField('add skill')


class UpdateAccountForm(FlaskForm):
	First_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=60)])
	Second_name = StringField('Second Name', validators=[DataRequired(),Length(min=2, max=60)])
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=60)])
	email = StringField('Email', validators=[DataRequired(),Email(),Length(min=2, max=60)])
	picture = FileField('Update Your Profile picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('update')

	def Validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).First()
			if user:
				raise ValidationError('Email already in use')

class ProjectsForm(FlaskForm):
	Title = StringField('Title', validators=[DataRequired(), Length(min=2, max=60)])
	TxtContent = TextAreaField('Content', validators=[DataRequired(), Length(min=2, max=1999)])
	#uid = StringField('Content', validators=[DataRequired(), Length(min=2, max=60)])

	cover_img = FileField('Upload a cover image', validators=[FileAllowed(['jpg', 'png'])])

	img = FileField('Upload image', validators=[FileAllowed(['jpg', 'png'])])
	vid = FileField('Upload video', validators=[FileAllowed(['mp4', 'png'])])
	audio = FileField('Upload audio', validators=[FileAllowed(['mp3', 'wav'])])
	doc = FileField('Upload Project document/file')

	Requests = StringField('Requests', validators=[DataRequired(), Length(min=2, max=60)])

	submit = SubmitField('Upload Project')
	


		

