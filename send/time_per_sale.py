import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('DSA_data.csv')
df = df.drop_duplicates()               #remove duplicates
df = df.sort_values('ModelPrediction')  #sort rows by model prediction


thing = zip(df['duration'], df['campaign'], df['y'], df['ModelPrediction']) #create a list for each client 

count = 0
time = 0
calls = 0
people = 0
mp = 0
totals = []

for i in thing:

    time = time + i[0]      #sum time to get 100 sales
    calls = calls + i[1]     #sum calls made to get 100 sales
    people = people + 1     #sum people called made to get 100 sales
    mp = mp + i[3]
    if i[2] == 'yes':
        count = count+1     #count to 100 sales

    if count == 100:
        totals.append([40*round(time/3600, 1), calls, people, mp/people])
        count = 0
        time = 0
        calls = 0
        people = 0
        mp = 0

results = pd.DataFrame(totals, columns=['time', 'calls', 'people', 'average_mp'])

print(results)

#PLOTTING
import matplotlib.pyplot as plt

x = 'average_mp'
y = 'time'
#y = 'duration'
#y = 'emp.var.rate'
#y = 'nr.employed'
#x = 'ModelPrediction'
fig, ax = plt.subplots()

plt.scatter(results[x], results[y], color='b', s=25)  
#plt.scatter(df_yes[x],df_yes[y], color='r', s=4)    #calls that succeeded

#ax2 = ax1.twinx()


plt.title('Cost to Make 100 Sales', size=25 )
plt.xticks(rotation = 45)
plt.xlabel('Model Prediction', size=20)
plt.ylabel('Cost (USD)', size=20)

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

plt.grid()
plt.gcf().subplots_adjust(bottom=0.15)

plt.savefig('time100sales.png')

plt.show()


