# Using Online Job Adverts as indicators of Industry's Status

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import seaborn as sns
import datetime

sns.set_style('whitegrid')

# - - - - - - - - - - - - - - - - - - - - - - -
# 1. Collect OnlineJobAdverts Postings

df = pd.read_excel(r'data/OnlineJobAdverts.xlsx')

# 2. Clean for use
# Focus on Catering and Hospitality

Catering_Hospitality = df[12:14]
Months = df[1:2].to_numpy()

Fig = plt.figure()
plt.title("2019 to 2020 Catering and Hospitality Job Adverts Postings")
x = md.DateFormatter('%Y-%m-%d')
ax = plt.gca()
ax.xaxis.set_major_formatter(x)
plt.plot(Months[0, 2:], Catering_Hospitality.to_numpy()[0,2:]) # 2019
plt.plot(Months[0, 2:38], Catering_Hospitality.to_numpy()[1,2:38]) # 2020

# Web Scraping for more specific 'Delivery' jobs available?

# - - - - - - - - - - - - - - - - - - - - - - -
# 2. Online Food Delivery Market

# https://www.statista.com/outlook/374/100/online-food-delivery/worldwide#market-users


