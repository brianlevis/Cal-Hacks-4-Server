import argparse
import time
import sys

import math

import select

from api.listener import twitter_stream
from api.listener.keystore import keystore

from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage

# Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--region', dest='region', action='store', required=True)
parser.add_argument('--latitude', dest='latitude', action='store', required=True)
parser.add_argument('--longitude', dest='longitude', action='store', required=True)
parser.add_argument('--token', dest='token', action='store', required=True)
parser.add_argument('--user', dest='user', action='store', required=True)
# region, latitude, longitude = parser.parse_args()
args = parser.parse_args()
region, latitude, longitude = args.region, args.latitude, args.longitude
token, user = args.token, args.user
# Constants
SECONDS_TO_LIVE = 600
# This is how you get twitter keys!
# dict with keys consumerKey, consumerSecret, tokenKey, tokenSecret
TWITTER_KEYS = keystore.get_keys('twitter')
DISTANCE = 10
KEYWORD_LISTS = [
    # ('Cal', 'Washington', 'Huskies'),
    # ('protest', 'controversial speaker'),
    # ('amberalert', 'amber alert'),
    ('calhacks', 'calhacks4'),
]

expiration = time.time() + SECONDS_TO_LIVE


def reset_lifetime():
    global expiration
    expiration = time.time() + SECONDS_TO_LIVE


def check_lifetime():
    return time.time() < expiration


def input_available():
    return select.select([sys.stdin, ], [], [], 0.0)[0]


def get_input():
    line = sys.stdin.readline()


reset_lifetime()

start = time.time()
while check_lifetime():
    if input_available():
        get_input()
        reset_lifetime()

    new_tweets = twitter_stream.get_filtered_tweets_by_location(latitude, longitude, DISTANCE, KEYWORD_LISTS)
    response = PushClient().publish(
            PushMessage(to=token,
                        body="New tweet",
                        data=new_tweets[0]))


    delta = time.time() - start
    if delta < 120:
        time.sleep(math.ceil(delta))
    start = time.time()
