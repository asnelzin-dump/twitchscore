from datetime import datetime
from pytz import UTC

from django.core.management import BaseCommand

from twitchscore.apps.accounts.models import User
from twitchscore.apps.stats.models import Game
from twitchscore.apps.utils.riot import RiotAPI


class Command(BaseCommand):

    def __init__(self):
        super(Command, self).__init__()
        self.games = []
        self.players = []
        self.stats = []

    def handle(self, *args, **options):
        for user in User.objects.all():
            riot_api = RiotAPI(user)
            games_data = riot_api.get_recent_games()
            if games_data is not None:
                for game_data in games_data:
                    self.create_game(game_data, user)

                user_games = Game.objects.filter(user=user)
                last_saved_games_ids = user_games.order_by('-create_date')[:10].values_list('game_id', flat=True)
                games = filter(lambda obj: obj.game_id not in last_saved_games_ids, self.games)
                print('\tFor user: {name} added {counter} games.'.format(name=user.summoner_name,
                                                                         counter=len(list(games))))
                Game.objects.bulk_create(games)
                self.games = []

    def create_game(self, game_data, user):
        game_data.update({'user': user})
        dt = datetime.fromtimestamp(game_data['create_date']/1000)
        game_data['create_date'] = dt.replace(tzinfo=UTC)

        stats_data = game_data.pop('stats')
        self.create_stats(stats_data)
        if 'fellow_players' in game_data:
            players_data = game_data.pop('fellow_players')
            for player_data in players_data:
                self.create_player(player_data)

        self.games.append(Game(**game_data))

    def create_stats(self, stats_data):
        pass

    def create_player(self, player_data):
        pass