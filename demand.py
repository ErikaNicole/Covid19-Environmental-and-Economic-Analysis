#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:45:12 2020

@author: dehajasenanayake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(0,'/Users/dehajasenanayake/Desktop')

demand_full = pd.read_excel('cfg_data.xlsx', sheet_name = 'demand_full')
demand_daily = pd.read_excel('cfg_data.xlsx', sheet_name = 'demand_daily')

# plt.figure(figsize =(15,9))
# plt.plot(demand_full['Date'],demand_full['Demand'])
# plt.plot(demand_daily['Date'],demand_daily['avdemand'])

# plt.xlabel('Date')
# plt.ylabel('Rolling Demand')
# plt.title('Electricity Demand from consumers in the UK')
# plt.legend()

"""Rolling demand vs Stringency Index"""

fig, ax1 = plt.subplots()
ax1.plot(demand_daily['Date'],demand_daily['avdemand'])
ax1.set_xlabel('Date')
ax1.set_ylabel('Rolling Demand from consumers in the UK')
ax1.legend()

ax2 = ax1.twinx()

stringency_dataset = pd.read_excel('stringency_dataset.xlsx', sheet_name='index_stringency')
ax2.plot(stringency_dataset['Date'], stringency_dataset['Index'], label='Date')
ax2.set_ylabel('UK Stringency Index (0-100)')

fig.tight_layout()
plt.title('Rolling System Demand in the UK vs Stringency Index for the UK')
plt.show()