from flask import Flask, redirect, render_template, url_for, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from werkzeug.utils import secure_filename

import os



WTF_CSRF_SECRET_KEY = 'ISAAC'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://k3nsh1n:k0rn82...@localhost/registroCedula'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Isaac'
app.config['DEBUG'] = True
app.config['UPLOAD_IMAGES'] = '/home/k3nsh1n/Imágenes/'



db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)

from models import *


WTF_CSRF_SECRET_KEY = 'ISAAC'

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/users/registerUser', methods=['GET', 'POST'])
def registerUser():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		print(username)
		user = User(username=username, password=password, email=email)
		db.session.add(user)
		db.session.commit()
		if user:
			print('Usuario creado')
	return render_template('users/registerUser.html', title='Registro de usuarios')

@app.route('/ced/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		name = request.form['name']
		matricula = request.form['matricula']
		turno = request.form['turno']
		adscripcion = request.form['adscripcion']
		if 'file' not in request.files:
			print('No hay archivo')
		img = request.files['img']
		if img.filename == '':
			print('No hay nombre de archivo')
		filename = secure_filename(img.filename)
		mimetype = img.mimetype
		img.save(os.path.join(app.config['UPLOAD_IMAGES'], img.filename))

		worker = Worker(name=name, matricula=matricula, turno=turno, adscripcion=adscripcion, img=img, mimetype=mimetype)
		db.session.add(worker)
		db.session.commit()
		if worker:
			print('Registro Satisfactorio')

	return render_template('workers/register.html', title='Registro Cédulas')





if __name__ == '__main__':

    app.run()
