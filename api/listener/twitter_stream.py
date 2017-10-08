"""

latitude, longitude: floats
range: miles away? idk
keywords: list-like of strings

return a list-like of tweets

"""
def realtime_stream_by_city(cityBoxCoordinates, keywords=[]):
    #function that collects all tweets from a city/keyword set within a 24 hour time period.
    locationalTweets = twitAPI.request('statuses/filter', {'locations':cityBoxCoordinates , 'track': keywords })
    return locationalTweets


def geoSearch_valid_locations(latitude, longitude, distance):
    #function that creates a json formatted object of all the possible locations closest to you in your radius
    distance = str(distance*5280) + "ft"
    places = twitAPI.request("geo/search", {"long": longitude, "lat": latitude, "accuracy": distance, "granularity": "city"})
    return places.json()


def get_filtered_tweets_by_location(latitude, longitude, distance, keywords=[]):
    #returns a list of tweet objects by location and distance of your setting
    boxSetCoordinates = geoSearch_valid_locations(latitude, longitude, distance)['result']['places'][0]['bounding_box']['coordinates'][0]
    return realtime_stream_by_city(boxSetCoordinates, keywords)
