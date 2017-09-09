import urllib.request
from json import loads
import csv
from time import sleep


year = 1920
temp_cab = []
while year < 2016:
    year_id = str(year)
    target_url = 'http://mlb.mlb.com/lookup/json/named.team_hitting_season_leader_master.bam?season=' + year_id +\
                 '&sort_order=%27desc%27&sort_column=%27hr%27&game_type=%27R%27&sport_code=%27mlb%27&recSP=1&recPP=50'
    req = urllib.request.urlopen(target_url)
    data = loads(req.read().decode())
    for item in data:
        print (item)
    for item in data['team_hitting_season_leader_master']['queryResults']['row']:
        temp_cab.append([year,item['team_abbrev'], item['hr']])
    sleep(2)
    year += 1
with open('hr.csv', 'w', newline='') as hr_csv:
    writer = csv.writer(hr_csv)
    writer.writerows(temp_cab)