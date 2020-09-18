# The Data displays the relative energy performance of UK central government buildings for the selected period.
# The data driving this is taken from building utility meters, either half-hourly or daily.
# Performance is shown per square metre or per occupant depending on which 'Analyse By' button is selected.

# - - - - - -
# 1. Shall focus on the Home Office Generation of its Headquarters with comparison to 2019 Data;
# The site contains 800,000 sq ft (74,000 m2) of office space.

# NOTE:
# The most commonly accepted rule in London is that 100 sq.ft. per employee is the ideal amount of space per person. This allows for roughly 50 sq ft for desk space and another 50 sq ft to accommodate room in communal areas, like breakout spaces, meeting rooms and kitchens.
# Hence capacity should be roughly 8,000 employees.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import seaborn as sns
import datetime

sns.set_style('whitegrid')

March_Data = pd.read_excel(r'data/HomeOfficeGeneration.xlsx', sheet_name = 'March')
April_Data = pd.read_excel(r'data/HomeOfficeGeneration.xlsx', sheet_name = 'April')
May_Data = pd.read_excel(r'data/HomeOfficeGeneration.xlsx', sheet_name = 'May')
#June_Data = pd.read_excel(r'data/HomeOfficeGeneration.xlsx', sheet_name = 'June')

# Question: in 'normal times' what is the average energy produced per day across a month?
# Using 2019 data this point can be proved

# Clean up March 2019 Data

March_19_Data = March_Data[20:]
Time = March_Data[1:2].to_numpy()[0][5:]
labels = March_Data[1:2].values.tolist()
March_19_Data.columns = labels

# Visualising March 2019 Data

HQ_Electr_March_2019 = March_19_Data[31:].to_numpy()
Date = HQ_Electr_March_2019[:,4]

x = March_Data[1:2].values[0][5:].tolist()
# For the first day of March Date[0]
x_dt = [datetime.datetime.combine(Date[0], t) for t in x]

x = md.DateFormatter('%H:%M:%S')
ax = plt.gca()
ax.xaxis.set_major_formatter(x)
plt.plot(x_dt, HQ_Electr_March_2019[0,5:])

# Plot any chosen day histogram;

def plot_generation_of_any_chosen_day_2019(day_chosen):
    """

    :param day_chosen: this is an integer 1..31
    :return: Fig
    """

    x = March_Data[1:2].values[0][5:].tolist()
    x_dt = [datetime.datetime.combine(Date[day_chosen], t) for t in x]
    x = md.DateFormatter('%H:%M:%S')
    ax = plt.gca()
    ax.xaxis.set_major_formatter(x)
    plt.plot(x_dt, HQ_Electr_March_2019[day_chosen,5:])

    return

plot_generation_of_any_chosen_day_2019(2)
plt.title("Energy Generation in the HQ Home Office on 2nd of the Month")

plot_generation_of_any_chosen_day_2019(15)
plt.title("Energy Generation in the HQ Home Office on 15th of the Month")

Fig = plt.figure()
for i in range(31):
    plot_generation_of_any_chosen_day_2019(i)
plt.title("Energy Generation in the HQ Home Office in 2019 for the whole of March")
plt.show()

# Question: What happened in the main HQ Building in terms of Energy Generation around Covid Time?
# Using 2020 data this point can be proved

# Clean up March 2020 Data

March_20_Data = March_Data[:20]
March_20_Data.columns = labels

HQ_Electr_March_2020 = March_20_Data[2:10].to_numpy()

def plot_generation_of_any_chosen_day_march(day_chosen, year_chosen):
    """
    :param day_chosen: this is an integer 1..31
    :return:
    """
                                                                            # Date in a List
    x = March_Data[1:2].values[0][5:].tolist()                              # Hours in a List
    x_dt = [datetime.datetime.combine(Date[day_chosen], t) for t in x]      # Function to combine Date and Hour
    x = md.DateFormatter('%H:%M:%S')                                        # Necessary to Plot datetime.datetime format
    ax = plt.gca()
    ax.xaxis.set_major_formatter(x)

    if year_chosen == 2019:
        plt.plot(x_dt, HQ_Electr_March_2019[day_chosen,5:])
    elif year_chosen == 2020:
        plt.plot(x_dt, HQ_Electr_March_2020[day_chosen,5:])
    else:
        print("Oops - date not valid: it's either 2019 or 2020 (integer)")

    return

Fig = plt.figure()
for i in range(31):
    plot_generation_of_any_chosen_day_march(i, 2019)
plt.title("Energy Generation in the HQ Home Office in 2019 for the whole of March")
plt.show()

