from flask import Blueprint, jsonify, request, redirect, url_for, session, flash
from ..models import User, db

api = Blueprint('api', __name__)

def unpack(fields, _dict):
    result = []
    for field in fields:
        result.append(_dict.get(field))

@api.route('/signup', methods=['POST'])
def signup():
    form = request.form

    username, email, password = form.get('username'), form.get('email'), form.get('password')

    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()

    session['username'] = username
    
    return redirect(url_for('frontend.myUser'))

@api.route('/login', methods=['POST'])
def login():
    form = request.form

    username, password = form.get('username'), form.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    if user:
        session['username'] = username
        return redirect(url_for('frontend.myUser'))
    
    flash("User not found", category="error")
    return redirect(url_for('frontend.login'))