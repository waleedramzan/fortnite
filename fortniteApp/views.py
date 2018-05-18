from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from django.template import loader
from django.urls import reverse


def index(request):
    template = loader.get_template("blog.html")
    return HttpResponse(template.render())

def getData(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'getData.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })


def forniteData(request):
    user = {}
    KEY = '3ffdffa5-7f61-4b2d-a21a-e3c0dea58e0f'
    if 'username' in request.GET:
        platform = request.GET['platform']
        username = request.GET['username']
        url = 'https://api.fortnitetracker.com/v1/profile/%s'%platform+'/%s/'%username

        headers = {'TRN-Api-Key': KEY}
        response = requests.get(url, headers=headers)
        key_array = ['Score', 'Matches Played', 'Wins', 'Win%', 'Kills', 'K/d']
        # key_array = key_array.json()
        if response.status_code == 200:
            user = response.json()
            return render(request, 'user-details.html',{'data': user, 'key_array': key_array})
    return render(request, 'fortniteData.html', {'user': user})


def nextLink(request, *args, **kwargs):
    pass

