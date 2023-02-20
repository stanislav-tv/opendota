class StatisticCalculation:

    @staticmethod
    def get_kda(data):
        kda = {'kills': 0, 'deaths': 0, 'assists': 0}
        for data_match in data:
            kda["kills"] += data_match['kills']
            kda["deaths"] += data_match['deaths']
            kda["assists"] += data_match['assists']
        return kda

    def get_win(self, data):
        win = 0
        for data_match in data:
            if (data_match['player_slot'] < 128) and (data_match['radiant_win'] is True):
                win += 1
            elif (data_match['player_slot'] > 127) and (data_match['radiant_win'] is False):
                win += 1
        return win

    def get_defeats(self, data):
        defeats = 0
        for data_match in data:
            if (data_match['player_slot'] < 128) and (data_match['radiant_win'] is False):
                defeats += 1
            elif (data_match['player_slot'] > 127) and (data_match['radiant_win'] is True):
                defeats += 1
        return defeats

    def get_win_rate(self, data):
        games = len(data)
        return int(self.get_win(data)) / int(games) * 100

    def get_kills(self, data):
        result = self.get_kda(data)
        return result['kills']

    def get_deaths(self, data):
        result = self.get_kda(data)
        return result['deaths']

    def get_assists(self, data):
        result = self.get_kda(data)
        return result['assists']

