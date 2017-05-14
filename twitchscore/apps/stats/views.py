from django.views.generic.list import ListView
from twitchscore.apps.stats.models import SummonerStatistic


class SummonerStatisticListView(ListView):
    model = SummonerStatistic
    template_name = 'stats/statistics_list.html'
