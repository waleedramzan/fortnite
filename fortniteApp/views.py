import json

from django.contrib import messages
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.template import loader
from django.views import View
from django.views.generic import TemplateView, RedirectView, CreateView
from psycopg2.extensions import JSON
from zinnia.models import Entry
import datetime
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt

from fortniteApp.models import *


class FortniteView(TemplateView):
    template_name = 'fortniteData.html'

    def get(self, request, *args, **kwargs):
        user = {}
        entree = ''
        home_banner = ''
        if HomePageBanner.objects.filter():
            home_banner = HomePageBanner.objects.filter().order_by('-id')[0]

        if 'username' in request.GET:

            if 'platform' in request.GET:
                platform = request.GET['platform']
                username = request.GET['username']
                headers = {
                    'authorization': 'a54432b15b52e4c14e2ac8d32994bca7',
                }
                url = 'https://fortniteapi.com/api/getUserID'
                data = {
                    "username": username
                }
                response = requests.post(url,headers=headers, data=data)

                if response.status_code == 200:
                    user = response.json()
                    if 'error' in user:
                        if user['error'] == True:
                            entree = Entry.objects.first()
                            validation_error = "This user does not exist or didn't play fortnite"
                            return render(request, 'fortniteData.html',
                                          {'user': user, 'entree': entree, 'home_banner': home_banner,
                                           'validation_error': validation_error})

                    else:
                        user_id = user['uid']
                        next_url = 'https://fortniteapi.com/api/playerData'
                        new_data = {
                            "user_id": user_id,
                            "platform": platform,
                            "window": "alltime"
                        }
                        new_response = requests.post(next_url, headers=headers, data=new_data)

                        if new_response.status_code == 200:
                            user_profile = new_response.json()
                            return render(request, 'user-details.html', {'data': user_profile})
            else:
                entree = Entry.objects.first()
                validation_error = "Please chose the platform first"
                return render(request, 'fortniteData.html',
                              {'user': user, 'entree': entree, 'home_banner': home_banner, 'validation_error': validation_error})
        else:
            entree = Entry.objects.first()
        return render(request, 'fortniteData.html', {'user': user, 'entree': entree, 'home_banner': home_banner})


class BlogView(TemplateView):
    template_name = "blog.html"

    def get(self, request, *args, **kwargs):
        entries = Entry.objects.all()
        return render(request, self.template_name, {'entries': entries})


class CosmeticsView(TemplateView):
    template_name = 'cosmetics.html'

    def get(self, request, *args, **kwargs):
        cosmetics_results = Cosmetics.objects.all()
        primary_banner = CosmeticsPrimaryBanner.objects.filter(expiry_date__gt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        secondary_banner = CosmeticSecondaryBanner.objects.filter(expiry_date__gt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        args = {'cosmetics': cosmetics_results, 'banners': primary_banner, 'secondaryBanner': secondary_banner}

        return render(request, self.template_name, args)


class WeaponsView(TemplateView):
    template_name = 'weapons.html'

    def get(self, request, *args, **kwargs):
        weapons_results = Weapons.objects.all()
        weapon_banner = ''
        if WeaponsBanner.objects.filter():
            weapon_banner = WeaponsBanner.objects.filter().order_by('-id')[0]
        weapon_category = WeaponCategory.objects.all()

        args = {'weapons': weapons_results , 'weapon_banner': weapon_banner, 'weapon_categories': weapon_category}
        return render(request, self.template_name, args)


class WeaponSpecificationsView(TemplateView):
    template_name = 'weapon_specifications.html'

    def get(self, request, *args, **kwargs):
        selected_weapon = self.kwargs['weapon_id']
        weapon_specs_object = WeaponSpecifications.objects.filter(weapon_id=selected_weapon).order_by('weapon_rarity_type')
        weapon_object = Weapons.objects.get(id=selected_weapon)
        weapon_specification_banner = WeaponsSpecificationsBanner.objects.get()
        args = {'weapon_details': weapon_specs_object , 'weapon':weapon_object, 'specs_banner':weapon_specification_banner}
        return render(request, self.template_name, args)


class MediaView(TemplateView):
    template_name = 'media_page.html'

    def get(self, request, *args, **kwargs):
        media_results = Media.objects.all()
        primary_banner = CosmeticsPrimaryBanner.objects.filter(
            expiry_date__gt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        args = {'cosmetics': media_results, 'banners': primary_banner}

        return render(request, self.template_name, args)

@csrf_exempt
def map_view(request):
    template_name = 'map.html'
    if request.method == 'POST':
        if 'remove' in request.POST:
            pin = MapCoordinates.objects.get(id=int(request.POST['marker_id']))
            pin.delete()
        else:
            map_coordinates = MapCoordinates()
            map_coordinates.x_coordinate = request.POST['x_cord']
            map_coordinates.y_coordinate = request.POST['y_cord']
            map_coordinates.save()

    all_marked_locations = MapCoordinates.objects.filter()
    map_pins =[]
    for foo in all_marked_locations:
        pin_info = {}
        pin_info['id']=foo.id
        pin_info['title']='map pin ' + str(foo.id)
        pin_info['xcoord']=foo.x_coordinate
        pin_info['ycoord']=foo.y_coordinate
        map_pins.append(pin_info)
    args = {'marked_locations': map_pins}
    return render(request,template_name,args)