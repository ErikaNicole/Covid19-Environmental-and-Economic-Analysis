# File to examine the following questions

# IMPORTS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import seaborn as sns
import datetime

sns.set_style('whitegrid')

# - - - - - - - - - - - - - - - - - - - - - - -
# 1. Collect Traffic Cam Data

df = pd.read_excel(r'data/10septembertrafficcamerasdataset.xlsx', sheet_name = 'Seasonally adjusted')

# 2. Clean for use

df = df[3:192]                                 # Ignore non-data related first few rows
df = df.replace({'*':0, '#':0}).to_numpy()     # Clean up data from unnecessary strings

days = df[:,0]                                 # In Unix Time - need some formatting for plotting

index = np.arange(0, 36, 6)                    # Step to separate different locations
Locations = np.zeros((7, 189, 6))
for j, i in enumerate(index):
    Locations[j, :, :] = df[:,i+1 : i+7]

London = Locations[0]                          # Explicit Separation
London = London[len([i for i in London[:,0] if float(i) == 0.0]):-1]

North_East = Locations[1]
North_East = North_East[len([i for i in North_East[:,0] if float(i) == 0.0]):-1]

Durham = Locations[2]
Durham = Durham[len([i for i in Durham[:,0] if float(i) == 0.0]):-1]

Northern_Ireland = Locations[3]
Northern_Ireland = Northern_Ireland[len([i for i in Northern_Ireland[:,0] if float(i) == 0.0]):-1]

Southend = Locations[4]
Southend = Southend[len([i for i in Southend[:,0] if float(i) == 0.0]):-1]

Greater_Manchester = Locations[5]
# Greater_Manchester_dates = days[len([i for i in Greater_Manchester[:,0] if float(i) == 0.0]):-1]              # Not necessary - function takes care of dates automatically.
Greater_Manchester = Greater_Manchester[len([i for i in Greater_Manchester[:,0] if float(i) == 0.0]):-1]

Reading = Locations[6]
Reading = Reading[len([i for i in Reading[:,0] if float(i) == 0.0]):-1]

# 3. Initial Visualisation Plots for Deliveries

# Vans and Trucks in London
# Fig1 = plt.figure()
# x = md.DateFormatter('%Y-%m-%d')
# ax = plt.gca()
# ax.xaxis.set_major_formatter(x)
# plt.plot(days[0:len(London[:,0])], London[:,3], color = 'black')                # Trucks
# plt.plot(days[0:len(London[:,0])], London[:,4], color = 'orange')               # Vans
# plt.fill_between(days[22:70], y1 = 0, y2 = max(max(London[:,3]), max(London[:,4])), facecolor = 'lightblue')      # Lockdown dates: 23rd March (Stay at Home) - 10th of May (Stay Alert)

def plotting_trucks_and_vans(town_name):

    Fig = plt.figure()
    x = md.DateFormatter('%Y-%m-%d')
    ax = plt.gca()
    ax.xaxis.set_major_formatter(x)
    plt.plot(days[len(days)-len(town_name[:,0])-1:-1], town_name[:,3], color = 'black')                # Trucks
    plt.plot(days[len(days)-len(town_name[:,0])-1:-1], town_name[:,4], color = 'orange')               # Vans
    plt.fill_between(days[22:71], y1 = 0, y2 = max(max(town_name[:,3]), max(town_name[:,4])), facecolor = 'lightblue')      # Lockdown dates: 23rd March (Stay at Home) - 10th of May (Stay Alert)

    return Fig

def plotting_cars_and_buses(town_name):

    Fig = plt.figure()
    x = md.DateFormatter('%Y-%m-%d')
    ax = plt.gca()
    ax.xaxis.set_major_formatter(x)
    plt.plot(days[len(days)-len(town_name[:,0])-1:-1], town_name[:,0], color = 'black')                # Cars
    plt.plot(days[len(days)-len(town_name[:,0])-1:-1], town_name[:,2], color = 'orange')               # Buses
    plt.fill_between(days[22:71], y1 = 0, y2 = max(max(town_name[:,0]), max(town_name[:,2])), facecolor = 'lightblue')      # Lockdown dates: 23rd March (Stay at Home) - 10th of May (Stay Alert)

    return Fig

plotting_trucks_and_vans(Greater_Manchester)
plt.title("Traffic Camera - Trucks and Vans in Greater_Manchester")

plotting_cars_and_buses(Greater_Manchester)
plt.title("Traffic Camera - Cars and Buses in Greater_Manchester")

# 4. Examining the Percentage Change during Lockdowns;

# Calculate percentage change during lockdown?
# Entry 22 signifies 23rd of March
# Entry 70 signifies 10th of May
# But not for every Area in the same way - Because of eliminating terms not relevant.

p_change_trucks_during_lockdown = (London[70,3] - London[22,3])/London[70,3]
p_change_vans_during_lockdown = (London[70,4] - London[22,4])/London[70,4]
# np.where(Greater_Manchester_dates == datetime.datetime(2020, 3, 23, 0, 0))

# for index, i in enumerate(Greater_Manchester_dates):
#    print(index, i)
#    if i == datetime.datetime(2020, 3, 23, 0, 0):
#        print(index)

