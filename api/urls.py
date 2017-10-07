from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getData/$', views.get_data, name='getData'),
]
