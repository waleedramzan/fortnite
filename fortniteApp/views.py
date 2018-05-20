from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView
from zinnia.models import Entry

from fortniteApp.models import *


class FortniteView(TemplateView):
    template_name = 'fortniteData.html'

    def get(self, request, *args, **kwargs):
        user = {}
        KEY = '3ffdffa5-7f61-4b2d-a21a-e3c0dea58e0f'
        if 'username' in request.GET:
            platform = request.GET['platform']
            username = request.GET['username']
            url = 'https://api.fortnitetracker.com/v1/profile/%s' % platform + '/%s/' % username

            headers = {'TRN-Api-Key': KEY}
            response = requests.get(url, headers=headers)
            key_array = ['Score', 'Matches Played', 'Wins', 'Win%', 'Kills', 'K/d']
            # key_array = key_array.json()
            if response.status_code == 200:
                user = response.json()
                return render(request, 'user-details.html', {'data': user, 'key_array': key_array})
        return render(request, 'fortniteData.html', {'user': user})


class BlogView(TemplateView):
    template_name = "blog.html"

    def get(self, request, *args, **kwargs):
        entries = Entry.objects.all()
        return render(request, self.template_name, {'entries': entries})


class CosmeticsView(TemplateView):
    template_name = 'cosmetics.html'

    def get(self, request, *args, **kwargs):
        # return Cosmetics.objects.all()
        cosmetics_results = Cosmetics.objects.all()
        banner_results = CosmeticsBanner.objects.all()

        args = {'cosmetics': cosmetics_results, 'banners': banner_results}

        return render(request, self.template_name, args)


class WeaponsView(TemplateView):
    template_name = 'weapons.html'

    def get(self, request, *args, **kwargs):
        weapons_results = Weapons.objects.all()
        args = {'weapons': weapons_results}
        return render(request, self.template_name, args)


class WeaponSpecificationsView(TemplateView):
    template_name = 'weapon_specifications.html'

    def get(self, request, *args, **kwargs):
        selected_weapon = self.kwargs['weapon_id']
        weapon_specs_object = WeaponSpecifications.objects.filter(weapon_id=selected_weapon).order_by('weapon_rarity_type')
        weapon_object = Weapons.objects.get(id=selected_weapon)
        args = {'weapon_details': weapon_specs_object , 'weapon':weapon_object}
        return render(request, self.template_name, args)
