import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import datetime
import time

# Create a .txt to .csv conversion function
# Create case for rows E-H
# How to calculate IC50 from this data
   # - Slope of absorbance vs time
# How is this normally plotted?
# Can I see a sample plot of this protocol?




columns = [0,2,3,4,5,6,7,8,9,10,11,12,13]

# Read Raw Data
df = pd.read_csv('data/pnppassayrawdata/atw122-2.csv', 
    header=2,
    usecols=columns, 
    skip_blank_lines=True)

# Remove all NaN rows only
df_2 = df[df['2'].notna()]
df_2.columns = [0,1,2,3,4,5,6,7,8,9,10,11,12]
df_2.index = range(len(df_2))

# Remove all rows except fourth row (Negative Control)
df_5 = df_2[df_2.index % 4 == 3]
print(df_5)

# Remove every fourth and take the mean and standard deviation of the first three sets in each column
df_3 = df_2[df_2.index % 4 != 3]
df_4 = df_3.groupby(df_3.index // 4).mean()     
# print(df_3.groupby(df_3.index // 4).std())

# Get time intervals and convert to seconds
time_interval = pd.Series(df_2[0].dropna())
seconds = []
for i in time_interval:
    date_time = datetime.datetime.strptime(i, "%H:%M:%S")
    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    seconds.append(a_timedelta.total_seconds())

# Compound Concentrations
compound_conc = ['200 uM', '100 uM', '50 uM', '25 uM', '12.5 uM', '6.25 uM', '3.125 uM', '1.5625 uM', '0.78125 uM', '0.3906 uM', '0.1953 uM', '+Control (Protein)']

# Colors for Each Line
line_colors = ['cyan', 'deepskyblue', 'steelblue', 'dodgerblue', 'blue', 'navy', 'orange', 'salmon', 'red', 'maroon', 'magenta', 'yellow']

# Plot DataFrame
plt.style.use("cyberpunk")
for i in df_4.columns:
    plt.plot(seconds, df_4[i], marker='o', label=compound_conc[i-1], color=line_colors[i-1])
plt.plot(seconds, df_5[1], marker='o', label='-Control (No Prot)', color='gray')

plt.legend()
plt.title('Compound in 5% DMSO')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Absorbance (405 nm)', fontsize=12)
mplcyberpunk.make_lines_glow()
plt.show()