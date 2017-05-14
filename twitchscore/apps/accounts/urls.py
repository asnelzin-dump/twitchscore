from django.conf.urls import patterns, url
from twitchscore.apps.accounts.views import login

urlpatterns = patterns(
    '',
    url(r'^login/$', login, name='login')
)