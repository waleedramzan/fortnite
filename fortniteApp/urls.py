from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('', views.forniteData, name='forniteData'),
    url('getData', views.getData, name='getData'),
    url('nextLink', views.nextLink, name='nextLink'),
]
