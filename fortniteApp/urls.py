from django.conf.urls import url
from django.urls import path

from fortniteApp.views import *
from . import views

urlpatterns = [
    url('cosmetics', CosmeticsView.as_view(), name='cometics'),
    url('weapons', WeaponsView.as_view(), name='cometics'),
    url('blog', BlogView.as_view(), name='blog'),
]
