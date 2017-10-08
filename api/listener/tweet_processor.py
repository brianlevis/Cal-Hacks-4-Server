from TwitterAPI import TwitterAPI
#import keystore
#import httplib, urllib
import json
from twitter_stream import get_filtered_tweets_by_location

consumerKey = "YOBQnrulcSHFtEiJnnWiDaVhG"
consumerSecret = "zQRNJ2J8hw1kccQO1Sb3X5bhbiVAFph6KSJr46d6cbZqP4rTZR"
tokenKey = "814761966723960832-EOKXXImj9OA8sNz51dasntrhbeReSsG"
tokenSecret = "CoKgSROWgP1Jxbql5oEtHnzt3Tt9jDJ7SAMfmJdsAOiJL"
twitAPI = TwitterAPI(consumerKey,consumerSecret, tokenKey, tokenSecret)

# In the future, import list of keyword sets from listener.py- for now, just a list of our keywords
KEYWORD_LISTS = [
    ['protest', 'rally', 'controversial speaker'],
    ['game', 'football']
]

"""

keywords: list-like of tweets

return a list-like of hashtags

"""

def groupTweets():
    classify = {}
    for key in KEYWORD_LISTS:
        tweets = get_filtered_tweets_by_location(37.7749, 122.4194, 10, key)
        for t in tweets:
            if t['entities']['hashtags'] != None:
                for hashtag in t['entities']['hashtags']:
                    if classify[hashtag['text']] == None:
                        classify[hashtag['text']] = [t]
                    else:
                        classify[hashtag['text']].append(t)
    return classify
test = groupTweets()
print(test)

#key is dependent on whether there's a hashtag or not
# def extract_hashtags(tweets, keyword_lists):
#     hashtag_dict = {}
#     for t in tweets:
#         if t['entities']['hashtags'] != []:
#             for hashtag in t['entities']['hashtags']:
#                 if hashtag_dict[hashtag['text']] == None:
#                     hashtag_dict[hashtag['text']] = [t]
#                 else:
#                     hashtag_dict[hashtag['text']].append(t)
#     return hashtag_dict


    # for keylist in KEYWORD_SETS:
    #     #keywordTweets = twitAPI.request('statuses/filter', {'track': keyword_sets})
    #     print(keylist)
#extract_hashtags("", KEYWORD_SETS)


"""

keywords: list-like of tweets

estimate using geographic average? clustering? etc

return a tuple of (latitude, longitude)

"""


def estimate_location(tweets):
    pass


"""

keywords: list-like of tweets


return a tuple of (positivity/sentiment, controversy)

"""


def get_sentiment(tweets):
    pass
# Tracker that looks at location of the
# user while also filtering tweets by those and key locations



#function that collects all tweets from a city within a 24 hour time period.
def tweetStreamCity(cityBoxCoordinates):
    locationalTweets = twitAPI.request('statuses/filter', {'locations':cityBoxCoordinates})
    return locationalTweets

#function that collects all tweets filtering by keywords

def tweetStreamKeywords(listOfKeyWords):
    keywordTweets = twitAPI.request('statuses/filter', {'track':listOfKeyWords})
    return keywordTweets

#function that prints out each tweet inside of the list of tweets
def printOutTweets(twitterTweetsList):
    for tweet in twitterTweetsList.get_iterator():
        print(tweet['text'])
        if tweet['entities']['hashtags'] != []:
            print('#'+tweet['entities']['hashtags'][0]['text'])

#applies a function to each tweet inside of a list of tweets
def funcApplyTweet(twitterTweetsList, func):
    for tweet in twitterTweetsList.get_iterator():
        func(tweet)


# keywordList = ['lebron']
#
# rv = tweetStreamKeywords(keywordList)
#
# printOutTweets(rv)
