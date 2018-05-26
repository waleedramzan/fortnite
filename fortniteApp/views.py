from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.template import loader
from django.views import View
from django.views.generic import TemplateView, RedirectView, CreateView
from zinnia.models import Entry
import datetime
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt

from fortniteApp.models import *


class FortniteView(TemplateView):
    template_name = 'fortniteData.html'

    def get(self, request, *args, **kwargs):
        user = {}
        KEY = '3ffdffa5-7f61-4b2d-a21a-e3c0dea58e0f'
        home_banner = ''
        if HomePageBanner.objects.filter():
            home_banner = HomePageBanner.objects.filter().order_by('-id')[0]

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

        args = {'cosmetics': media_results}

        return render(request, self.template_name, args)

@csrf_exempt
def map_view(request):
    template_name = 'map.html'
    if request.method == 'POST':
        map_coordinates = MapCoordinates()
        map_coordinates.x_coordinate = request.POST['x_cord']
        map_coordinates.y_coordinate = request.POST['y_cord']
        map_coordinates.save()

    all_marked_locations = MapCoordinates.objects.filter()
    map_pins =[]
    for foo in all_marked_locations:
        pin_info = {}
        pin_info['id'] = foo.id
        pin_info['xcoord'] = foo.x_coordinate
        pin_info['ycoord'] = foo.y_coordinate
        map_pins.append(pin_info)

    # also tried to pass pin_info in arguments
    args = {'marked_locations': map_pins}
    return render(request,template_name,args)