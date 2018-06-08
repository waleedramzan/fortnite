from django.contrib import admin
from fortniteApp.models import *

# Register your models here.


class WeaponSpecificationsInline(admin.StackedInline):
    model = WeaponSpecifications


class WeaponClass(admin.ModelAdmin):
    inlines = [WeaponSpecificationsInline]


admin.site.register(Weapons, WeaponClass)

# admin.site.register(Weapons)
# admin.site.register(WeaponSpecifications)
admin.site.register(WeaponCategory)
admin.site.register(CosmeticCategory)
admin.site.register(Cosmetics)
admin.site.register(CosmeticsPrimaryBanner)
admin.site.register(WeaponsBanner)
admin.site.register(CosmeticSecondaryBanner)
admin.site.register(WeaponsSpecificationsBanner)
admin.site.register(HomePageBanner)
admin.site.register(Media)
admin.site.register(MainPageBlog)
