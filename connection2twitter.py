## Jorge Lopez
## December 8, 2017
## CST 205-01
## Avner Biblarz

import tweepy

# import twitter
consumer_key = 'bpTjS9ITJewUuxbZEcIwPnWqP'
consumer_secret = 'iMrwIcMYKIo3L8aAO3Jfbb6Pq5SntX5iJK9dnzxrjroLtZOGmd'
acces_token = '1437064778-SMbqdOOK2Et5ftZNeEKecuIWhMS1ceFEsjnfz9P'
acces_token_secret = 'ca58DLvuT82rlBvzpIkkkgYEEQ8md8IHJSgqbsfQsF5X5'


## Authentication
auth = tweepy.OAuthHandler(consumer_key,consumer_secret,'/home.html')

auth.set_access_token(acces_token,acces_token_secret)

api = tweepy.API(auth)

    # Search hashtags along with keywords #
def hashtag(search):
    for tweet in tweepy.Cursor(api.search, q = search,
                                            include_entities=True,
                                            lang="en").items(10):
        # print ("entities:", tweet.entities['hashtags'])
        print (tweet.text)

    # Accepts username and prints tweets from them #
tweetcount = 10
user = input("Enter user:")
my_user=api.get_user(user)
print('Name:' + user)
print()
print('Number of Followers:')
print(my_user.followers_count)
print()
print('Followers:')
# print(my_user.followers['screen_name'])
print()
results_2 = api.user_timeline(id=user,count=tweetcount)
print("Recent tweets:")
for tweet in results_2:
    print(tweet.text)
print()
# Calls hashtag function to search input #
query = input("Enter hashtag or keyword:")

hashtag(query)
