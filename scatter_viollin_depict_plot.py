#!python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import  numpy as np
import pandas as pd

tips = pd.read_csv("./IMPUT_FILE.csv")
print (tips)
name="Feature1,Feature2,Feature3,Feature4,Feature5,Feature6,Feature7,Feature8,Feature9,Feature10,Feature11,Feature12,Feature13,Feature14,Feature15,Feature16,Feature17,Feature18,Feature19".split(",")
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
