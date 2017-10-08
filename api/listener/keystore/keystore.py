import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(BASE_DIR + '/keystore/keystore', 'rb') as handle:
    secret = pickle.load(handle)


"""
return a list of keys associated with the service (django, azure, twitter)

structure of secret:
    'azure': {
        'COGNITIVE': '********************************',
    },
    'django': {
        'SECRET_KEY': '**************************************************',
    },
    'twitter': {      **************************************************
        'consumerKey': '*************************',
        'consumerSecret': '**************************************************',
        'tokenKey': '**************************************************',
        'tokenSecret': '*********************************************',
    }

"""


def get_keys(service):
    return secret[service]
