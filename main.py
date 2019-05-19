import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import numpy as np

games = pd.read_csv('games.csv');
wellness = pd.read_csv('wellness.csv');
rpe = pd.read_csv('rpe.csv');
gps = pd.read_csv('gps.csv'); #You need to download this yourself. ver 25mb#

#total count of Nutrition values(Excellent v Okay v Poor)
#AIM:  plot excellent nutrition and poor nutrition vs.
print(wellness.Nutrition.value_counts(sort=True))

#checks players who have poor nutrition
wellness.loc[wellness["Nutrition"] == "Poor"]

#checks all players who have a desire greater or equal to 5, almost all have a good game readiness
wellness.loc[wellness["Desire"] >= 5].sort_values(by="PlayerID")

#this is one of the games where they win, more than half of the team had excellent nutrition
wellness.loc[wellness["Date"]=="2017-11-30"]

#thisis one of the games where they lost, they had half or less players with excellent nutrition
wellness.loc[wellness["Date"]=="2017-12-01"]