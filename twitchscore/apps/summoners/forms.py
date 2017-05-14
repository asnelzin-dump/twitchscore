# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from twitchscore.apps.summoners.models import Summoner


class CreateSummonerForm(forms.ModelForm):

    class Meta:
        model = Summoner
        fields = ('name', 'region')