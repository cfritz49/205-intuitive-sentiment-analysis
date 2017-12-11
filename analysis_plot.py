"""
CST 205-01

Intuitive Sentiment Analysis - Analyzing and displaying positive, neutral, and negative sentiment of tweets

By Connor Fritz, Jorge Lopez, and Matthew Connolly

This file takes in the list of tweets from the twitter search and analyzes them with VADER. It then uses the analysis
data to generate a histogram of compoun d scores and a pie chart of average sentiment.

All work on this file by Connor Fritz
"""

import plotly
from plotly.graph_objs import *
import vaderSentiment.vaderSentiment as vS


# Takes in a list of tweets as strings, analyzes them, returns graphs as divs in the format (Pie chart, Histogram)
def vader_analyze(twitter_input):
    analyzer = vS.SentimentIntensityAnalyzer()
    pos = []
    neg = []
    neu = []
    com = []

    # VADER analysis
    for tweet in twitter_input:
        analyzed_tweet = analyzer.polarity_scores(tweet)
        pos.append(analyzed_tweet['pos'])
        neg.append(analyzed_tweet['neg'])
        neu.append(analyzed_tweet['neu'])
        com.append(analyzed_tweet['compound'])

    # Average calculation
    ave_pos = sum(pos) / float(len(pos))
    ave_neu = sum(neu) / float(len(neu))
    ave_neg = sum(neg) / float(len(neg))

    # Setting up Plot.ly graphing
    labels = ['Positive', 'Neutral', 'Negative']
    values = [ave_pos, ave_neu, ave_neg]
    trace = Pie(labels=labels, values=values)
    data = [Histogram(x=com)]

    # Creates Plot.ly graphs and stores them in tuple as strings. The graphs are saved as HTML divs
    divs = (plotly.offline.plot([trace], include_plotlyjs=False, output_type='div'),    # Pie Chart
            plotly.offline.plot(data, include_plotlyjs=False, output_type='div'))       # Histogram

    return divs


print(vader_analyze(['positive', 'negative', 'neutral']))
