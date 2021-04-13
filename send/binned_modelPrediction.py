import numpy as np; np.random.seed(0)
import matplotlib.pyplot as plt
import pandas as pd

n = 15 #number of bins

#df = pd.read_csv('DSA_data.csv')
df = pd.read_csv('DSA_days_dates.csv')
'''
day_dict = dict(zip(df['day'], df['dates']))
print(day_dict)
'''

#df = df[ df['euribor3m']<3 ]       #check the data for high Euribor values
#df = df[ df['pdays'] ==999 ]        #check only success rate of first calls, if Eurior is a good indicator than the success rate should be higher at lower euribor values


col = 'ModelPrediction'
#col = 'euribor3m'
#col = 'day'

#df_yes = df[df['y'] == 1][col]    #predictions of the model for sucesses
#df = df[col]                          #predictions of the model for all
#print(df_yes)
df_yes = 1-df[df['y'] == 1][col]    #predictions of '1 minus the model' for sucesses
df = 1-df[col]                          #predictions of '1 minus the model' for all



df_L = 0#round(df.min(), 2)     #lowest model prediction
df_H = .75#round(df.max(), 2)     #highest model prediction
bin_size = (df_H-df_L)/n   #10 bins
bins = np.around(np.arange(df_L, df_H+bin_size, bin_size), decimals=3) #list for bin spacing

#PLOTTING
fig, ax = plt.subplots(figsize=(16, 10))
ax.set(xticks=bins)
ax.hist(df.values, bins=bins, edgecolor="k")        #bar of people called
ax.hist(df_yes.values, bins=bins, edgecolor="r")    #bar of success


#make list of hights of each bar
heights = [bar.get_height() for bar in ax.patches]
heights_ratio = [i/j for i, j in zip(heights[n:], heights[:n])]
heights = heights[:n]

print(sum(heights[n:]))
print(sum(heights[:n]))


#for loops to add number to each bar, total and ration of success to total
for rect in ax.patches[:n]:
    height = rect.get_height()
    ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height), 
                xytext=(0, 7), textcoords='offset points', ha='center', va='bottom')

for rect in ax.patches[n:]:
    height = heights_ratio[ax.patches[n:].index(rect)]
    ax.annotate(f'{round(height,2)}', xy=(rect.get_x()+rect.get_width()/2, height),
                xytext=(0, -2), textcoords='offset points', ha='center', va='bottom')


if col == 'day':
    bins = [ day_dict[int(round(i))] for i in bins  ]

ax.set_xticklabels(bins)#, rotation=40)
ax.set_title('\'1-Model Prediction\' Distribution', size = 25)
ax.set_xlabel(str(col).capitalize(), size=20)
ax.set_ylabel('Clients', size=20)
ax.legend(('Clients Called', 'Successful Sales'), loc='upper right', prop={'size': 20})
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('test.png')
plt.show()

