## Jorge Lopez
## December 8, 2017
## CST 205-01
## Avner Biblarz

## Abstract: Auntheticates myself as owner.
## Allows the user to search for users and pull their tweets.
## I was also able to provide the user to search for a
## specific keyword or hashtag and get those tweets

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
    tweetList = []
    for tweet in tweepy.Cursor(api.search, q = search,
                                            count = 100,
                                            result_type = "recent",
                                            include_entities=True,
                                            lang="en").items(100):

        if (not tweet.retweeted) and ('RT @'not in tweet.text):
            tweetList.append(tweet.text)

    return tweetList


#     # Accepts username and prints tweets from them #
# def usr(user):
#     tweetcount = 10
#     my_user=api.get_user(user)
#     print('Name:' + user)
#     print()
#     print('Number of Followers:')
#     print(my_user.followers_count)
#     print()
#     results_2 = api.user_timeline(id=user,count=tweetcount,full_text=True)
#     print("Recent tweets:")
#     for tweet in results_2:
#         if not tweet.retweeted:
#             print(tweet.text)
#     print()
#
# # Calls usr function to search user w/ number of followers & tweets #
# user = input("Enter user:")
# usr(user)
# Calls hashtag function to search input #
# query = input("Enter hashtag or keyword:")


# print(hashtag(query))
