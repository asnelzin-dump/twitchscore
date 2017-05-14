from django.conf.urls import patterns, url
from twitchscore.apps.stats.views import SummonerStatisticListView

urlpatterns = patterns(
    '',
    url(r'^$', SummonerStatisticListView.as_view(), name='stats_list')
)