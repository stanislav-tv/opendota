import requests
import json


class OpenDotaClient:
    __base_url = 'https://api.opendota.com/api/players/'
    __matches_endpoint = '/matches'

    @classmethod
    def validate(cls, steam_id: str):
        return len(steam_id) == 9

    def get_matches_player_id(self, steam_id):
        if self.validate(steam_id):
            url = f"{self.__base_url}{steam_id}{self.__matches_endpoint}"
            data = requests.get(url)
            return json.loads(data.text)





