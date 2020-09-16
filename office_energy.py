#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:30:25 2020

@author: dehajasenanayake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(0,'/Users/dehajasenanayake/Desktop')

fueltype_data = pd.read_excel('cfg_data.xlsx', sheet_name = 'fuel_type')
# fueltype_data.head(5)

# plt.figure(figsize=(9,9))
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Total'][0:6], label='Total',color='blue')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Coal'][0:6], label='Coal',color='red')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Oil'][0:6], label='Oil',color='brown')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Gas'][0:6], label='Gas',color='grey')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Nuclear'][0:6], label='Nuclear',color='orange')
# # plt.plot(fueltype_data['Month'][0:6],fueltype_data['Hydro'][0:6], label='Hydro')
# # plt.plot(fueltype_data['Month'][0:6],fueltype_data['Wind'][0:6], label='Wind')
# # plt.plot(fueltype_data['Month'][0:6],fueltype_data['Solar'][0:6], label='Solar')
# # plt.plot(fueltype_data['Month'][0:6],fueltype_data['Bioenergy'][0:6], label='Bioenergy')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Renewables'][0:6], label='Renewables',color='green')

# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Total'][12:18], label='Total',ls='--',color='blue')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Coal'][12:18], label='Coal',ls='--',color='red')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Oil'][12:18], label='Oil',ls='--',color='brown')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Gas'][12:18], label='Gas',ls='--',color='grey')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Nuclear'][12:18], label='Nuclear',ls='--',color='orange')
# # plt.plot(fueltype_data['Month'][12:18],fueltype_data['Hydro'][12:18], label='Hydro',ls='--')
# # plt.plot(fueltype_data['Month'][12:18],fueltype_data['Wind'][12:18], label='Wind',ls='--')
# # plt.plot(fueltype_data['Month'][12:18],fueltype_data['Solar'][12:18], label='Solar',ls='--')
# # plt.plot(fueltype_data['Month'][12:18],fueltype_data['Bioenergy'][12:18], label='Bioenergy',ls='--')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Renewables'][12:18], label='Renewables',ls='--',color='green')


# plt.xlabel('Month')
# plt.ylabel('Fuel used in electricity generation')
# plt.title('Generation of electricity by major producers in the UK')
# plt.legend()

"""Fuel Type and Stringency Index"""

fig, ax1 = plt.subplots()

ax1.plot(fueltype_data['Month'][0:6],fueltype_data['Total'][0:6], label='Total',color='blue')
ax1.plot(fueltype_data['Month'][0:6],fueltype_data['Coal'][0:6], label='Coal',color='red')
ax1.plot(fueltype_data['Month'][0:6],fueltype_data['Oil'][0:6], label='Oil',color='brown')
ax1.plot(fueltype_data['Month'][0:6],fueltype_data['Gas'][0:6], label='Gas',color='grey')
ax1.plot(fueltype_data['Month'][0:6],fueltype_data['Nuclear'][0:6], label='Nuclear',color='orange')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Hydro'][0:6], label='Hydro')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Wind'][0:6], label='Wind')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Solar'][0:6], label='Solar')
# plt.plot(fueltype_data['Month'][0:6],fueltype_data['Bioenergy'][0:6], label='Bioenergy')
ax1.plot(fueltype_data['Month'][0:6],fueltype_data['Renewables'][0:6], label='Renewables',color='green')

ax1.plot(fueltype_data['Date'][12:18],fueltype_data['Total'][12:18], label='Total',ls='--',color='blue')
ax1.plot(fueltype_data['Date'][12:18],fueltype_data['Coal'][12:18], label='Coal',ls='--',color='red')
ax1.plot(fueltype_data['Date'][12:18],fueltype_data['Oil'][12:18], label='Oil',ls='--',color='brown')
ax1.plot(fueltype_data['Date'][12:18],fueltype_data['Gas'][12:18], label='Gas',ls='--',color='grey')
ax1.plot(fueltype_data['Date'][12:18],fueltype_data['Nuclear'][12:18], label='Nuclear',ls='--',color='orange')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Hydro'][12:18], label='Hydro',ls='--')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Wind'][12:18], label='Wind',ls='--')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Solar'][12:18], label='Solar',ls='--')
# plt.plot(fueltype_data['Month'][12:18],fueltype_data['Bioenergy'][12:18], label='Bioenergy',ls='--')
ax1.plot(fueltype_data['Date'][12:18],fueltype_data['Renewables'][12:18], label='Renewables',ls='--',color='green')

ax1.set_xlabel('Date')
ax1.set_ylabel('Fuel type used in electricity generation in the UK')
ax1.legend()

ax2 = ax1.twinx()

stringency_dataset = pd.read_excel('stringency_dataset.xlsx', sheet_name='index_stringency')
ax2.plot(stringency_dataset['Date'], stringency_dataset['Index'], label='Date')
ax2.set_ylabel('UK Stringency Index (0-100)')

fig.tight_layout()
plt.title('Fuel type used in electricity generation in the UK vs Stringency Index for the UK')
plt.show()





