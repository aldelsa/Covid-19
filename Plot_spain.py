#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import os
from six.moves import urllib

DATASET_PATH = "datasets/spain"
DATASET_URL = "https://raw.githubusercontent.com/datadista/datasets/master/COVID%2019/nacional_covid19.csv"

def download_load_data(dataset_path=DATASET_PATH):
    csv_path = os.path.join(DATASET_PATH, "nacional_covid19.csv")
    urllib.request.urlretrieve(DATASET_URL, csv_path )
    return pd.read_csv(csv_path,sep=',')



# In[11]:


virus = download_load_data()
virus.loc[:,"fecha"] = pd.to_datetime(virus['fecha'], format='%Y/%m/%d')
virus.head()


# In[12]:


virus_spain = virus.loc[virus['fecha'] > "2020-02-25"]
virus_spain.sort_values(by=['fecha'])


# In[17]:


import matplotlib.dates as mdates
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20, 10]
fig, ax = plt.subplots()

x = virus_spain['fecha']
y = virus_spain['casos']
z = virus_spain['fallecimientos']
z1 = virus_spain['altas']
z2 = virus_spain['ingresos_uci']
z3 = virus_spain['hospitalizados']


ax.plot(x,y, linestyle='--', marker='x', color='b', label='Casos')
ax.plot(x,z, linestyle='--', marker='x', color='r', label='Fallecimientos')
ax.plot(x,z1, linestyle='--', marker='x', color='g', label='Altas')
ax.plot(x,z2, linestyle='--', marker='x', color='y', label='Ingresos UCI')
ax.plot(x,z3, linestyle='--', marker='x', label='Hospitalizados')

ax.grid()
plt.xticks(x)
plt.legend()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.savefig('sample.png')


# In[ ]:
