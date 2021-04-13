import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('DSA_data.csv')

yes = len(df[df['y']=='yes'].index)     #count the yes's
no = len(df[df['y']=='no'].index)       #and the no's

size = [yes, no]

fig1, ax1 = plt.subplots()
ax1.pie(size, labels=['Yes   \n('+str(size[0])+')' , '    No\n('+str(size[1])+')'], autopct='%1.1f%%', startangle=180, textprops={'fontsize': 20})

ax1.axis('equal')
ax1.set_title('Successes and Failures', size=30)

plt.show()

