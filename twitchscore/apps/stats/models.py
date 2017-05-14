from django.db import models

from twitchscore.apps.summoners.models import Summoner


class SummonerStatistic(models.Model):
    summoner = models.ForeignKey(Summoner)
    games_played = models.IntegerField(verbose_name='Number of played games in database', blank=True, null=True)