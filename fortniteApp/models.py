from django.db import models


class Cosmetics(models.Model):
    title = models.CharField(max_length=100)
    decsription = models.CharField(max_length=500)
    image = models.ImageField(upload_to='cosmetics_images')

    def __str__(self):
        return self.title


class CosmeticsBanner(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=10)
    image = models.ImageField(upload_to='cosmetics_banners')
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Weapons(models.Model):
    title = models.CharField(max_length=50)
    decsription = models.CharField(max_length=500)
    image = models.ImageField(upload_to='weapon_images')

    def __str__(self):
        return self.title

class WeaponSpecifications(models.Model):
    weapon_id = models.ForeignKey(Weapons, on_delete=models.CASCADE, related_name='weapons_related_name')
    # 1 for grey, 2 for green, 3 for blue, 4 for purple, 5 for gold
    weapon_rarity_type = models.IntegerField()
    dps = models.FloatField()
    damage = models.FloatField()
    env_damage =  models.FloatField()
    fire_rate = models.FloatField()
    magazine = models.FloatField()
    reload_time = models.CharField(max_length=20)
    body_shoot = models.FloatField()

    def __str__(self):
        return self.weapon_id.title