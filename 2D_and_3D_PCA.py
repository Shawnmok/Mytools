#!python
# Code source: Gaël Varoquau
# Modified for documentation by Jaques Grobler
# Modified by Xiaodong
# License: BSD 3 clause
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from numpy import array,zeros,shape,tile
import matplotlib.patches as mpatches
# import some data to play with
#iris = datasets.load_iris()
#X = iris.data[:, :2]  # we only take the first two features.
#y = iris.target

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals



IN=open("./test.txt","r")
X=[]
y=[]
k=[]
''''TA','LADA',"control","T2D"'''
IN.readline()
for i in IN:
    irr=i.strip().split()
    if irr[-1]=="TA":
        kl="TA"
        label="indigo"
    elif irr[-1]=="LADA":
        continue
        kl="LADA"
        label="darkorange"
    elif irr[-1]=="control":
        kl="control"
        label="forestgreen"
    elif irr[-1]=="T2D":
        kl="T2D"
        label="cornflowerblue"

    snp=irr[0:-1]
    #snp=map(int,snp[:])
    snp2=[]
    for ss in snp:
        if ss=="NA":
            ss= float('nan')
        snp2.append(float(ss))
    y.append(label)
    k.append(kl)
    X.append(snp2)
X=array(X)
y=array(y)

X,rr,cc=autoNorm(X)

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.savefig("pca2d2.png")
# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(X)
colors = ['black', 'darkorange', 'forestgreen','cornflowerblue']
target_names=["TA",'LADA',"control","T2D"]
ax.legend(loc='best', shadow=False, scatterpoints=1)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='w', s=30)

patch1 = mpatches.Patch(color='black', label='TA')
patch2 = mpatches.Patch(color='darkorange', label='LADA')
patch3 = mpatches.Patch(color='forestgreen', label='control')
patch4 = mpatches.Patch(color='cornflowerblue', label='T2D')
plt.legend(handles=[patch1,patch2,patch3,patch4])
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()
plt.savefig("PCA3d2.pdf")
