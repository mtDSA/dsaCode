#logistic regression just on demographic info
#one model for pre-crash, one model for post-crash

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils import resample


df = pd.read_csv('cleanData_dayss.csv')

mp = df[['day', 'ModelPrediction', 'y']]   
df = df.drop(['emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed', 'ModelPrediction'], 1)

#before crash (day<83) after crash (day>119)
df = df[df['day']>119]
mp = mp[mp['day']>119]

mp['bi'] = [0 if i>.75 else 1 for i in mp['ModelPrediction']]   #values of mp<.75 are predicted to be sles (as informed y the 'Time for 100 Sales' plot

print(mp)

x_og = df.iloc[:, :-1]
y_og = df['y']

# Upsample sales and combine with failures
df_majority = df[df['y']==0]
df_minority = df[df['y']==1]
df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority.index), random_state=123)
df_up = pd.concat([df_majority, df_minority_upsampled])

#break up test and training sets
x_up = df_up.iloc[:, :-1]
y_up = df_up['y']          


x_train, x_test, y_train, y_test = train_test_split(x_up, y_up, test_size=0.25)

#train model
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x_train, y_train)

'''
#run model over test data
y_pred = model.predict(x_test)

#confusion matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

print('tn=',tn,' fp=',fp, ' fn=',fn, ' tp=',tp)
'''

#run model over all data
y_pred = model.predict(x_og)

#confusion matrix
tn, fp, fn, tp = confusion_matrix(y_og, y_pred).ravel()

print('tn=',tn,' fp=',fp, ' fn=',fn, ' tp=',tp)


#confusion matrix
tn, fp, fn, tp = confusion_matrix(mp['y'], mp['bi']).ravel()

print('tn=',tn,' fp=',fp, ' fn=',fn, ' tp=',tp)
