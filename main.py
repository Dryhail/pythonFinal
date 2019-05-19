import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import numpy as np

games = pd.read_csv('games.csv');
wellness = pd.read_csv('wellness.csv');
rpe = pd.read_csv('rpe.csv');
#gps = pd.read_csv('gps.csv'); #You need to download this yourself. ver 25mb#

#total count of Nutrition values(Excellent v Okay v Poor)
#AIM:  plot excellent nutrition and poor nutrition vs.
#print(wellness.Nutrition.value_counts(sort=True))

#checks players who have poor nutrition
#wellness.loc[wellness["Nutrition"] == "Poor"]

#checks all players who have a desire greater or equal to 5, almost all have a good game readiness
#wellness.loc[wellness["Desire"] >= 5].sort_values(by="PlayerID")

#this is one of the games where they win, more than half of the team had excellent nutrition
#wellness.loc[wellness["Date"]=="2017-11-30"]

#thisis one of the games where they lost, they had half or less players with excellent nutrition
#wellness.loc[wellness["Date"]=="2017-12-01"]



#All games where the team won with the Date and convert to csv
game_wins = games.loc[games["Outcome"]=="W"][['GameID','Date','Outcome']]
game_wins.to_csv('game_wins', sep='\t')

#All games where the team lost with the Date and convert to csv
game_loss = games.loc[games["Outcome"]=="L"][['GameID','Date','Outcome']]
game_loss.to_csv('game_loss', sep='\t')



#data of players we wanna analyze
wellness_data = wellness.loc[wellness["TrainingReadiness"]>="0"][['Date','PlayerID','Desire','Nutrition','SleepQuality']].sort_values("PlayerID")
wellness_data.to_csv('wellness_data', sep='\t')


#games won with player analysis
wins_merged_data = wellness_data.merge(game_wins).sort_values('GameID')
wins_merged_data.to_csv('wins_merged_data',sep='\t')


#games lost with player analysis
loss_merged_data = wellness_data.merge(game_loss).sort_values('GameID')
loss_merged_data.to_csv('loss_merged_data',sep='\t')




