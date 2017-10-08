import argparse
import datetime
import sys

import keystore


# Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--region', dest='region', action='store', required=True)
parser.add_argument('--latitude', dest='latitude', action='store', required=True)
parser.add_argument('--longitude', dest='longitude', action='store', required=True)


# Constants
MINUTES_TO_LIVE = 5
# This is how you get twitter keys!
# dict with keys consumerKey, consumerSecret, tokenKey, tokenSecret
TWITTER_KEYS = keystore.get_keys('twitter')

expiration = datetime.datetime.now() + datetime.timedelta(minutes=MINUTES_TO_LIVE)


def reset_lifetime():
    expiration = datetime.datetime.now() + datetime.timedelta(minutes=MINUTES_TO_LIVE)


def check_lifetime():
    if datetime.datetime.now() > expiration:
        sys.exit()


def get_input():
    sys.stdin.readline()
    pass


# Control Loop
while True:
    break
