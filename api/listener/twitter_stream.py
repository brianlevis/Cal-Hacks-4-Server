from TwitterAPI import TwitterAPI

KEYWORD_LISTS = [
['Berkeley']
]
"""

latitude, longitude: floats
range: miles away? idk
keywords: list-like of strings

return a list-like of tweets

"""
consumerKey = "YOBQnrulcSHFtEiJnnWiDaVhG"
consumerSecret = "zQRNJ2J8hw1kccQO1Sb3X5bhbiVAFph6KSJr46d6cbZqP4rTZR"
tokenKey = "814761966723960832-EOKXXImj9OA8sNz51dasntrhbeReSsG"
tokenSecret = "CoKgSROWgP1Jxbql5oEtHnzt3Tt9jDJ7SAMfmJdsAOiJL"
twitAPI = TwitterAPI(consumerKey,consumerSecret, tokenKey, tokenSecret)
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


def groupTweets():
    classify = {}
    for key in KEYWORD_LISTS:

        tweets = get_filtered_tweets_by_location(37.8719, -122.2585, 10, key)
        if tweets is not None:
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
