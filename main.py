import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import numpy as np

games = pd.read_csv('games.csv');
wellness = pd.read_csv('wellness.csv');
rpe = pd.read_csv('rpe.csv');
#gps = pd.read_csv('gps.csv'); #You need to download this yourself. ver 25mb#


games_group = games.groupby("Date")
print(games)
print(games_group)
#print(gps.head());

wellness.loc[wellness["Nutrition"] == "Poor"]
