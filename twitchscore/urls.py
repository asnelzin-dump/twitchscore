from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^accounts/', include('twitchscore.apps.accounts.urls', namespace='accounts')),
    url(r'^summoners/', include('twitchscore.apps.summoners.urls', namespace='summoners')),
    url(r'^stats/', include('twitchscore.apps.stats.urls', namespace='stats')),

    url(r'^admin/', include(admin.site.urls)),
)
