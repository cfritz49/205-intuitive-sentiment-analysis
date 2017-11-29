import connection2twitter

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'bpTjS9ITJewUuxbZEcIwPnWqP'
consumer_secret = 'iMrwIcMYKIo3L8aAO3Jfbb6Pq5SntX5iJK9dnzxrjroLtZOGmd'
acces_token = '1437064778-SMbqdOOK2Et5ftZNeEKecuIWhMS1ceFEsjnfz9P'
acces_token_secret = 'ca58DLvuT82rlBvzpIkkkgYEEQ8md8IHJSgqbsfQsF5X5'

# api = tweepy.API(auth)
def searching():
    query = input("Enter Search term: ")
    lang = "en"
    results = api.search(q=query, language=lang)

    for tweet in results:
        print (tweet.user.screen_name,"Tweeted:",tweet.text)
