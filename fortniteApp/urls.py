from django.conf.urls import url
from django.urls import path

from fortniteApp.views import *
from . import views

app_name = 'fortniteApp'
urlpatterns = [
    url('cosmetics', CosmeticsView.as_view(), name='cometics'),
    url('blog', BlogView.as_view(), name='blog'),
    url('weapons/$', WeaponsView.as_view(), name='weapons'),
    url('weapon_specifications/(?P<weapon_id>\d+)/$', WeaponSpecificationsView.as_view(), name='weapon_specifications'),
    url('media', MediaView.as_view(), name='media'),
    url('map', views.map_view, name='map'),
]
