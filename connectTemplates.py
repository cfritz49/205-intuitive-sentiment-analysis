"""
CST 205-01

Intuitive Sentiment Analysis - Analyzing and displaying positive, neutral, and negative sentiment of tweets

By Connor Fritz, Jorge Lopez, and Matthew Connolly

This file acts as the visual interface for the project. It uses Flask and Bootstrap to display a web page that reads a
search query, calls the twitter search functions and analysis/plotting, and displays the resultant graphs.

All work on this file by Matthew Connolly
"""

# import test
# import twitterstream
import connection2twitter as twit

from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

# C:\Users\Matt\Desktop\envs\cst205\Scripts\Activate.ps1
# $env:FLASK_APP='\205-intuitive-sentiment-analysis\connectTemplates.py'
# $env:FLASK_DEBUG=1
# flask run

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/index', methods=['POST'])

def index():
    
    search = request.form['twitHash']
    #result = twit.hashtag(search)




    return render_template('index.html', search = search)

#possible link to graph?
@app.route('/graph/')
def graph(srch):




    return render_template('index.html')