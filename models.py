from app import db
from sqlalchemy import Column, Integer, String, DateTime

import datetime

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(93), unique=True, nullable=False)
	password = db.Column(db.String(93), unique=True, nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())




class Worker(db.Model):
	__tablename__ = 'workers'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(93), unique=True, nullable=False)
	matricula = db.Column(db.String(20), unique=True, nullable=False)
	turno = db.Column(db.String(90), nullable=False)
	adscripcion = db.Column(db.String(90), nullable=False)
	img = db.Column(db.Text(), nullable=False)
	mimetype = db.Column(db.Text(), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())

	def __str__(self):
		return self.name
