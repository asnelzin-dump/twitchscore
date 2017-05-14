from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from twitchscore.apps.summoners.views import SummonerCreate

urlpatterns = patterns(
    '',
    url(r'^add/$', login_required(SummonerCreate.as_view()), name='add')
)