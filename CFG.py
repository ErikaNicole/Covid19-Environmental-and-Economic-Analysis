#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:12:31 2020

@author: dehajasenanayake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(0,'/Users/dehajasenanayake/Desktop')

av_consumption = pd.read_excel('CFG1.xls', sheet_name = 'Month')
av_consumption = av_consumption.copy()
# av_consumption.head(5)

# plt.figure(figsize=(9,4))
# plt.plot(av_consumption['Month'][0:11],av_consumption['Total'][0:11], label='Total',color='b',ls='--')
# plt.plot(av_consumption['Month'][0:11],av_consumption['Industrial'][0:11], label='Industrial',color='r',ls='--')
# plt.plot(av_consumption['Month'][0:11],av_consumption['Domestic'][0:11], label='Domestic',color='g',ls='--')
# plt.plot(av_consumption['Month'][0:11],av_consumption['Other'][0:11], label='Other',color='y',ls='--')

# plt.plot(av_consumption['Month'][12:17],av_consumption['Total'][12:17], label='Total',color='b')
# plt.plot(av_consumption['Month'][12:17],av_consumption['Industrial'][12:17], label='Industrial',color='r')
# plt.plot(av_consumption['Month'][12:17],av_consumption['Domestic'][12:17], label='Domestic',color='g')
# plt.plot(av_consumption['Month'][12:17],av_consumption['Other'][12:17], label='Other',color='y')

# plt.xlabel('Month')
# plt.ylabel('Sales of electricity, TWh')
# plt.title('Consumption of electricity by consumers in the UK')
# plt.legend()
# #
# #"""Stringency Data"""
# #
stringency_dataset = pd.read_excel('stringency_dataset.xlsx', sheet_name='index_stringency')
# plt.plot(stringency_dataset['Date'], stringency_dataset['Index'], label='Date')
# plt.xlabel('Date')
# plt.ylabel('UK Stringency Index (0-100)')
# plt.legend()

"""Both Stringency and Energy Data"""

fig, ax1 = plt.subplots()

ax1.plot(av_consumption['Date'][12:17],av_consumption['Total'][12:17], label='Total 2020',color='b')
ax1.plot(av_consumption['Date'][12:17],av_consumption['Industrial'][12:17], label='Industrial 2020',color='r')
ax1.plot(av_consumption['Date'][12:17],av_consumption['Domestic'][12:17], label='Domestic 2020',color='g')
ax1.plot(av_consumption['Date'][12:17],av_consumption['Other'][12:17], label='Other 2020',color='y')

ax1.set_xlabel('Date')
ax1.set_ylabel('Sales of electricity, TWh')
ax1.legend()

ax2 = ax1.twinx()

ax2.plot(stringency_dataset['Date'], stringency_dataset['Index'], label='Date')
ax2.set_ylabel('UK Stringency Index (0-100)')

fig.tight_layout()
plt.title('Consumption of electricity by consumers in the UK vs Stringency Index for the UK')
plt.show()










