from application import application
from flask import render_template

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/dash')
def dash():
    return render_template('dashboard.html')