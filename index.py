import OpenDotaClient as ODClient
import StatisticCalculation as sc


print('Enter your steam_id: ')
steamid = input()
#147189593

data = ODClient.OpenDotaClient().get_matches_player_id(steamid)
stat_calculate = sc.StatisticCalculation()

print('Statistics of Steam_id = ' + steamid)
print(f'Wins: {stat_calculate.get_win(data)}')
print(f'Defeats: {stat_calculate.get_defeats(data)}')
print(f'Win rate: {stat_calculate.get_win_rate(data)}')
print(f"Kills: {stat_calculate.get_kills(data)}")
print(f"Deaths: {stat_calculate.get_deaths(data)}")
print(f"Assists: {stat_calculate.get_assists(data)}")
