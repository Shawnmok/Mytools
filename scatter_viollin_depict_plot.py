#!python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import  numpy as np
import pandas as pd

tips = pd.read_csv("./t3.2.csv")
print (tips)
name="age,BMI,WHR,FBS,2hPBS,GADA_index,height,weight,waist,hip,TG,TC,HDL,LDL,HbA1c,FCP,2hCP,GADA,onset_age".split(",")
plt.subplots(3,3,figsize=(20,15))
for i in range(1,10):
   print(name[i])
   number=str('33'+str(i))
   plt.subplot(int(number))
   sns.stripplot(x='type',y=name[i],data=tips,jitter=True)
   sns.violinplot(x='type',y=name[i],data=tips,color='.8')
plt.tight_layout()
plt.show()
plt.savefig("test1"+".pdf")
plt.close()
plt.subplots(3,3,figsize=(20,15 ))
for i in range(10,19):
   print(name[i])
   number=str('33'+str(i-9))
   plt.subplot(number)
   sns.stripplot(x='type',y=name[i],data=tips,jitter=True)
   sns.violinplot(x='type',y=name[i],data=tips,color='.8')
plt.tight_layout()
plt.show()
plt.savefig("test2"+".pdf")
plt.close()
