# -*- coding:utf-8 -*-
# @Time : 2022/7/28 3:44 下午
# @Author : Bin Bin Xue
# @File : chart6_科学计算与机器学习
# @Project : python_data_analysis

'''
    6.1 Scipy科学计算库
        scipy常量包 - scipy.constants
        scipy积分包 - scipy.integrate

    6.2 scikit-learn机器学习库
        LinearRegression、LogisticRegression、KMeans
'''
# 案例1_用线性回归分析披萨尺寸与价格的关系，并预测
# from sklearn.linear_model import LinearRegression
# # 数据集-直径和价格
# x = [[5],[6],[7],[8],[10],[11],[13],[14],[16],[18]]
# y = [[6],[7.5],[8.6],[9],[12],[13.6],[15.8],[18.5],[19.2],[20]]
# clf = LinearRegression()
# clf.fit(x,y)
# print(clf.coef_)
# print(clf.intercept_)
# print(clf.predict([[12]]))

# 案例2_逻辑回归预测鸢尾花类别
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
#导入数据集
iris = load_iris()
print(iris.data)
print(iris.data.shape)
x = iris.data
y = iris.target
# 逻辑回归模型
lr = LogisticRegression(C=1e5)
lr.fit(x,y)
# 预测数据
X1 = [[5.1,3.5,1.4,0.2],[5.9,3.,5.1,1.8]]
print(lr.predict(X1))
