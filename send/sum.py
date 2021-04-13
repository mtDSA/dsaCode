import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('DSA_data.csv')

people = df.shape[0]
total_yes = df[df['y'] == 'yes'].shape[0]
total_time = df['duration'].sum()
total_calls = df['campaign'].sum()

print('total people called: ', people)

print('cumulative call time: ', total_time)

print('number of calls made: ', total_calls)
print('number of sales: ', total_yes)
print('average time per person: ', total_time/people) 
print('average call time: ', total_time/total_calls)
print('average time spent per sale: ', total_time/total_yes)

