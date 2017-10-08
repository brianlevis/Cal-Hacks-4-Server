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


def real_time_stream_by_city(city_box_coordinates, keywords=[]):
    # function that collects all tweets from a city/keyword set within a 24 hour time period.
    locational_tweets = twitAPI.request('statuses/filter', params={'locations': city_box_coordinates, 'track': keywords})
    return locational_tweets


def geo_search_valid_locations(latitude, longitude, distance):
    # function that creates a json formatted object of all the possible locations closest to you in your radius
    distance = str(distance * 5280) + "ft"
    places = twitAPI.request("geo/search",
                             {"long": longitude, "lat": latitude, "accuracy": distance, "granularity": "city"})
    return places.json()


def get_filtered_tweets_by_location(latitude, longitude, distance, keywords=[]):
    # returns a list of tweet objects by location and distance of your setting
    valid_locations = geo_search_valid_locations(latitude, longitude, distance)
    box_set_coordinates = valid_locations['result']['places'][0]['bounding_box']['coordinates'][0]
    max_lat = min_lat = box_set_coordinates[0][0]
    max_lon = min_lon = box_set_coordinates[0][1]
    for coord in box_set_coordinates:
        max_lat = max(coord[0], max_lat)
        min_lat = min(coord[0], min_lat)
        max_lon = max(coord[1], max_lon)
        min_lon = min(coord[1], min_lon)
    coordinates = str(min_lat) + ',' + str(min_lon) + ',' + str(max_lat) + ',' + str(max_lon)
    return real_time_stream_by_city(coordinates, keywords)


#
# def group_tweets():
#     classify = {}
#     for key in KEYWORD_LISTS:
#         tweets = get_filtered_tweets_by_location(37.8719, -122.2585, 10, key)
#         if tweets is not None:
#             for t in tweets:
#                 if t['entities']['hashtags'] != None:
#                     for hashtag in t['entities']['hashtags']:
#                         if classify[hashtag['text']] == None:
#                             classify[hashtag['text']] = [t]
#                         else:
#                             classify[hashtag['text']].append(t)
#     return classify


# test = group_tweets()
# print(test)
# flat_list = [item for sublist in KEYWORD_LISTS for item in sublist]
# print(flat_list)
