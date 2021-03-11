from flask import Blueprint, render_template, flash, session, redirect, url_for
from ..models import User

frontend = Blueprint(
    'frontend',
    __name__,
    template_folder="frontend\\templates",
    static_folder="frontend\\static"
)

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/about')
def about():
    return render_template('about.html')

@frontend.route('/user')
def myUser():
    user = User.query.filter_by(username=session['username']).first()
    if user:
        username = user.username
        email = user.email
        return render_template('myUser.html', username=username, email=email)
    return redirect(url_for('frontend.login'))

@frontend.route('/signup')
def signup():
    return render_template('signup.html')

@frontend.route('/login')
def login():
    return render_template('login.html')