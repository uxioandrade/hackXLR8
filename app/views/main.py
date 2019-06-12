from flask import render_template, jsonify
from app import app
import random
#import requests
from flask import (Blueprint, render_template, redirect, request, url_for,
                   abort, flash)
from app.interface_sum_yt_transcr import summarize_from_url

@app.route('/')
@app.route('/index')
def index():
    if(request.form['url'] == 'POST'):
        summary_text = 'para que sirve flask'
        return render_template('summary.html',content=summary_text)
    else:
        return render_template('index.html', title='Home')

@app.route('/map')
def map():
    return render_template('map.html', title='Map')

@app.route('/summary/<string:url>')
def sum_up(url):
    #summary_text = summarize_from_url("https://www.youtube.com/watch?v=al0CVsiffu8")
    return render_template('summary.html',content=summary_text)

'''
if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            pass # do something
        elif request.form['submit_button'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
'''
'''
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
'''
@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')