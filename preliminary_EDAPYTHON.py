
# coding: utf-8

# In[21]:


#import all the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import pandas_profiling as pdpf
from pandas import DataFrame


# In[22]:


games = pd.read_csv('games.csv')
gps = pd.read_csv('gps.csv')
rpe = pd.read_csv('rpe.csv')
wellness = pd.read_csv('wellness.csv')


# In[23]:


games.head()


# In[24]:


gps.head()


# In[25]:


rpe.head()


# In[26]:


wellness.head()


# In[27]:


AverageScore = wellness.groupby('PlayerID').MonitoringScore.mean()
AverageScore


# In[28]:


data = {'AverageScore':AverageScore}
frame = DataFrame(data)
frame


# In[29]:


wellness
wellness.shape


# In[30]:


temp = pd.merge(wellness, frame, on = 'PlayerID')
temp.head()


# In[31]:


temp['DeviationScore'] = (temp['MonitoringScore'] - temp['AverageScore'])**2 
temp


# In[32]:


calc = temp[['PlayerID', '' 'DeviationScore']]
calc = calc.groupby('PlayerID').sum().rename(columns={'DeviationScore':'TotalScore'})
calc


# In[33]:


temp = pd.merge(temp, calc, on = 'PlayerID')


# In[34]:


temp['DeviationScore'] = 0
totals = temp[['PlayerID', 'TotalScore']].groupby('PlayerID').count()


# In[35]:


temp = pd.merge(temp, totals, on = 'PlayerID')


# In[36]:


temp['DeviationScore'] = (temp['TotalScore_x'] / temp['TotalScore_y'])**.5


# In[37]:


temp = temp.rename(columns={'DeviationScore':'veriance'})


# In[38]:


use = temp[['Date','PlayerID', 'MonitoringScore', 'AverageScore', 'veriance']]


# In[39]:


use


# In[44]:


use['PercentVariance'] = (use['MonitoringScore'] - use['AverageScore']) / 2 / (use['MonitoringScore'] + use['AverageScore'])* 100


# In[46]:


use.groupby('PlayerID').max()

