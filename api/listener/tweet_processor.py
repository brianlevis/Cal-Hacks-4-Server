# In the future, import list of keyword sets from listener.py- for now, just a list of our keywords
KEYWORD_SETS = [
    ('protest', 'rally', 'controversial speaker'),
    ('game', 'football'),
]

"""

keywords: list-like of tweets

return a list-like of hashtags

"""


def extract_hashtags(tweets, keyword_sets):
    pass


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
