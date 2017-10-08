from TwitterSearch import *
from api.listener.keystore.keystore import get_keys


try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    tso.set_language('en')
    tso.set_include_entities(False)
    tso.

    # it's about time to create a TwitterSearch object with our secret tokens
    keys = get_keys('twitter')

    ts = TwitterSearch(
        consumer_key= keys['consumerKey'],
        consumer_secret= keys['consumerSecret'],
        access_token= keys['tokenKey'],
        access_token_secret= keys['tokenSecret'],
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

"""

latitude, longitude: floats
range: miles away? idk
keywords: list-like of strings

return a list-like of tweets

"""


def get_tweets(latitude, longitude, radius):
    locational_tweets = twitAPI.request('search/tweets') # TODO