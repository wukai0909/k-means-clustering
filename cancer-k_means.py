# -*- coding: utf-8 -*- 
#导入相应的包
import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import numpy as np
import matplotlib.pylab as plt


#待聚类的数据点,cancer.csv有653行数据,每行数据有11维: 
dataset = np.loadtxt('cancer.csv', delimiter=",")
#np数据从0开始计算，第0维维序号排除，第10维为标签排除，所以为1到9
points = dataset[:,1:9]
cancer_label = dataset[:,10]
print "points:\n",points
print "cancer_label:\n",cancer_label
# k-means聚类
#将原始数据做归一化处理
data=whiten(points)
#使用kmeans函数进行聚类,输入第一维为数据,第二维为聚类个数k.
#有些时候我们可能不知道最终究竟聚成多少类,一个办法是用层次聚类的结果进行初始化.当然也可以直接输入某个数值. 
#k-means最后输出的结果其实是两维的,第一维是聚类中心,第二维是损失distortion,我们在这里只取第一维,所以最后有个[0]
#centroid = kmeans(data,max(cluster))[0]  
centroid = kmeans(data,2)[0]
print centroid
#使用vq函数根据聚类中心对所有数据进行分类,vq的输出也是两维的,[0]表示的是所有数据的label
label=vq(data,centroid)[0]
num = [0,0]
for i in label:
    if(i == 0):
        num[0] = num[0] + 1
    else:
        num[1] = num[1] + 1
print 'num =',num       
#np.savetxt('file.csv',label)
print "Final clustering by k-means:\n",label
result = np.subtract(label,cancer_label)
print "result:\n",result

count = [0,0]
for i in result:
    if(i == 0):
        count[0] = count[0] + 1
    else:
        count[1] = count[1] + 1
print count
print float(count[1])/(count[0]+count[1])
