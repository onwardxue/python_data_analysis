# -*- coding:utf-8 -*-
# @Time : 2022/7/28 3:40 下午
# @Author : Bin Bin Xue
# @File : chart5_数据可视化
# @Project : python_data_analysis

'''
    5.1 Matplotliv可视化
        1_Matplotlib基本图形
            设置中文：plt.rcParams['font.sans-serif'] = ['SimHei']
            设置负号：plt.rcParams['axes.unicode_minus'] = False
            (1)折线图
                    plt.plot(x,y,'rs--')
            (2)柱状图
                    plt.bar(x,height,width)
            (3)散点图
                    plt.scatter(x,y,s,c,marker)
            (4)直方图和密度图
                    plt.hist(x,bins,color)
            (5)饼图
                    plt.pie(x,explode,labels,colors..)
            (6)箱型图
                    plt.boxplot(data,label..)
        2_Matplotlib自定义（同一张画布绘制多张图）
            第一步，创建画布：
                    fig=plt.figure(figure=(10,6))
            第二步，创建子图：
                    ax1=fig.add_subplot(2,2,1)
                    ax2=fig.add_subplot(2,2,2)..
            第三步，各子图绘图（标题、图例等）：
                    ax1.hist(..)
                    ax2.scatter(...)
            第四步，展示画布：
                    plt.show()
            或者，直接用数组存储子图：
                    fig,axes = plt.subplots(2,2) - axes[0,0]表示左上第一幅图
            其他：
                调整子图间距（缩小到0）：
                    plt.subplots_adjust(wspace=0,hspace=0)


    5.2 Pyecharts可视化
        商业级图表库，是百度开源的可视化javascripts库，用于生成商业级数据图表
        1_pyeCharts常用图形


'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy

print('-----折线图-----')
time = np.arange(1,11)
sales = np.random.randint(100,200,10)
plt.plot(time,sales,color='r',linewidth=1.0,marker='*',linestyle='--')
plt.plot(time,sales,'rs--')
plt.show()

print('-----柱状图-----')
# 两个分布
men_means = [20,30,40,50,60]
women_means = [25,32,34,20,25]
# 刻度标签
labels = ['G1','G2','G3','G4','G5']
x = np.arange(len(labels))
width = 0.35
# 绘制柱状图（设置图例名称）
rects1 = plt.bar(x - width/2,men_means,width,label='men_means')
rects2 = plt.bar(x + width/2,women_means,width,label='women_means')
# 设置坐标名称
plt.xlabel('Groups')
plt.ylabel('Scores')
# 设置图片名
plt.title('Score by group and gender')
# 设置x轴刻度值
plt.xticks(x,labels)
# 显示图例
plt.legend(loc='best')
# 显示图片
plt.show()

print('-----散点图-----')
a = np.random.randn(100)
b = np.random.randn(100)
plt.scatter(a,b,s=np.power(5*a+10*b,2),c=np.random.randn(100),marker='o')
plt.xlabel('X value')
plt.ylabel('y value')
plt.title('Scatter Diagram')
plt.show()

print('-----直方图和密度图-----')
#密度图就是在直方图的基础上加了分布曲线
x = np.random.randint(50,101,size=100)
plt.hist(x,bins=20,density=True,color='g',alpha=0.75)
s = pd.Series(x)
s.plot(kind='kde',linestyle='--')
plt.show()

print('-----饼图-----')
labels = ['A','B','C','D']
data = [15,30,45,10]
explode = (0,0.1,0,0)
colors = ['r','g','b','y']
plt.pie(data,explode=explode,labels=labels,shadow=True,startangle=90,textprops={'fontsize':12,'color':'black'})
plt.axis('equal')
plt.legend(loc='upper right')
plt.title('Pie Graph', fontsize=16)
plt.show()

print('-----箱型图-----')
testA = np.random.rand(500)
testB = np.random.rand(500)
labels = ['testA','testB']
data = [testA,testB]
plt.boxplot(data,labels=labels,showmeans=True)
plt.title('BoxPlot')
plt.show()

print('-----绘制子图-----')
fig,axes = plt.subplots(2,2,sharex=True,sharey=True,figsize=(10,6))
for i in range(2):
    for j in range(2):
        axes[i,j].plot(np.random.randn(50).cumsum(),'b--')
# 子图间距缩小为0
plt.subplots_adjust(wspace=0,hspace=0)
plt.show()