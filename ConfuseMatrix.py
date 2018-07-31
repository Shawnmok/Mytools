# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:49:04 2018

@author: moxiaodong
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
# 调用魔法方法 使得每次显示结果时不用调用plt.show()方法
sns.set(style='white', color_codes=True)
# 设置默认风格
plt.figure(frameon=True,edgecolor="k")
np.random.seed(sum(map(ord, 'categorical')))
data = np.array([[0.86,0.14,0.00],[0.26,0.74,0.00],[0.00,0.00,0.99]])
sns.heatmap(data,annot=True,cmap="Blues",xticklabels=["T1D","LADA","T2D"]\
            , yticklabels=["T1D","LADA","T2D"], linecolor= 'k',linewidths = 0.05)
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Overall accurancy=0.86')
print(data)
plt.savefig("ConfuseMatrix.pdf")
