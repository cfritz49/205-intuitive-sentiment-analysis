from urllib.request import urlopen, Request
import ssl
import tweepy
import pprint

# import twitter
consumer_key = 'bpTjS9ITJewUuxbZEcIwPnWqP'
consumer_secret = 'iMrwIcMYKIo3L8aAO3Jfbb6Pq5SntX5iJK9dnzxrjroLtZOGmd'
acces_token = '1437064778-SMbqdOOK2Et5ftZNeEKecuIWhMS1ceFEsjnfz9P'
acces_token_secret = 'ca58DLvuT82rlBvzpIkkkgYEEQ8md8IHJSgqbsfQsF5X5'

# context = ssl._create_unverified_context()
## Authentication
auth = tweepy.OAuthHandler(consumer_key,consumer_secret,'/home.html')

auth.set_access_token(acces_token,acces_token_secret)

api = tweepy.API(auth)
# def searching():
#     query = input("Enter Search term: ")
#     lang = "en"
#     results = api.search(q=query, language=lang)
#
#     for tweet in results:
#         print (tweet.user.screen_name,"Tweeted:",tweet.text)


user = input("Enter user:")
api.get_user(user)
# tweepy.Cursor(api.user_timeline(id="twitter"))
print('Name:' + user)
print('Friends:')
print(user.followers_count)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print (tweet.text)
    print (tweet.user.screen_name)
