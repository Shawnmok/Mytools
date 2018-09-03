# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:16:30 2018

@author: moxiaodong
"""

import os
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_excel('D:\Projects\LADA\统计建议\e72.xlsx','e30')
data.describe()
name=data.columns.values.tolist()
type_set = set(data['type'])
compare_list=[]
for i in type_set:
    #compare_list.append(data.loc[data["type"]==i].index)
    compare_list=data.loc[data["type"]==i].index
    print(i,len(compare_list))
    for j in name:
        if j=="ID" or j=="type":
            continue
        m=data[j][compare_list].mean()
        st=data[j][compare_list].std()
        print('%s,%s,%0.3f±%0.3f'%(i,j,m,st))


for i in name:
    if i =='ID' or i == "type":
        continue
    formula1=str(i)+" ~ C(type)"
    results = ols(formula1, data=data).fit()
    print(results.summary())
