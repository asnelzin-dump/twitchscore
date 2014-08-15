from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from twitchscore.apps.utils.riot import RiotAPI


class User(AbstractBaseUser):
    REGION_CHOICES = (
        (1, 'BR'),
        (2, 'EUNE'),
        (3, 'EUW'),
        (4, 'KR'),
        (5, 'LAN'),
        (6, 'LAS'),
        (7, 'NA'),
        (8, 'OCE'),
        (9, 'RU'),
        (10, 'TR'),
    )

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)

    summoner_name = models.CharField(max_length=255)
    summoner_id = models.IntegerField(blank=True)
    region = models.CharField(max_length=3, choices=REGION_CHOICES)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.summoner_id:
            riot_api = RiotAPI(self)
            self.summoner_id = riot_api.get_id_by_name()
        super(User, self).save(*args, **kwargs)



