from TwitterAPI import TwitterAPI

from api.listener.keystore.keystore import get_keys

"""

latitude, longitude: floats
range: miles away? idk
keywords: list-like of strings

return a list-like of tweets

"""
keys = get_keys('twitter')
twitAPI = TwitterAPI(keys['consumerKey'], keys['consumerSecret'], keys['tokenKey'], keys['tokenSecret'])


def get_tweets(latitude, longitude, radius):
    locational_tweets = twitAPI.request('search/tweets') # TODO