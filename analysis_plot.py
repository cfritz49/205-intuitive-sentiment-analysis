"""
CST 205-01

Intuitive Sentiment Analysis - Analyzing and displaying positive, neutral, and negative sentiment of tweets

By Connor Fritz, Jorge Lopez, and Matthew Connolly

This file takes in the list of tweets from the twitter search and analyzes them with VADER. It then uses the analysis
data to generate a histogram of compound scores and a pie chart of average sentiment.

All work on this file by Connor Fritz
"""

import plotly
from plotly.graph_objs import *
import vaderSentiment.vaderSentiment as vS


def vader_analyze(twitter_input):
    analyzer = vS.SentimentIntensityAnalyzer()
    pos = []
    neg = []
    neu = []
    com = []
    for tweet in twitter_input:
        analyzed_tweet = analyzer.polarity_scores(tweet)
        pos.append(analyzed_tweet['pos'])
        neg.append(analyzed_tweet['neg'])
        neu.append(analyzed_tweet['neu'])
        com.append(analyzed_tweet['compound'])

    ave_pos = sum(pos) / float(len(pos))
    ave_neu = sum(neu) / float(len(neu))
    ave_neg = sum(neg) / float(len(neg))

    labels = ['Positive', 'Neutral', 'Negative']
    values = [ave_pos, ave_neu, ave_neg]
    trace = Pie(labels=labels, values=values)
    data = [Histogram(x=com)]

    divs = (plotly.offline.plot([trace], include_plotlyjs=False, output_type='div'),
            plotly.offline.plot(data, include_plotlyjs=False, output_type='div'))

    return divs


print(vader_analyze(['positive', 'negative', 'neutral']))
