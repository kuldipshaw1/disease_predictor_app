import joblib
import pandas as pd
import numpy as np

import sklearn
from sys import argv
n=len(argv)
m=17-n+1
li=[0]*m
lis=argv[1:] + li
# slow=['weight gain', 'anxiety', 'cold hands and feets', 'mood swings',0,0,0,0,0,0,0,0,0,0,0,0,0]
final_model=joblib.load("final_modal.pkl")
ektra7at = pd.read_csv("symptom_precaution.csv")
df1 = pd.read_csv('Symptom-severity.csv')
df1['Symptom'] = df1['Symptom'].str.replace('_',' ')

# In[65]:


discrp = pd.read_csv("symptom_Description.csv")

# In[66]:


def predd(x,l):
    psymptoms = l
    #print(psymptoms)
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j]==a[k]:
                psymptoms[j]=b[k]
    psy = [psymptoms]
    pred2 = x.predict(psy)
    disp= discrp[discrp['Disease']==pred2[0]]
    disp = disp.values[0][1]
    recomnd = ektra7at[ektra7at['Disease']==pred2[0]]
    c=np.where(ektra7at['Disease']==pred2[0])[0][0]
    precuation_list=[]
    for i in range(1,len(ektra7at.iloc[c])):
          precuation_list.append(ektra7at.iloc[c,i])
    print("The Disease Name: ",pred2[0])
    print("The Disease Discription: ",disp)
    print("Recommended Things to do at home: ")
    for i in precuation_list:
        print(i)
predd(final_model,lis)