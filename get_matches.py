from riotwatcher import LolWatcher
import pandas as pd

#Riot API Key 
lol_watcher = LolWatcher('Insert Riot API Key Here')

my_region = 'na1' #insert region for a certain user
me = lol_watcher.summoner.by_name(my_region, 'ItadoriYuujii') #insert username 

#get last 500 matches
match_history = []
for i in range(5):
    match_history.append(lol_watcher.match.matchlist_by_puuid('americas', me['puuid'],start=(i*100),count=100))
matches = [item for sublist in match_history for item in sublist]

#initialize lists for different features
assists = []
neutral_minions_killed = []
user_name = []
game_length = []
gold_earned = []
jg_cs_10min = []
lane_minions_10min = []
skillshots_dodged = []
skillshots_hit = []
solo_kills = []
vision_score = []
champ_name = []
position = []
damage_dealt = []
total_minions_killed = []
first_baron = []
baron_kills = []
first_blood = []
team_kills = []
first_drag = []
dragon_kills = []
first_inhib = []
inhib_kills = []
first_rift = []
herald_kills = []
first_tower = []
tower_kills = []
damage_taken = []
damage_shielded = []
kills = []
deaths = []
win = []

#run through matches and append to appropriate list 
for m in range(len(matches)):

    match = lol_watcher.match.by_id('americas',match_id=matches[m])
    stats = match['info']['participants']

    for i in range(len(stats)):
        player = stats[i]
        if player['summonerName'] == 'ItadoriYuujii':
            
            for j in range(2):
                if player['teamId'] == match['info']['teams'][j]['teamId']:
                    first_baron.append(match['info']['teams'][j]['objectives']['baron']['first'])
                    baron_kills.append(match['info']['teams'][j]['objectives']['baron']['kills'])
                    first_blood.append(match['info']['teams'][j]['objectives']['champion']['first'])
                    team_kills.append(match['info']['teams'][j]['objectives']['champion']['kills'])
                    first_drag.append(match['info']['teams'][j]['objectives']['dragon']['first'])
                    dragon_kills.append(match['info']['teams'][j]['objectives']['dragon']['kills'])
                    first_inhib.append(match['info']['teams'][j]['objectives']['inhibitor']['first'])
                    inhib_kills.append(match['info']['teams'][j]['objectives']['inhibitor']['kills'])
                    first_rift.append(match['info']['teams'][j]['objectives']['riftHerald']['first'])
                    herald_kills.append(match['info']['teams'][j]['objectives']['riftHerald']['kills'])
                    first_tower.append(match['info']['teams'][j]['objectives']['tower']['first'])
                    tower_kills.append(match['info']['teams'][j]['objectives']['tower']['kills'])
                
            assists.append(player['assists'])
            neutral_minions_killed.append(player['neutralMinionsKilled'])
            user_name.append(player['summonerName'])
            game_length.append(match['info']['gameDuration'])
            champ_name.append(player['championName'])
            position.append(player['individualPosition'])
            total_minions_killed.append(player['totalMinionsKilled']) 
            damage_taken.append(player['totalDamageTaken'])
            gold_earned.append(player['goldEarned'])
            vision_score.append(player['visionScore'])
            damage_dealt.append(player['totalDamageDealt'])
            kills.append(player['kills'])
            deaths.append(player['deaths'])
            damage_shielded.append(player['totalDamageShieldedOnTeammates'])
            win.append(player['win'])
            
            if 'challenges' in player:
                jg_cs_10min.append(player['challenges']['jungleCsBefore10Minutes'])
                lane_minions_10min.append(player['challenges']['laneMinionsFirst10Minutes'])
                skillshots_dodged.append(player['challenges']['skillshotsDodged'])
                skillshots_hit.append(player['challenges']['skillshotsHit'])
                solo_kills.append(player['challenges']['soloKills'])
            else:
                jg_cs_10min.append('NA')
                lane_minions_10min.append('NA')
                skillshots_dodged.append('NA')
                skillshots_hit.append('NA')
                solo_kills.append('NA')
            
#create a raw data list
raw_data = [user_name,champ_name,position,kills,deaths,assists,neutral_minions_killed,game_length,
            gold_earned,jg_cs_10min,lane_minions_10min,skillshots_dodged,skillshots_hit,solo_kills,
            vision_score,damage_dealt,total_minions_killed,first_baron,baron_kills,
            first_blood,team_kills,first_drag,dragon_kills,first_inhib,inhib_kills,first_rift,
            herald_kills,first_tower,tower_kills,damage_taken,damage_shielded,win] 

#create data frame with the raw data
raw_df = pd.DataFrame(raw_data).transpose()       

#name columns
new_columns = ['Username','Champ Name','Position','Kills','Deaths','Assists',
            'Neutral Minions Killed','Game Length','Gold Earned','Jungle CS Under 10 Min',
            'Lane Minions Under 10 Min','Skillshots Dodged','Skillshots Hit','Solo Kills','Vision Score',
            'Damage Dealt','Total Minions Killed','First Baron','Baron Kills','First Blood',
            'Team Kills','First Drag','Dragon Kills','First Inhib','Inhib Kills','First Rift',
            'Herald Kills','First Tower','Tower Kills','Damage Taken','Damage Shielded','Win']
raw_df.columns = new_columns

#export data frame to a csv
raw_df.to_csv('lol_raw_data.csv')
            
            
            
            
            
            
            
            
            
            
            
            