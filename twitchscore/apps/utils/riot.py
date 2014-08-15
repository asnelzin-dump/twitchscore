import json
import re
import urllib.request
import urllib.parse
from twitchscore import settings


def camelcase_to_underscore(name):
    temp = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', temp).lower()


def fix_keys(obj):
    if isinstance(obj, dict):
        return {camelcase_to_underscore(key): fix_keys(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [fix_keys(value) for value in obj]
    else:
        return obj


class RiotAPI(object):
    URL_TEMPLATE = 'https://{region}.api.pvp.net/api/lol/{region}/v{version}/{command}/?api_key={api_key}'

    def __init__(self, user):
        self.user = user

    def get_id_by_name(self):
        version = '1.4'
        command = 'summoner/by-name/{summoner_name}'
        parameters = {
            'region': self.user.region.lower(),
            'summoner_name': urllib.parse.quote(self.user.summoner_name),
        }
        data = self._execute_command(command, version, parameters)
        if data is not None:
            _, val = data.popitem()
            return val['id']
        return None

    def get_recent_games(self):
        version = '1.3'
        command = 'game/by-summoner/{summoner_id}/recent'
        parameters = {
            'region': self.user.region.lower(),
            'summoner_id': self.user.summoner_id,
        }
        data = self._execute_command(command, version, parameters)
        if data is not None:
            return data['games']
        return None

    def _execute_command(self, command, version, parameters):
        url = self.URL_TEMPLATE.format(region=parameters['region'],
                                       version=version,
                                       command=command.format(**parameters),
                                       api_key=settings.RIOT_API_KEY)
        print(url)
        response = urllib.request.urlopen(url)
        if response.status == 200:
            raw_data = response.read().decode('utf8')
            return fix_keys(json.loads(raw_data))
        return None




