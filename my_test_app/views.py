import requests
from flask import flash, redirect, render_template, url_for, request, abort
from my_test_app import app#, db
#  from my_test_app.config import GOOGLE_API_KEY
from my_test_app.validator import validate_youtube_id

v_id = 'Y1MF4Pa626I'

@app.route('/')
def test():
    return 'Let\'s start!'


@app.route('/add_youtube_id/<youtube_id>', methods=['GET', 'POST'])
def add_youtube_id(youtube_id):
    return validate_youtube_id(youtube_id)
