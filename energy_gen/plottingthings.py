# Tricks and things

import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd
import seaborn as sns
import datetime

# A Few References;
# http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
# https://www.codecademy.com/articles/seaborn-design-ii

# Line Plot Example

sns.set_style('whitegrid')
palette = sns.color_palette("muted")
#sns.set() # another possible style

# Some necessary data cleaning
March_Data = pd.read_excel(r'data/HomeOfficeGeneration.xlsx', sheet_name = 'March')
March_19_Data = March_Data[20:]
Time = March_Data[1:2].to_numpy()[0][5:]
labels = March_Data[1:2].values.tolist()
March_19_Data.columns = labels
HQ_Electr_March_2019 = March_19_Data[31:].to_numpy()
Date = HQ_Electr_March_2019[:,4]
x = March_Data[1:2].values[0][5:].tolist()
x_dt = [datetime.datetime.combine(Date[0], t) for t in x]

# Size is important
Fig = plt.figure(figsize=(8, 6), dpi = 120)

# Necessary Handling of Datetime
x = md.DateFormatter('%H:%M:%S')
ax = plt.gca()
ax.xaxis.set_major_formatter(x)
plt.plot(x_dt, HQ_Electr_March_2019[0,5:])
plt.plot(x_dt, HQ_Electr_March_2019[4,5:])

# May want to remove the plot frame lines.
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# You may want the axis ticks only show up on the bottom and left of the plot.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.

plt.ylim(0, max(max(HQ_Electr_March_2019[0,5:]), max(HQ_Electr_March_2019[4,5:])) + 50) # Nifty line to use maximum value of the dataset and add a little extra space
#plt.xlim(0,100) Not necessary here

# Title the plot: can be done in different ways
plt.title("This is a Title")
plt.text(x_dt[20], 93, "This is another Title", fontsize=17, ha="center")

# Include legend for each plotted line
plt.text(x_dt[-4], 300, "This is the orange line", fontsize = 12, color = sns.color_palette("muted")[1])
plt.text(x_dt[-4], 200, "This is the blue line", fontsize = 12, color = sns.color_palette("muted")[0])

# Include acknowledgment of data source
plt.text(x_dt[1], -100, "Data source: somewhere.com"    
       "\nAuthor: Me (me.com / @me)"    
       "\nNote: Some things are missing because the historical data "    
       "is not available for them", fontsize=10)




