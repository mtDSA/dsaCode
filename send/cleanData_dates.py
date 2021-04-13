#remove all columns except for age, job, maritial, education, housing, loan, pday, previous, poutcome


import pandas as pd
import matplotlib.pyplot as plt
import datetime
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split


df = pd.read_csv('DSA_data.csv')

df = pd.read_csv('data_dates.csv')


#df = df.drop_duplicates()           #remove duplicates


#create a row thats a unique number for each day
date = zip(df['day_of_week'], df['month'])

day_list = []
last_day = 'mon'
total_days = 1
last_month = 'may'

for day, month in date:
    if day != last_day or last_month != month:
        total_days = total_days+1

    last_day=day
    last_month=month

    day_list.append(total_days)

df['day'] = day_list
print(day_list)

'''
#hot encode columns of strings into columns of bools
job = pd.get_dummies(df.job, prefix='job')

marital = pd.get_dummies(df.marital, prefix='marital')

edu = pd.get_dummies(df.education, prefix='edu')

default = pd.get_dummies(df.default, prefix='default')
default = default.drop('default_no', 1)     #drop redundant 'no' column

house = pd.get_dummies(df.housing, prefix='house')
house = house.drop('house_no', 1)           #drop redundant 'no' column

loan = pd.get_dummies(df.loan, prefix='loan')
loan = loan.drop('loan_no', 1)              #drop redundant 'no' column

df = pd.concat([ df['day'], df['euribor3m'], df['age'], job, marital, edu, default, house, loan, df['ModelPrediction'], df['y']], axis=1)
'''

loan = pd.get_dummies(df.y, prefix='y')
loan = loan.drop('y_no', 1)              #drop redundant 'no' column
df['y'] = loan

#print(df[['month', 'day_of_week', 'day']])
df.to_csv('DSA_days_dates.csv', index=False)


print(df.head)





'''
df = df.drop(df.columns[list(range(7, 11, 1)) + list(range(15, 19, 1))], axis=1)


print(df)

'''
