from re import L
from flask import Blueprint

secure = Blueprint('secure', __name__)


@secure.route('/reg')
def reg():
    return '<p> Register </p>'

@secure.route('/login')
def login():
    return '<p> log in </p>'

@secure.route('/logout')
def logout():
    return '<p> log out </p>'
