from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getEvents', views.get_events, name='getEvents'),
    url(r'^getTweets', views.get_tweets, name='getTweets'),
    url(r'^addTracker', views.add_tracker, name='addTracker'),
    url(r'^removeTracker', views.remove_tracker, name='removeTracker'),
]
