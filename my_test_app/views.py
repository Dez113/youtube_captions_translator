from flask import flash, redirect, render_template, url_for, request, abort
from my_test_app import app, db

@app.route('/')
def test():
    return 'Let\'s start!'

@app.route('/add_youtube_id_<youtube_id>', methods=['GET','POST'])
def add_you_tube_id(youtube_id):
	return youtube_id