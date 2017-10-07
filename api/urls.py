from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getData', views.get_data, name='getData'),
    url(r'^addTracker', views.add_tracker, name='addTracker'),
    url(r'^removeTracker', views.remove_tracker, name='removeTracker'),
]
