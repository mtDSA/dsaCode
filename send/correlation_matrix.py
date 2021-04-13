import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn


#df = pd.read_csv('DSA_days_dates.csv')
#df = df[['age', 'day', 'dates', 'duration', 'euribor3m', 'nr.employed', 'cons.conf.idx', 'cons.price.idx', 'emp.var.rate', 'y', 'ModelPrediction']]


df = pd.read_csv('cleanData_dayss.csv')
df['mp_1'] = 1-df['ModelPrediction']

df = df[df['day']>175] #compare correlation at only high or love Euribor values


#dataframe for each catagory 
df_job = df[ ['y', 'ModelPrediction', 'job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired', 'job_self-employed', 'job_services', 'job_student', 'job_technician', 'job_unemployed', 'job_unknown']]

df_marital = df[['y', 'ModelPrediction', 'marital_divorced', 'marital_married', 'marital_single', 'marital_unknown']]

df_edu = df[['y', 'ModelPrediction', 'edu_illiterate', 'edu_basic.4y', 'edu_basic.6y', 'edu_basic.9y', 'edu_high.school', 'edu_professional.course', 'edu_university.degree', 'edu_unknown']]

df_other = df[['y', 'ModelPrediction', 'age', 'default_unknown', 'default_yes', 'house_unknown', 'house_yes', 'poutcome_failure', 'poutcome_success']]

df_econ = df[['y', 'ModelPrediction', 'day', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']]


#gets the column names in the form I need to put into the df_* catagories above
'''
word = ''
for col in df:
    word = word+'\''+col+'\', '
print(word)
'''


data = df_econ

mask = np.triu(np.ones_like(data.corr()))       #create mask for upper half of cor-matrix

corrMatrix = round(data.corr(), 3)

print(data)
sn.heatmap(corrMatrix, annot=True, cmap="PiYG", mask=mask, vmin=-1, vmax=1)
#plt.xticks(rotation = 45)
plt.yticks(rotation=0)
plt.title('Economic and Social Correlation Matrix (day>175)')
plt.gcf().subplots_adjust(bottom=0.25, left=.35)

plt.savefig('cor_matrix_econ_175-488.png')

plt.show()



