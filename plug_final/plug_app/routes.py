import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from plug_app import app , db ,bcrypt
from plug_app.forms import RegistrationForm, LoginForm,SkilltagForm, UpdateAccountForm, ProjectsForm
from plug_app.models import User, Post, Skilltag, Projects
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import MetaData, Column


@app.route('/', methods=['GET' , 'POST' ])
@app.route('/landing', methods=['GET' , 'POST' ])

def landing():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = RegistrationForm()
	form2 = LoginForm()
	if form.validate_on_submit():

		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(Firstname=form.First_name.data, Secondname=form.Second_name.data, username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('account made')
		return redirect(url_for('landing'))

	if form2.validate_on_submit():
		user=User.query.filter_by(email=form2.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form2.password.data):
			login_user(user, remember=form2.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else: 
				return redirect(url_for('skill'))	


	return render_template('landing2.html', title='landing', form=form , form2=form2)




@app.route('/layout',methods =['GET' , 'POST'])
def layout():
	form2 = LoginForm()
	if form2.validate_on_submit():
		user=User.query.filter_by(email=form2.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form2.password.data):
			login_user(user, remember=form2.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else: 
				return redirect(url_for('home'))	

	return render_template('layout.html', title='layout' , form2=form2)


@app.route('/layout_main',methods =['GET' , 'POST'])
def layout_main():
	return render_template('layout_main.html', title='layout' , form2=form2)










































@app.route('/register', methods=['GET' , 'POST' ])

def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = RegistrationForm()
	if form.validate_on_submit():

		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(Firstname=form.First_name.data, Secondname=form.Second_name.data, username=form.username.data, email=form.email.data, password=hashed_password)

		db.session.add(user)
		db.session.commit()
		flash('account made')
		return redirect(url_for('login'))

	return render_template('register.html', title='Register', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
	
	if current_user.is_authenticated:
		return  redirect(url_for('search'))
	form = LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else: 
				return redirect(url_for('search'))	
	return render_template('login.html', title='login', form=form)















#////////////// PROJECT UPLOADER ///////////////////////////////
# renaming pic to a random hex str with original extension and then saving 
#it into static folder  FOR PROJECT PICTURES
#/////////////////// ADD USER ID AT THE FRONT OF HEX/////////////////////



@app.route('/projects', methods=['GET' , 'POST' ])
@login_required
def projects():
	form = ProjectsForm()
	image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
	random_hex = secrets.token_hex(5)
	random_hex_two = secrets.token_hex(5)

	Project_id = "P_ID"+"_"+ str(current_user.id)+"_"+random_hex
	uid = current_user.id

	Img_id = Project_id+"Img_ID"+"_"+random_hex_two
	Vid_id  = Project_id+"Vid_id"+"_"+random_hex_two
	Doc_id  = Project_id+"Doc_id "+"_"+random_hex_two

	def save_prjct_img(project_form_picture):
		_name, f_ext = os.path.splitext(project_form_picture.filename)
		picture_fn = Img_id + f_ext
		picture_path = os.path.join(app.root_path, 'static/project_upload', picture_fn)
		project_form_picture.save(picture_path)
		
		return picture_fn


	if form.validate_on_submit():
		#d_picture_fn = save_prjct_img(form.cover_img.data)
		if form.cover_img.data:
			d_picture_fn = save_prjct_img(form.cover_img.data)
			projects.Img_id  = d_picture_fn	

		project = Projects( user_id=uid, Title=form.Title.data, TxtContent=form.TxtContent.data, Project_id=Project_id, Vid_id=Vid_id, Doc_id=Doc_id, Requests=form.Requests.data, Img_id=d_picture_fn )
		db.session.add(project)
		db.session.commit()
		flash('project uploaded')	
		return redirect(url_for('search'))


	return render_template('project.html', title='projects upload', form=form, image_file=image_file)	







@app.route('/home',methods =['GET' , 'POST'])
@login_required
def home():
    return render_template('home.html', title='home')

@app.route('/newsfeed',methods =['GET' , 'POST'])
@login_required
def newsfeed():
	result = User.query.all()
	return render_template('newsFeed.html', title='home', result=result )



@app.route('/search',methods =['GET' , 'POST'])
#@login_required
def search():
    return render_template('search.html', title='search')




@app.route('/area',methods =['GET' , 'POST'])
def peopleInArea():
    return render_template('peopleInArea.html', title='peopleInArea')	



@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('landing'))



#////////////// PROFILE PIC UPLOADER ///////////////////////////////
# renaming profile pic to a random hex str with original extension and then saving 
#it into static folder  FOR PROFILE PICTURES
#/////////////////// ADD USER ID AT THE FRONT OF HEX/////////////////////
def save_img(form_picture):
	random_hex = secrets.token_hex(8)
	_name, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)


# Resizing uploaded image using pillow packad
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)

	return picture_fn



@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	image_file = url_for('static', filename='profile_pics/'+current_user.image_file)

	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:

			picture_file = save_img(form.picture.data)
			current_user.image_file = picture_file

		current_user.Firstname = form.First_name.data
		current_user.Secondname = form.Second_name.data
		current_user.email = form.email.data
		current_user.username = form.username.data
		db.session.commit()

		flash('account updated')
		return redirect(url_for('account'))

	elif request.method == 'GET':
		form.First_name.data = current_user.Firstname
		form.Second_name.data = current_user.Secondname
		form.email.data = current_user.email
		form.username.data = current_user.username
	return render_template('account.html', title='Account', form=form, image_file=image_file)







@app.route('/upload', methods=['GET' , 'POST' ])
@login_required
def upload():
	form = ProjectsForm()
	image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
	random_hex = secrets.token_hex(5)
	random_hex_two = secrets.token_hex(5)

	Project_id = "P_ID"+"_"+ str(current_user.id)+"_"+random_hex
	uid = current_user.id

	Img_id = Project_id+"Img_ID"+"_"+random_hex_two
	Vid_id  = Project_id+"Vid_id"+"_"+random_hex_two
	Doc_id  = Project_id+"Doc_id "+"_"+random_hex_two

	def save_prjct_img(project_form_picture):
		_name, f_ext = os.path.splitext(project_form_picture.filename)
		picture_fn = Img_id + f_ext

		picture_path = os.path.join(app.root_path, 'static/project_upload', picture_fn)
		project_form_picture.save(picture_path)
		
		return picture_fn


	if form.validate_on_submit():
		#d_picture_fn = save_prjct_img(form.cover_img.data)
		if form.cover_img.data:
			d_picture_fn = save_prjct_img(form.cover_img.data)
			projects.Img_id  = d_picture_fn	

		project = Projects( user_id=current_user.id, Title=form.Title.data, TxtContent=form.TxtContent.data, Project_id=Project_id, Vid_id=Vid_id, Doc_id=Doc_id, Requests=form.Requests.data, Img_id=d_picture_fn )
		db.session.add(project)
		db.session.commit()

		flash('project uploaded')	
		return redirect(url_for('search'))
		
	return render_template('project2.html', title='projects upload', form=form, image_file=image_file)	




#///////////////////////////////////////////NEWSFEED///////////////////////////////////////////////

@app.route('/newsfeed2',methods =['GET' , 'POST'])
@login_required
def newsfeed2():
	result = Projects.query.all()
	user_id = result[0]
	uid = result[0]
	post_user = User.query.filter(User.id == "1")
	#post_user = User.query.filter(User.id == projects.user_id).all()
	#fresult = result[0].id
	profile_pic = url_for('static', filename='profile_pics/')
	image_file = url_for('static', filename='project_upload/')

	user = User.query.all()
	return render_template('newsFeed2.html', title='home', result=result, image_file=image_file, user_id=user_id, post_user=post_user, profile_pic=profile_pic, uid=uid, user=user)

  #////////////////////////////////////////SKILLTAGS/////////////////////////////////////////////


@app.route('/skill', methods=['GET' , 'POST' ])
@login_required
def skill():
	image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
	form = SkilltagForm()
	allSkill = Skilltag.query.all()
	cu_skills = current_user.Skilltag
	u_skill=form.skill.data
	dot = "-"

	if form.validate_on_submit():
		for i in allSkill:
			if i.skill == u_skill:
				c_db_uid = str(i.user_id) +dot+str(current_user.id)



				skilltag = Skilltag(user_id=str(c_db_uid), skill=u_skill, s_uid=current_user.id)
				db.session.add(skilltag)
				db.session.commit()
				flash('A duplicate has been skilltag added to your profile')
				return redirect(url_for('skill'))
		#db_skills = allSkill.skill
		#if skill == :
		skilltag = Skilltag(user_id=current_user.id, skill=u_skill, s_uid=current_user.id)
		db.session.add(skilltag)
		db.session.commit()
		flash('skilltag added to your profile')
		return redirect(url_for('skill'))

	return render_template('skill.html', title='Register', form=form, allSkill=allSkill, cu_skills=cu_skills, image_file=image_file)