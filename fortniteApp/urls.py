from django.conf.urls import url
from django.urls import path

from fortniteApp.views import *
from . import views

urlpatterns = [
    path('fortniteData', views.forniteData, name='forniteData'),
    url('cosmetics', CosmeticsView.as_view(), name='cometics'),
    url('weapons', WeaponsView.as_view(), name='cometics'),
]
