from django.db import models

RARITY_CHOICES = (
    ('COMMON','Common'),
    ('UNCOMMON', 'Uncommon'),
    ('RARE','Rare'),
    ('EPIC','Epic'),
    ('LEGENDARY','Legendary'),
)

class CosmeticCategory(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Cosmetics(models.Model):
    cosmetic_category = models.ForeignKey(CosmeticCategory, on_delete=models.CASCADE,
                                        related_name='cosmetic_category_related_name')
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20,default='type')
    rarity = models.CharField(max_length=9, choices=RARITY_CHOICES, default='EPIC')
    obtained = models.CharField(max_length=20,default='obtained')
    decsription = models.CharField(max_length=500)
    image = models.ImageField(upload_to='cosmetics_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CosmeticsPrimaryBanner(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20,default='type')
    rarity = models.CharField(max_length=9,choices=RARITY_CHOICES, default='grey')
    obtained = models.CharField(max_length=20,default='abc')
    image = models.ImageField(upload_to='cosmetics_banners')
    description = models.CharField(max_length=250)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CosmeticSecondaryBanner(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20,default='abc')
    rarity = models.CharField(max_length=9, choices=RARITY_CHOICES, default='grey')
    obtained = models.CharField(max_length=20,default='abc')
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='cosmetics_banners')
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WeaponCategory(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Weapons(models.Model):
    weapon_category = models.ForeignKey(WeaponCategory, on_delete=models.CASCADE, related_name='weapons_category_related_name')
    title = models.CharField(max_length=50)
    decsription = models.CharField(max_length=500)
    image = models.ImageField(upload_to='weapon_images')
    release_date = models.DateField()
    bullets_used = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WeaponSpecifications(models.Model):
    weapon_id = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='weapons_related_name')
    # 1 for grey, 2 for green, 3 for blue, 4 for purple, 5 for gold
    weapon_rarity_type = models.IntegerField()
    dps = models.CharField(max_length=10,default='N/A')
    damage = models.CharField(max_length=10,default='N/A')
    env_damage =  models.CharField(max_length=10,default='N/A')
    fire_rate = models.CharField(max_length=10,default='N/A')
    magazine = models.CharField(max_length=10,default='N/A')
    reload_time = models.CharField(max_length=20,default='N/A')
    body_shoot = models.CharField(max_length=10,default='N/A')
    head_shoot = models.CharField(max_length=10,default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.weapon_id.title


class WeaponsBanner(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='weapon_banners')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class WeaponsSpecificationsBanner(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='weapon_banners')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HomePageBanner(models.Model):
    image = models.ImageField(upload_to='homepage_banner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Media(models.Model):
    title = models.CharField(max_length=100)
    decsription = models.CharField(max_length=500)
    # type = models.CharField(max_length=20, default='type')
    # rarity = models.CharField(max_length=9, choices=RARITY_CHOICES, default='EPIC')
    # obtained = models.CharField(max_length=20, default='obtained')
    image = models.ImageField(upload_to='media_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MapCoordinates(models.Model):
    x_coordinate = models.CharField(max_length=100)
    y_coordinate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon_code = models.IntegerField(default=0)


class MainPageBlog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='home_blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MediaPageBanner(models.Model):
    title = models.CharField(max_length=200)
    # type = models.CharField(max_length=20,default='type')
    # rarity = models.CharField(max_length=9,choices=RARITY_CHOICES, default='grey')
    # obtained = models.CharField(max_length=20,default='abc')
    image = models.ImageField(upload_to='media_banners')
    description = models.CharField(max_length=250)
    # expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title