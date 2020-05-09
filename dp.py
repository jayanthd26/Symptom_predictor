# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df=pd.read_csv('dataset.csv')
df=df.iloc[:,:-1]
df_i=df.copy()

v=1
label_dict={}
for i in df.columns:
    df[i]=df[i].replace([0,1],['nan',i])
    df_i[i]=df_i[i].replace([0,1],['nan',v])
    label_dict.update({v:i})
    v=v+1
    
dl=df.values.tolist()
dl_i=df_i.values.tolist()

di=[]
di_i=[]

for i in range(len(dl)):
    row=[j for j in dl[i] if j !='nan']
    row_i=[j for j in dl_i[i] if j !='nan']
    di.append(row)
    di_i.append(row_i)

with open('symps.csv', 'w') as file:
    file.writelines(','.join(str(j) for j in i) + '"\n"' for i in di_i)
with open('symps_txt.csv', 'w') as file:
    file.writelines(','.join(str(j) for j in i) + '\n' for i in di)
    
dataitems=pd.read_csv('symps.csv')