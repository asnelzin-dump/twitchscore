import logging
from datetime import datetime
from pytz import UTC

from django.core.management import BaseCommand

from twitchscore.apps.accounts.models import User
from twitchscore.apps.games.models import Game, Stats, Player
from twitchscore.apps.utils.riot import RiotAPI

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def __init__(self):
        super(Command, self).__init__()
        self.games = []
        self.players = []
        self.stats = []

    def handle(self, *args, **options):
        for user in User.objects.all():
            riot_api = RiotAPI(user)
            recent_games_data = riot_api.get_recent_games()
            if recent_games_data is not None:
                user_games = Game.objects.filter(user=user)
                last_saved_games_ids = user_games.order_by('-create_date')[:10].values_list('id', flat=True)
                unsaved_games_data = filter(lambda obj: obj['game_id'] not in last_saved_games_ids, recent_games_data)
                for data in unsaved_games_data:
                    self.create_references(data, user)

                Game.objects.bulk_create(self.games)
                Stats.objects.bulk_create(self.stats)
                Player.objects.bulk_create(self.players)
                logger.info('For user: {name} added {counter} games.'.format(name=user.summoner_name,
                                                                             counter=len(self.games)))
                self.games = []
                self.stats = []
                self.players = []

    def create_references(self, data, user):
        stats_data = data.pop('stats')
        players_data = data.pop('fellow_players', None)
        game = self.create_game(data, user)
        self.create_stats(stats_data, game)
        if players_data:
            for player_data in players_data:
                self.create_player(player_data, game)

    def create_game(self, game_data, user):
        game_data.update({'id': game_data.pop('game_id')})
        game_data.update({'user': user})
        dt = datetime.fromtimestamp(game_data['create_date']/1000)
        game_data['create_date'] = dt.replace(tzinfo=UTC)
        game = Game(**game_data)
        self.games.append(game)
        return game

    def create_stats(self, stats_data, game):
        stats_data.update({'game': game})
        self.stats.append(Stats(**stats_data))

    def create_player(self, player_data, game):
        player_data.update({'game': game})
        self.players.append(Player(**player_data))