def p_change_during_stay_home(town_name):
    """

    :param town_name:
    :return:
    """

    stay_home_index = np.where(days[len(days)-len(town_name[:,0])-1:-1] == datetime.datetime(2020, 3, 23, 0, 0))[0]                 # This line looks at dates applicable to each town input
    stay_alert_index = np.where(days[len(days)-len(town_name[:,0])-1:-1] == datetime.datetime(2020, 5, 10, 0, 0))[0][0]                # Then proceeds to find the index for the

    if stay_home_index.size == 0:                                                                                                   # If empty - means Data not available at specified Lockdown Date.
        stay_home_index = 0
        print("Data not available from the beginning of the first lockdown, first date available used as lower bound")
    else:
        stay_home_index = stay_home_index[0]

    p_change_trucks_during_lockdown = (town_name[stay_alert_index,3] - town_name[stay_home_index,3])/town_name[stay_home_index,3]   # Trucks
    p_change_vans_during_lockdown = (town_name[stay_alert_index,4] - town_name[stay_home_index,4])/town_name[stay_home_index,4]     # Vans
    p_change_cars_during_lockdown = (town_name[stay_alert_index,0] - town_name[stay_home_index,0])/town_name[stay_home_index,0]     # Cars
    p_change_buses_during_lockdown = (town_name[stay_alert_index,2] - town_name[stay_home_index,2])/town_name[stay_home_index,2]    # Buses

    p_changes = [p_change_trucks_during_lockdown, p_change_vans_during_lockdown, p_change_cars_during_lockdown, p_change_buses_during_lockdown]

    plt.bar(x = ['Trucks', 'Vans', 'Cars', 'Buses'], height = p_changes)
    plt.ylim([-1,1])

    return p_changes

Manc_Lock1 = p_change_during_stay_home(Greater_Manchester)

def p_change_before_stay_home(town_name):
    """

    :param town_name:
    :return:
    """

    stay_home_index = np.where(days[len(days)-len(town_name[:,0])-1:-1] == datetime.datetime(2020, 3, 16, 0, 0))[0]                 # This line looks at dates applicable to each town input
    stay_alert_index = np.where(days[len(days)-len(town_name[:,0])-1:-1] == datetime.datetime(2020, 5, 10, 0, 0))[0][0]                # Then proceeds to find the index for the

    print(stay_home_index, stay_alert_index)

    if stay_home_index.size == 0:                                                                                                   # If empty - means Data not available at specified Lockdown Date.
        stay_home_index = 0
        print("Data not available from before the beginning of the first lockdown, this plot will be the same as p_change_during_stay_home")
    else:
        stay_home_index = stay_home_index[0]

    p_change_trucks_during_lockdown = (town_name[stay_alert_index,3] - town_name[stay_home_index,3])/town_name[stay_home_index,3]   # Trucks
    p_change_vans_during_lockdown = (town_name[stay_alert_index,4] - town_name[stay_home_index,4])/town_name[stay_home_index,4]     # Vans
    p_change_cars_during_lockdown = (town_name[stay_alert_index,0] - town_name[stay_home_index,0])/town_name[stay_home_index,0]     # Cars
    p_change_buses_during_lockdown = (town_name[stay_alert_index,2] - town_name[stay_home_index,2])/town_name[stay_home_index,2]    # Buses

    p_changes = [p_change_trucks_during_lockdown, p_change_vans_during_lockdown, p_change_cars_during_lockdown, p_change_buses_during_lockdown]

    plt.bar(x = ['Trucks', 'Vans', 'Cars', 'Buses'], height = p_changes)
    plt.ylim([-1,1])

    return p_changes

p_change_before_stay_home(London)
plt.title("Percentage change Before Stay at Home - London")

def p_change_during_2nd_lockdown(town_name):
    """
    Considering Data a week prior 2nd Lockdown Announcement and Data when Stay Alert Announcement.
    31 July 2020 announcement - today
    :param town_name:
    :return:
    """

    secnd_lockdown_index = np.where(days[len(days)-len(town_name[:,0])-1:-1] == datetime.datetime(2020, 7, 31, 0, 0))[0][0]                 # This line looks at dates applicable to each town input

    p_change_trucks_during_lockdown = (town_name[-1,3] - town_name[secnd_lockdown_index,3])/town_name[secnd_lockdown_index,3]   # Trucks
    p_change_vans_during_lockdown = (town_name[-1,4] - town_name[secnd_lockdown_index,4])/town_name[secnd_lockdown_index,4]     # Vans
    p_change_cars_during_lockdown = (town_name[-1,0] - town_name[secnd_lockdown_index,0])/town_name[secnd_lockdown_index,0]     # Cars
    p_change_buses_during_lockdown = (town_name[-1,2] - town_name[secnd_lockdown_index,2])/town_name[secnd_lockdown_index,2]    # Buses

    p_changes = [p_change_trucks_during_lockdown, p_change_vans_during_lockdown, p_change_cars_during_lockdown, p_change_buses_during_lockdown]

    plt.bar(x = ['Trucks', 'Vans', 'Cars', 'Buses'], height = p_changes)
    plt.ylim([-1,1])

    return p_changes

Manc_Lock2 = p_change_during_2nd_lockdown(Greater_Manchester)
plt.title("Percentage change during 2nd Lockdown - Greater Manchester")
plt.show()

p_change_during_2nd_lockdown(North_East)
plt.title("Percentage change during 2nd Lockdown - North East")
plt.show()

# Focus on Manchester

Fig, ax = plt.subplots(ncols = 2, nrows = 1, sharey = True)
ax[0].set(title = "Manchester 1st Lockdown", ylim = [-1,1])
ax[1].set(title = "Manchester 2nd Lockdown")
ax[0].bar(x = ['Trucks', 'Vans', 'Cars', 'Buses'], height = Manc_Lock1)
ax[1].bar(x = ['Trucks', 'Vans', 'Cars', 'Buses'], height = Manc_Lock2)

# - - - - - - - - - - - - - - - - - - - - - - -
# 1. Collect Online Job Posting Data

df = pd.read_excel(r'data/10septembertrafficcamerasdataset.xlsx', sheet_name = 'Seasonally adjusted')

