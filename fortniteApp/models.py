from django.db import models

RARITY_CHOICES = (
    ('COMMON','Common'),
    ('UNCOMMON', 'Uncommon'),
    ('RARE','Rare'),
    ('EPIC','Epic'),
    ('LEGENDARY','Legendary'),
)

class Cosmetics(models.Model):
    title = models.CharField(max_length=100)
    decsription = models.CharField(max_length=500)
    image = models.ImageField(upload_to='cosmetics_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CosmeticsPrimaryBanner(models.Model):
    title = models.CharField(max_length=200)
    rarity = models.CharField(max_length=9,choices=RARITY_CHOICES, default='grey')
    image = models.ImageField(upload_to='cosmetics_banners')
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CosmeticSecondaryBanner(models.Model):
    title = models.CharField(max_length=100)
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
    dps = models.CharField(max_length=10)
    damage = models.CharField(max_length=10)
    env_damage =  models.CharField(max_length=10)
    fire_rate = models.CharField(max_length=10)
    magazine = models.CharField(max_length=10)
    reload_time = models.CharField(max_length=20)
    body_shoot = models.CharField(max_length=10)
    head_shoot = models.CharField(max_length=10)
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
    image = models.ImageField(upload_to='media_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title