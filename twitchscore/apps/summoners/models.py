from django.db import models

from twitchscore.apps.utils.riot import RiotAPI


class Summoner(models.Model):
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
    name = models.CharField(max_length=255, verbose_name='Summoner name')
    riot_id = models.IntegerField(blank=True)
    region = models.SmallIntegerField(choices=REGION_CHOICES)

    class Meta:
        verbose_name = 'Summoner'
        verbose_name_plural = 'Summoners'
        ordering = ['-pk']

    def save(self, *args, **kwargs):
        if not self.riot_id:
            riot_api = RiotAPI(self)
            self.riot_id = riot_api.get_id_by_name()
        super(Summoner, self).save(*args, **kwargs)

    def get_region_name(self):
        return dict(self.REGION_CHOICES)[self.region]
