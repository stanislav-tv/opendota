import requests
import json


def get_matches_player_id(steam_id, baseurl, endpoint):
    url = f"{baseurl}{steam_id}{endpoint}"
    print(url)
    data = requests.get(url)
    return json.loads(data.text)


def get_win(data):
    win = 0
    for data_match in data:
        if (data_match['player_slot'] < 128) and (data_match['radiant_win'] is True):
            win += 1
        elif (data_match['player_slot'] > 127) and (data_match['radiant_win'] is False):
            win += 1
    return win


def get_defeats(data):
    defeats = 0
    for data_match in data:
        if (data_match['player_slot'] < 128) and (data_match['radiant_win'] is False):
            defeats += 1
        elif (data_match['player_slot'] > 127) and (data_match['radiant_win'] is True):
            defeats += 1
    return defeats


def get_win_rate(data, win):
    games = len(data)
    return int(win) / int(games) * 100


def get_kda(data):
    kda = {'kills': 0, 'deaths': 0, 'assists': 0}
    for data_match in data:
        kda["kills"] += data_match['kills']
        kda["deaths"] += data_match['deaths']
        kda["assists"] += data_match['assists']
    return kda


def get_kills(kda):
    return kda["kills"]


def get_deaths(kda):
    return kda["deaths"]


def get_assists(kda):
    return kda["assists"]


base_url = 'https://api.opendota.com/api/players/'
endpoint = '/matches'

print('Enter your steam_id: ')
steamid = input()

data = get_matches_player_id(steamid, base_url, endpoint)

print('Statistics of Steam_id = ' + steamid)
print(f'Wins: {get_win(data)}')
print(f'Defeats: {get_defeats(data)}')
print(f'Winrate: {get_win_rate(data, get_win(data))}')
print(f"Kills: {get_kills(get_kda(data))}")
print(f"Deaths: {get_deaths(get_kda(data))}")
print(f"Assists: {get_assists(get_kda(data))}")