# In terms of GHG how much CO2 was produced during a 'normal' month?
# Carbon Factors and Cost
# Fuel	kgCO2e per unit
# Electricity (kWh)	0.537

# Again taking 2019 Data

kgCO2e = 0.547*HQ_Electr_March_2019[0,5:]
plt.plot(x_dt, kgCO2e)

# Bringing Everything Together;
# BEFORE COVID

fig, ax1 = plt.subplots()
ax1.set(title = "Energy Generated from an Office (800,000 sq ft) in a Sample Day Before Covid", ylim = [0, max(HQ_Electr_March_2019[0,5:]) + 100])

color = 'tab:red'
ax1.set_xlabel('month-day hour')
ax1.set_ylabel('kWh of Energy Generated', color=color)
ax1.plot(x_dt, HQ_Electr_March_2019[0,5:], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('kgCO2 Emissions from Energy Generated', color = color)  # we already handled the x-label with ax1
ax2.plot(x_dt, 0.547*HQ_Electr_March_2019[0,5:], color = color)
# ax2.fill_between(x = x_dt, y1 = 0.547*HQ_Electr_March_2019[0,5:], color = color, alpha = 0.30)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

# AFTER COVID

fig, ax1 = plt.subplots()
ax1.set(title = "Energy Generated from an Office (800,000 sq ft) in a Sample Day During Covid", ylim = [0, max(HQ_Electr_March_2020[0,5:]) + 100])

color = 'tab:red'
ax1.set_xlabel('month-day hour')
ax1.set_ylabel('kWh of Energy Generated', color=color)
ax1.plot(x_dt, HQ_Electr_March_2020[0,5:], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('kgCO2 Emissions from Energy Generated', color = color)  # we already handled the x-label with ax1
ax2.plot(x_dt, 0.547*HQ_Electr_March_2020[0,5:], color= color)
# ax2.fill_between(x = x_dt, y1 = 0.547*HQ_Electr_March_2019[0,5:], color = color, alpha = 0.30)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

def comparison_plot_with_emissions_of_any_chosen_date_march(day_chosen, year_chosen):
    """
    :param day_chosen: this is an integer n = 1, 2 ... 31 to stand for the day of the month.
    :param year_chosen: this is an integer 2019 or 2020 to give the choice to call upon any one of those datasets.
    :return: plot
    """

    fig, ax1 = plt.subplots()
    ax1.set(title = "Energy Generated from an Office (800,000 sq ft) in a Sample Day During Covid", ylim = [0, max(HQ_Electr_March_2020[0,5:]) + 100])

    color = 'tab:red'
    ax1.set_xlabel('month-day hour')
    ax1.set_ylabel('kWh of Energy Generated', color=color)
    if year_chosen == 2020:
        ax1.plot(x_dt, HQ_Electr_March_2020[day_chosen,5:], color=color)
    elif year_chosen == 2019:
        ax1.plot(x_dt, HQ_Electr_March_2019[day_chosen,5:], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('kgCO2 Emissions from Energy Generated', color = color)  # we already handled the x-label with ax1
    if year_chosen == 2020:
        ax2.plot(x_dt, 0.547*HQ_Electr_March_2020[day_chosen,5:], color= color)
    elif year_chosen == 2019:
        ax2.plot(x_dt, 0.547*HQ_Electr_March_2019[day_chosen,5:], color= color)
    # ax2.fill_between(x = x_dt, y1 = 0.547*HQ_Electr_March_2019[0,5:], color = color, alpha = 0.30)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

    return

# - - - - - - - Looking at single person consumption in the office

# In relative terms due to government law we have that the minimum office space is
# Under The Workplace (Health, Safety and Welfare) Regulations 1992, employers have a responsibility to provide a minimum work space of 40 square feet per person in an office area.

# However a more realistic average for London Seems to be around 100 sq ft - hence why such figure is used in making the subsequent calculations.

capacity_40sqft = 800000/40
capacity_100sqft = 800000/100

fig, ax1 = plt.subplots()
ax1.set(title = "Energy Generated from one individual (taking up 40 sq ft) in an office (800,000 sq ft) in a Sample Day Before Covid")

color = 'tab:red'
ax1.set_xlabel('month-day hour')
ax1.set_ylabel('kWh of Energy Generated', color=color)
ax1.plot(x_dt, HQ_Electr_March_2019[0,5:]/capacity_40sqft, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('kgCO2 Emissions from Energy Generated', color = color)  # we already handled the x-label with ax1
ax2.plot(x_dt, (0.547*HQ_Electr_March_2019[0,5:])/capacity_40sqft, color = color)
# ax2.fill_between(x = x_dt, y1 = 0.547*HQ_Electr_March_2019[0,5:], color = color, alpha = 0.30)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

# - - - - - - - - - -

fig, ax1 = plt.subplots()
ax1.set(title = "Energy Generated from one individual (taking up 100 sq ft) in an office (800,000 sq ft) in a Sample Day Before Covid")

color = 'tab:red'
ax1.set_xlabel('month-day hour')
ax1.set_ylabel('kWh of Energy Generated', color=color)
ax1.plot(x_dt, HQ_Electr_March_2019[0,5:]/capacity_100sqft, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('kgCO2 Emissions from Energy Generated', color = color)  # we already handled the x-label with ax1
ax2.plot(x_dt, (0.547*HQ_Electr_March_2019[0,5:])/capacity_100sqft, color = color)
# ax2.fill_between(x = x_dt, y1 = 0.547*HQ_Electr_March_2019[0,5:], color = color, alpha = 0.30)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

# - - - - - - - - - - - - - -
# - - - using May Data

# Clean up May 2019 Data

May_19_Data = May_Data[62:]
Time = March_Data[1:2].to_numpy()[0][5:]
labels = March_Data[1:2].values.tolist()
May_19_Data.columns = labels

# Visualising May 2019 Data

HQ_Electr_May_2019 = May_19_Data[31:].to_numpy()
Date_May = HQ_Electr_May_2019[:,4]

x = March_Data[1:2].values[0][5:].tolist()
# For the first day of May Date[0]
x_dt = [datetime.datetime.combine(Date_May[0], t) for t in x]

x = md.DateFormatter('%H:%M:%S')
ax = plt.gca()
ax.xaxis.set_major_formatter(x)
plt.plot(x_dt, HQ_Electr_May_2019[0,5:])

# - - - -

# https://www.wsp.com/en-GB/insights/office-vs-home-working-how-we-can-save-our-carbon-footprint

# https://www.ofgem.gov.uk/gas/retail-market/monitoring-data-and-statistics/typical-domestic-consumption-values
# TDCVs Typical Domestic Consumption Values
#
# https://uk.finance.yahoo.com/news/working-from-home-could-cost-uk-employees-52-m-more-a-week-on-energy-bills-000140655.html
# Expected % increase:
# People working from home will use 25% more electricity and 17% more gas per day than households where people are out at work all day, according to the research by comparison and switching service Uswitch.com.
# Can our analysis reflect that?

# Typical/Average Pre-Covid consumption of Energy in hours
# https://www.ukpower.co.uk/home_energy/average-household-gas-and-electricity-usage
# For an Electricity Profile Class 1 of an average household.
consumption_rate_low = 1,800        #kWh per day
consumption_rate_medium = 2,900     #kWh per day
consumption_rate_high = 4,300       #kWh per day

# Typical/Average Pre-Covid consumption of Energy per m2
# https://www.ukpower.co.uk/home_energy/average-energy-bill
# An average flat size is approx 80 m2
consumption_of_energy_m2 = 25       #kWh per m2
# m2 in sq ft: 1 m2 is 10.7639 sq ft
consumption_of_energy_sqft = consumption_of_energy_m2*10.7639           # kWh per sq ft
# flat size in ft

# https://www.cse.org.uk/advice/advice-and-support/how-much-electricity-am-i-using
# Energy by appliance - Dataset Household Appliances Average Power Ratings;
# Can we estimate what appliances - work related will be used more and calculate in terms of hours?
appliances_consumption = pd.read_excel(r'data/Household Appliances Average Power Ratings.xlsx')

# Assumption in terms of appliances used more -

# Smart phone charge
# Tablet charge
# Broadband router
# Laptop
# Desktop Computer
# Microwave
# Toaster
# Kettle

# Include conversion to kWh and make it weekly ie 9 h per day * 5-day working week

phone_charge_weekly_avg_power_rating_kWh = appliances_consumption[appliances_consumption['Appliance '] == 'Smart phone (charge)']['Average power rating (Watts)'].values[0]*0.0001*9*5
tablet_charge_weekly_avg_power_rating_kWh = appliances_consumption[appliances_consumption['Appliance '] == 'Tablet (charge)']['Average power rating (Watts)'].values[0]*0.0001*9*5
broadband_router_weekly_avg_power_rating_kWh = appliances_consumption[appliances_consumption['Appliance '] == 'Broadband router']['Average power rating (Watts)'].values[0]*0.0001*9*5
laptop_weekly_avg_power_rating_kWh = appliances_consumption[appliances_consumption['Appliance '] == 'Laptop']['Average power rating (Watts)'].values[0]*0.0001*9*5
desktop_computer_weekly_avg_power_rating_kWh = appliances_consumption[appliances_consumption['Appliance '] == 'Desktop computer']['Average power rating (Watts)'].values[0]*0.0001*9*5
microwave_weekly_avg_power_rating_kWh = appliances_consumption[appliances_consumption['Appliance '] == 'Microwave']['Average power rating (Watts)'].values[0]*0.0001*0.25*5
kettle_weekly_avg_power_rating_kWh = appliances_consumption[appliances_consumption['Appliance '] == 'Kettle']['Average power rating (Watts)'].values[0]*0.0001*0.25*5

# Note kettle and microwave only assumed to be used for max of 15 minutes during each working day.

# Now include heating up the home with electrical heating
# https://www.greenmatch.co.uk/green-energy/central-heating-capacity
# https://www.vivintsolar.com/blog/how-much-electricity-does-a-space-heater-use
# Space Heater stats on average
# 1,500 W x 9 hours

heating_weekly_avg_power_rating_kWh = 1.5*9*5

# Combining Data;

weekly_avg_power_rating_increase = np.array((phone_charge_weekly_avg_power_rating_kWh, tablet_charge_weekly_avg_power_rating_kWh,
                                    broadband_router_weekly_avg_power_rating_kWh, laptop_weekly_avg_power_rating_kWh,
                                    desktop_computer_weekly_avg_power_rating_kWh, microwave_weekly_avg_power_rating_kWh,
                                    kettle_weekly_avg_power_rating_kWh, heating_weekly_avg_power_rating_kWh))

plt.bar(x = ['Phone', 'Tablet', 'Broadband', 'Laptop', 'Desktop', 'Microwave', 'Kettle'], height = weekly_avg_power_rating_increase[0:7])

# Stacked Bar

Label = ['Phone', 'Tablet', 'Broadband', 'Laptop', 'Desktop', 'Microwave', 'Kettle', 'Heating']
plt.bar(x = "Appliances Consumption", height = weekly_avg_power_rating_increase[0], width = 0.75)
bottom_bar = weekly_avg_power_rating_increase[0]
for i in range(1, 7):
    plt.bar(x = "Appliances Consumption", height = weekly_avg_power_rating_increase[i], bottom = bottom_bar, width = 0.75)
    bottom_bar = bottom_bar + weekly_avg_power_rating_increase[i]
plt.bar(x = "Heating Consumption", height = weekly_avg_power_rating_increase[7])

plt.legend(labels = (Label[0], Label[1], Label[2], Label[3], Label[4], Label[5], Label[6], Label[7]), fancybox = True)

plt.title("Appliances Consumption in kWh over a working week (9 hours and 5 days)")
#plt.xticks(0, Label, fontweight='bold')

## -- subplots instead

# Assumption: a workday is 9 hour long, a 5 working week and there are 48 working weeks per year.
# For which it is necessary to have a desktop, and other small power equipment.

fig, ax = plt.subplots(ncols = 3, figsize = (14, 10))
Label = ['Phone', 'Tablet', 'Broadband', 'Laptop', 'Desktop', 'Microwave', 'Kettle', 'Heating']
ax[0].bar(x = "Appliances Consumption", height = weekly_avg_power_rating_increase[0], width = 0.75)
bottom_bar = weekly_avg_power_rating_increase[0]
for i in range(1, 7):
    ax[0].bar(x = "Appliances Consumption", height = weekly_avg_power_rating_increase[i], bottom = bottom_bar, width = 0.75)
    bottom_bar = bottom_bar + weekly_avg_power_rating_increase[i]
    ax[0].legend(labels = (Label[0], Label[1], Label[2], Label[3], Label[4], Label[5], Label[6]), fancybox = True)

ax[1].bar(x = "Heating Consumption", height = weekly_avg_power_rating_increase[7])

ax[0].set(title = "Appliances Consumption in kWh over a working week", ylabel = "Energy in kWh")
ax[1].set(title = "Heating Consumption in kWh over a working week", ylabel = "Energy in kWh")

ax[2].set(title = "Total Consumption in kWh over a working week", ylabel = "Energy in kWh")
ax[2].bar(x = "Appliances Consumption", height = weekly_avg_power_rating_increase[0], width = 0.75)
bottom_bar = weekly_avg_power_rating_increase[0]
for i in range(1, 8):
    ax[2].bar(x = "Appliances Consumption", height = weekly_avg_power_rating_increase[i], bottom = bottom_bar, width = 0.75)
    bottom_bar = bottom_bar + weekly_avg_power_rating_increase[i]
    ax[2].legend(labels = (Label[0], Label[1], Label[2], Label[3], Label[4], Label[5], Label[6], Label[7]), fancybox = True)

# What are new consumption_rate low medium and high for a working from home household?




