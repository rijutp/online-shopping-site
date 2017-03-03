from flask import Flask, render_template, request, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required
# from flask.ext.sqlalchemy import SQLAlchemy
from models import Register,Items
import logging
from logging import Formatter, FileHandler
from forms import RegisterForm
from forms import LoginForm
from forms import ForgotForm
from forms import ItemForm
import os
from app import app,db,login_manager

@app.route('/')
def home():
	return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
	return render_template('pages/placeholder.about.html')


@login_manager.user_loader
def load_user(user_id):
	return Register.query.filter_by(user_id=user_id).first()


@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'GET':
		form = LoginForm(request.form)
		return render_template('forms/login.html', form=form)
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		registered_user = Register.query.filter_by(email = email, password = password).first()
		if registered_user is None:
			print('email and password is invalid','error')
			return redirect(url_for('login'))
		# user = User.get_(phone)
		login_user(registered_user)
		print('logged in succesfully')
		return redirect(url_for('item'))
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='admin@gmail.com', password='admin')
#     db.session.commit()

@app.route('/register',methods = ['POST', 'GET'])
def register():
	print request.method
	if request.method == 'GET':
		form = RegisterForm(request.form)
		return render_template('forms/register.html',form=form)
	if request.method == 'POST':

		print "hello"
	   # result = request.form    
		user = Register(request.form['name'],request.form['email'],request.form['password'])
		# name = request.form['name']
		# email = request.form['email']
		# password = request.form['password']
		print user
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))


@app.route('/item',methods = ['POST', 'GET'])
def item():
	print "reached in item view"
	if request.method == 'GET':
		form = ItemForm(request.form)
		return render_template('forms/item.html', form=form)
	if request.method == 'POST':
		print "hii"
		itemlist = Items(request.form['itemname'],request.form['price'],request.form['description'])
		print itemlist
		db.session.add(itemlist)
		db.session.commit()
		return redirect(url_for('how'))


@app.route('/forgot')
def forgot():
	form = ForgotForm(request.form)
	return render_template('forms/forgot.html', form=form)

# Error handlers.
@app.route('/how')
def how():
	return render_template('forms/user.html',form=form)


@app.errorhandler(500)
def internal_error(error):
	#db_session.rollback()
	return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
	return render_template('errors/404.html'), 404

if not app.debug:
	file_handler = FileHandler('error.log')
	file_handler.setFormatter(
		Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
	)
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('errors')

