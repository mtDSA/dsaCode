import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
import matplotlib.ticker as mtick


df = pd.read_csv('DSA_days_dates.csv')

df = df[[ 'euribor3m', 'cons.conf.idx', 'emp.var.rate', 'nr.employed', 'day' ]]

#df = df[['nr.employed', 'day']]
'''
fig, ax = plt.subplots()
for col in df:
    if col != 'day':
        df[col] = df[col]/df[col][0]
        ax.scatter(df['day'], df[col], label=col)
        ax.legend()

'''

print(df[df.columns[1]])



#PLOTTING
ncols = 3
nrows = 3
fig=plt.figure()
gs1 = gridspec.GridSpec(2, 2)           #set the number of subplots
gs1.update(wspace=0.25, hspace=0.25)          # set the spacing between axes.

for i in range(4):    #i sets order of the fit
        ax = plt.subplot(gs1[i])
        #ax.bar(bin_array-step/2, count_array, color='b', alpha=0.25, width=step)        #bar graph of counts in each bin
        ax.scatter(df['day'], df[df.columns[i]], color='k', s=3)                                                        #points
        plt.xticks(np.arange(0, df['day'].max(), 50))
        plt.grid()
        if i==0:
            ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))

        ax.set_title(df.columns[i], x=.8, y=.8, fontsize=18)
        plt.xlabel('Day (May 2008 - Nov 2010)')
fig.tight_layout()

fig.suptitle('Social and Economic Attributes', y=.95, fontsize=30)


plt.show()




