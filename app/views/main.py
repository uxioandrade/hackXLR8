from flask import render_template, jsonify
from app import app
import random
#import requests
from flask import (Blueprint, render_template, redirect, request, url_for,
                   abort, flash)

from app import interface_sum_yt_transcr as i_sum
from app.srclib import tagtog_lib as tg

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    if(request.method == 'GET'):
        if request.form.get('submit_button'):
            summary_text = ""
            return render_template('summary.html',content=summary_text)
        else:
            return render_template('index.html', title='Home')
    elif(request.method == 'POST'):
        if(request.form.get('upvote')):
            link = request.form['url']
            summary_text = i_sum.summarize_from_url(link)
            keywords = i_sum.get_keywords_from_uril(link)
            return render_template('summary.html',content=summary_text,claves=keywords)
        else:
            return render_template('index.html', title='Home')
    else:
        return render_template('index.html', title='Home')

@app.route('/map')
def map():
    return render_template('map.html', title='Map')

@app.route('/summary/<string:url>')
def sum_up(url):
    summary_text = 'para que sirve flask'
    #summary_text = summarize_from_url("https://www.youtube.com/watch?v=al0CVsiffu8")
    return render_template('summary.html',content=summary_text)
'''
@app.route('/url/<string:link_video>')
def sum_up_video(link_video):
    summary_text = link_video
    #summary_text = summarize_from_url("https://www.youtube.com/watch?v=al0CVsiffu8")
    return render_template('summary.html',content=summary_text)
'''
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

@app.route('/tagtog',methods=['GET','POST'])
def tagtog():
    if(request.method == 'GET'):
        return render_template('tagtog.html', title='Tagtog')    
    elif(request.method == 'POST'):
        link = request.form['url']
        tagtog_url = tg.send_text_to_annotate(link)
        return redirect(tagtog_url.text, code=302)
    return render_template('tagtog.html', title='Tagtog')