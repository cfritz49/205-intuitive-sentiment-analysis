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
        print(a_tweet)
        pos.append(a_tweet['pos'])
        neg.append(a_tweet['neg'])
        neu.append(a_tweet['neu'])
        com.append(a_tweet['compound'])

    print(neg)
    print(neu)
    print(pos)

    mpos = sum(pos) / float(len(pos))
    mneu = sum(neu) / float(len(neu))
    mneg = sum(neg) / float(len(neg))

    print(mpos, mneu, mneg)

    trace0 = Bar(
        x=['1', '2', '3', '4'],
        y=neg,
        text=['neg', 'neg', 'neg', 'neg']
    )
    trace1 = Bar(
        x=['1', '2', '3', '4'],
        y=neu,
        text=['neu', 'neu', 'neu', 'neu']
    )
    trace2 = Bar(
        x=['1', '2', '3', '4'],
        y=pos,
        text=['pos', 'pos', 'pos', 'pos']
    )
    # trace3 = Pie(
    #     labels=['pos', 'neu', 'neg'],
    #     values=[mpos, mneu, mneg],
    #     colors=['#FEBFB3', '#E1396C', '#96D38C']
    # )

    data = [trace0, trace1, trace2]
    layout = Layout(
        barmode='stack'
    )
    fig = Figure(data=data, layout=layout)
    return plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')


print(vader_analyze(['positive', 'negative', 'neutral']))
