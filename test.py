import plotly
from plotly.graph_objs import *
import vaderSentiment.vaderSentiment as vS


sentences = [
    "So now that Matt Lauer is gone when will the Fake News practitioners at NBC be terminating the contract of Phil Griffin? And will they terminate low ratings Joe Scarborough based on the “unsolved mystery” that took place in Florida years ago? Investigate!",
    "Great day for Tax Cuts and the Republican Party. But the biggest Winner will be our great Country!",
    "Just won the lawsuit on leadership of Consumer Financial Protection Bureau, CFPB. A big win for the Consumer!",
    "After North Korea missile launch, it's more important than ever to fund our gov't & military! Dems shouldn't hold troop funding hostage for amnesty & illegal immigration. I ran on stopping illegal immigration and won big. They can't now threaten a shutdown to get their demands."
]


def vader_analyze(twitter_input):
    analyzer = vS.SentimentIntensityAnalyzer()
    pos = []
    neg = []
    neu = []
    com = []
    for tweet in twitter_input:
        a_tweet = analyzer.polarity_scores(tweet)
        pos.append(a_tweet['pos'])
        neg.append(a_tweet['neg'])
        neu.append(a_tweet['neu'])
        com.append(a_tweet['compound'])

    mpos = sum(pos) / float(len(pos))
    mneu = sum(neu) / float(len(neu))
    mneg = sum(neg) / float(len(neg))

    labels = ['Positive', 'Neutral', 'Negative']
    values = [mpos, mneu, mneg]
    trace = Pie(labels=labels, values=values)
    data = [Histogram(x=com)]

    divs = (plotly.offline.plot([trace], include_plotlyjs=False, output_type='div'),
            plotly.offline.plot(data, include_plotlyjs=False, output_type='div'))

    return divs


print(vader_analyze(['positive', 'negative', 'neutral']))
