import plotly
import plotly.plotly as pl
from plotly.graph_objs import *
import vaderSentiment.vaderSentiment as vS
# plotly.tools.set_credentials_file(username='cfritz49', api_key='ct7v5dxYbbpZlmnjx2wf')
# pl.sign_in('cfritz49', 'ct7v5dxYbbpZlmnjx2wf')

sentences = [
    "So now that Matt Lauer is gone when will the Fake News practitioners at NBC be terminating the contract of Phil Griffin? And will they terminate low ratings Joe Scarborough based on the “unsolved mystery” that took place in Florida years ago? Investigate!",
    "Great day for Tax Cuts and the Republican Party. But the biggest Winner will be our great Country!",
    "Just won the lawsuit on leadership of Consumer Financial Protection Bureau, CFPB. A big win for the Consumer!",
    "After North Korea missile launch, it's more important than ever to fund our gov't & military! Dems shouldn't hold troop funding hostage for amnesty & illegal immigration. I ran on stopping illegal immigration and won big. They can't now threaten a shutdown to get their demands."
]


analyzer = vS.SentimentIntensityAnalyzer()
pos = []
neg = []
neu = []
com = []
for sentence in sentences:
    sent = analyzer.polarity_scores(sentence)
    print(sent)
    pos.append(sent['pos'])
    neg.append(sent['neg'])
    neu.append(sent['neu'])
    com.append(sent['compound'])

print(neg)
print(neu)
print(pos)

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
trace3 = Bar(
    x=['1', '2', '3', '4'],
    y=com
)

data = [trace0, trace1, trace2]
layout = Layout(
    barmode='stack'
)
fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='abc')
