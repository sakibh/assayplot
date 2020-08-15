import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import datetime
import time

# Selecting columns with absorbance data
columns = [0,2,3,4,5,6,7,8,9,10,11,12,13]

filepath = 'data/pnppassayrawdata/'

# Read Raw Data
df = pd.read_csv(filepath, 
    header=2,
    usecols=columns, 
    skip_blank_lines=True)

# Remove all NaN rows only
df_2 = df[df['2'].notna()]
df_2.columns = [0,1,2,3,4,5,6,7,8,9,10,11,12]
df_2.index = range(len(df_2))

'''
Subtract Row D1-11 from A, B, C 1-11
Subtract ligand concentration from experimental conditions
Grabs the columns and rows from df_2
The for loop subtracts every 4th row from the last three rows and appends to the list
The list contains many dataframes that get concatenated to one dataframe
Note: This may be very inefficient on much larger datasets and utilizing numpy arrays may be the way to go.
'''

df_sub = df_2.iloc[:, 1:13]

data=[]

k = 3
n = 0
for i in range(0, len(df_sub)):
    if k <= len(df_sub):
        data.append(df_sub[n:k] - df_sub.iloc[k])
        k += 4
        n += 4

# Combine multiple dataframes
df_sub = pd.concat(data)

# Calculate the mean
df_mean = df_sub.groupby(df_sub.index // 4).mean()

# Remove all rows except fourth row (Negative Control)
df_5 = df_2[df_2.index % 4 == 3]

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
line_colors = ['#03045e', '#023e8a', '#0077b6', '#0096c7', '#00b4d8', '#48cae4', '#90e0ef', '#ade8f4', '#caf0f8', '#D6EAF8', '#EBF5FB', 'yellow']

# Plot DataFrame
plt.style.use("cyberpunk")
for i in df_mean.columns:
    # plt.plot(seconds, df_4[i], marker='o', label=compound_conc[i-1], color=line_colors[i-1])
    plt.plot(seconds, df_mean[i], marker='o', label=compound_conc[i-1], color=line_colors[i-1])
plt.plot(seconds, df_5[1], marker='o', label='-Control (No Prot)', color='red')

plt.legend()
plt.title('Compound in 5% DMSO')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Absorbance (405 nm)', fontsize=12)
mplcyberpunk.make_lines_glow()
plt.show()