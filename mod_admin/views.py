from flask import session
from . import admin

@admin.route('/')
def index():
    return 'Hello From Admin Index'

@admin.route('/login/')
def login():
    session['name'] = 'Arash'
    #session.clear()
    #print(session.get('name'))
    print(session)
    return '1'