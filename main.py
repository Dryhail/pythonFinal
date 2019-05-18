import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import numpy as np

games = pd.read_csv('games.csv');
wellness = pd.read_csv('wellness.csv');
rpe = pd.read_csv('rpe.csv');
#gps = pd.read_csv('gps.csv'); #You need to download this yourself. ver 25mb#


print(games.columns)
print(games.head());
print(wellness.columns)
print(wellness.head());
print(rpe.columns)
print(rpe.head());
#print(gps.head());

#total count of Nutrition values(Excellent v Okay v Poor)
#AIM:  plot excellent nutrition and poor nutrition vs.
print(wellness.Nutrition.value_counts(sort=True))

