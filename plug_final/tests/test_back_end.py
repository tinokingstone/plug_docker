import unittest
import werkzeug

from flask import abort, url_for, Flask
from flask_testing import TestCase

from plug_app import app, db 
from plug_app.models import User, Post, Skilltag
from werkzeug.utils import cached_property

class TestBase(TestCase):
	def create_app(self):
		config_name = 'testing'
		app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@127.0.0.1/testdb" )
		return app

	def setUp(self):
		db.session.commit()
		db.drop_all()
		db.create_all()

		admin = User(Firstname="admin", Secondname="admin", email="admin@admin.com", password="admin2016")
		employee = User(Firstname="test", Secondname="user", email="test@user.com", password="test2016")

		db.session.add(admin)
		db.session.add(employee)
		db.session.commit()

	def TearDown(self):
		db.session.remove()
		db.drop_all()
		

class TestViews(TestBase):
	def test_homepage_view(self):
		response = self.client.get(url_for('register'))
		self.assertEqual(response.status_code, 200)

