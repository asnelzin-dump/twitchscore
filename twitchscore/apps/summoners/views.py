# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from twitchscore.apps.summoners.forms import CreateSummonerForm
from twitchscore.apps.summoners.models import Summoner


class SummonerCreate(SuccessMessageMixin, CreateView):
    model = Summoner
    form_class = CreateSummonerForm
    template_name = 'summoners/summoner_add.html'
    success_url = reverse_lazy('stats:stats_list')
    success_message = 'New summoner was created successfully'