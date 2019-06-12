from flask import render_template, jsonify
from app import app
import random
from app.interface_sum_yt_transcr import summarize_from_url

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/map')
def map():
    return render_template('map.html', title='Map')

@app.route('/summary/<string:url>')
def sum_up(url):
    summary_text = summarize_from_url("https://www.youtube.com/watch?v=al0CVsiffu8")
    return render_template('summary.html',content=summary_text)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')